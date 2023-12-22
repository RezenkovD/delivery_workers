from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from database import Base
from enums import VehicleStatus


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    marka = Column(String, unique=False, nullable=False)
    model = Column(String, unique=False, nullable=False)
    status = Column(String, Enum(VehicleStatus), nullable=False)
