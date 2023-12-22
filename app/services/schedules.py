from database import UnitOfWork
from repositories.impl import ScheduleRepository, UserRepository
from models import Schedule, User
from sqlalchemy.orm import Session
from schemas import ScheduleCreate, ScheduleModel, UserRole, ScheduleStatus


def create_schedule(
    unit_of_work: Session, logist_id: int, schedule_data: ScheduleCreate
) -> ScheduleModel:
    if (
        schedule_data.departure_location is None
        or schedule_data.arrival_location is None
        or schedule_data.departure_time is None
        or schedule_data.arrival_time is None
    ):
        raise ValueError("All fields must be filled!!!")

    if schedule_data.departure_time > schedule_data.arrival_time:
        raise ValueError("Departure time cannot be later than arrival time!!!")

    with unit_of_work as uow:
        user_repo = UserRepository(uow._session)
        user = user_repo.get_by_id(logist_id)
        if user is None:
            raise ValueError("No user found with this id!!!")
        if user.role != UserRole.LOGIST:
            raise ValueError("You are not logist!!!")

        shedule_repo = ScheduleRepository(uow._session)
        schedule_data = Schedule(
            **schedule_data.dict(), logist_id=logist_id, status=ScheduleStatus.ACTIVE
        )
        schedule_data = shedule_repo.create(schedule_data)
        uow.commit()

        return schedule_data
