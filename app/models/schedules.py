import datetime

from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from database import Base
from enums import ScheduleStatus


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    departure_location = Column(String, unique=False, nullable=False)
    arrival_location = Column(String, unique=False, nullable=False)
    departure_time = Column(
        DateTime, default=datetime.datetime.utcnow(), nullable=False
    )
    arrival_time = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)
    logist_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, Enum(ScheduleStatus), nullable=False)
