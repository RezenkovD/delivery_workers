import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import UnitOfWork
from models import User
from repositories.impl import BaseRepository
from enums import UserRole


class TestBaseRepository(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Session = sessionmaker(bind=engine)
        self.session = Session()

        User.metadata.create_all(bind=engine)

        self.unit_of_work = UnitOfWork(lambda: self.session)

    def tearDown(self):
        User.metadata.drop_all(bind=self.session.bind)

    def test_base_repository_get_all(self):
        with self.unit_of_work as uow:
            user_repository = BaseRepository(uow._session, User)

            users = user_repository.get_all()
            self.assertEqual(len(users), 0)

            user = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.DRIVER,
            )
            uow.users.create(user)

            users = user_repository.get_all()
            self.assertEqual(len(users), 1)

    def test_base_repository_get_by_id(self):
        with self.unit_of_work as uow:
            user_repository = BaseRepository(uow._session, User)

            non_existing_user = user_repository.get_by_id(1)
            self.assertIsNone(non_existing_user)

            user = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.DRIVER,
            )
            uow.users.create(user)

            retrieved_user = user_repository.get_by_id(user.id)
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(retrieved_user.first_name, "John")

    def test_base_repository_create(self):
        with self.unit_of_work as uow:
            user_repository = BaseRepository(uow._session, User)

            user = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.DRIVER,
            )

            user_repository.create(user)

            self.assertIsNotNone(user.id)

    def test_base_repository_update(self):
        with self.unit_of_work as uow:
            user_repository = BaseRepository(uow._session, User)

            user = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.DRIVER,
            )
            uow.users.create(user)

            user.first_name = "Updated Name"
            user_repository.update(user)

            updated_user = uow.users.get_by_id(user.id)
            self.assertIsNotNone(updated_user)
            self.assertEqual(updated_user.first_name, "Updated Name")

    def test_base_repository_delete(self):
        with self.unit_of_work as uow:
            user_repository = BaseRepository(uow._session, User)

            user = User(
                first_name="John",
                last_name="Doe",
                password="secret",
                role=UserRole.DRIVER,
            )
            uow.users.create(user)

            result = user_repository.delete(user.id)
            self.assertTrue(result)

            deleted_user = uow.users.get_by_id(user.id)
            self.assertIsNone(deleted_user)


if __name__ == "__main__":
    unittest.main()
