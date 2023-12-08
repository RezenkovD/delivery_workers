from sqlalchemy.orm import Session
from models import User

from repositories.impl import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session, User)
