import datetime
from enum import StrEnum
from typing import Optional

from schemas.base_model import BaseModel


class ScheduleStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ScheduleCreate(BaseModel):
    departure_location: str
    arrival_location: str
    departure_time: datetime.datetime
    arrival_time: datetime.datetime
    logist_id: int
    status: Optional[ScheduleStatus]


class ScheduleModel(VehicleCreate):
    id: int
