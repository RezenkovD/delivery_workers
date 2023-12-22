from abc import ABC, abstractmethod
from typing import Callable
from sqlalchemy.orm import Session

from repositories.impl import UserRepository, ScheduleRepository


class UnitOfWorkBase(ABC):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()


class UnitOfWork(UnitOfWorkBase):
    def __init__(self, session_factory: Callable[[], Session]) -> None:
        self._session_factory: Callable[[], Session] = session_factory

    def __enter__(self):
        self._session: Session = self._session_factory()
        self.users = UserRepository(self._session)
        self.schedules = ScheduleRepository(self._session)
        return super().__enter__()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
