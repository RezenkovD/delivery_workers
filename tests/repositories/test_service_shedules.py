from datetime import datetime, timedelta

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest.mock import Mock

from database import UnitOfWork
from services import create_schedule
from models import User, Schedule
from schemas import ScheduleCreate, ScheduleModel
from repositories.impl import ScheduleRepository
from enums import UserRole


class TestCreateSchedule(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Session = sessionmaker(bind=engine)
        self.session = Session()

        User.metadata.create_all(bind=engine)
        Schedule.metadata.create_all(bind=engine)

        self.unit_of_work = UnitOfWork(lambda: self.session)

        with self.unit_of_work as uow:
            user1 = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.LOGIST,
            )
            self.user1 = uow.users.create(user1)

            user2 = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.DRIVER,
            )
            self.user2 = uow.users.create(user2)

            uow.commit()

    def tearDown(self):
        User.metadata.drop_all(bind=self.session.bind)

    def test_create_schedule_with_valid_data(self):
        valid_schedule_data = ScheduleCreate(
            departure_location="Location A",
            arrival_location="Location B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=1),
        )

        result = create_schedule(self.unit_of_work, self.user1.id, valid_schedule_data)

        self.assertIsNotNone(result.id)

    def test_create_schedule_with_invalid_data(self):
        invalid_schedule_data = ScheduleCreate(
            departure_location="Location A",
            arrival_location="Location B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() - timedelta(hours=1),
        )

        with self.assertRaises(ValueError) as context:
            create_schedule(self.unit_of_work, self.user1.id, invalid_schedule_data)

        self.assertEqual(
            str(context.exception),
            "Departure time cannot be later than arrival time!!!",
        )

    def test_create_schedule_with_invalid_user_id(self):
        invalid_user_id = 9999

        schedule_data = ScheduleCreate(
            departure_location="Location A",
            arrival_location="Location B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=1),
        )

        with self.assertRaises(ValueError) as context:
            create_schedule(self.unit_of_work, invalid_user_id, schedule_data)

        self.assertEqual(str(context.exception), "No user found with this id!!!")

    def test_create_schedule_with_invalid_user_role(self):
        schedule_data = ScheduleCreate(
            departure_location="Location A",
            arrival_location="Location B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=1),
        )

        with self.assertRaises(ValueError) as context:
            create_schedule(self.unit_of_work, self.user2.id, schedule_data)

        self.assertEqual(str(context.exception), "You are not logist!!!")


if __name__ == "__main__":
    unittest.main()
