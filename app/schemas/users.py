from enum import StrEnum
from typing import Optional

from schemas.base_model import BaseModel


class UserRole(StrEnum):
    DRIVER = "DRIVER"
    EMPLOYEE = "EMPLOYEE"
    LOGIST = "LOGIST"


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    password: str
    role: Optional[UserRole]


class UserModel(UserCreate):
    id: int
