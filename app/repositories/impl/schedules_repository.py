from sqlalchemy.orm import Session
from models import Schedule

from repositories.impl import BaseRepository


class ScheduleRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Schedule)
