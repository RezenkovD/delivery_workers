from sqlalchemy.orm import Session
from models import Vehicle

from repositories.impl import BaseRepository


class VehicleRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Vehicle)
