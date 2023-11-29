from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from database import Base
from enums import UserStatus


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=False, nullable=False)
    last_name = Column(String, unique=False, nullable=False)
    password = Column(String, unique=False, nullable=False)
    role = Column(String, Enum(UserStatus), nullable=False)
