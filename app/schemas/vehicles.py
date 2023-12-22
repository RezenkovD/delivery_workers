from enum import StrEnum
from typing import Optional

from schemas.base_model import BaseModel


class VehicleStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class VehicleCreate(BaseModel):
    marka: str
    model: str
    status: Optional[VehicleStatus]


class VehicleModel(VehicleCreate):
    id: int
