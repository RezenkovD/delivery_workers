from sqlalchemy.orm import Session
from models import User
from repositories.interfaces import UserInterface


class BaseRepository:
    def __init__(self, session: Session, model_class) -> None:
        self._session: Session = session
        self._model_class = model_class

    def get_all(self):
        return self._session.query(self._model_class).all()

    def get_by_id(self, item_id):
        return (
            self._session.query(self._model_class)
            .filter(self._model_class.id == item_id)
            .first()
        )

    def create(self, item):
        self._session.add(item)
        self._session.flush()
        self._session.refresh(item)

    def update(self, item):
        existing_item = (
            self._session.query(self._model_class)
            .filter(self._model_class.id == item.id)
            .first()
        )
        if existing_item:
            existing_item.__dict__.update(item.__dict__)
            self._session.flush()
            self._session.refresh(existing_item)
        return existing_item

    def delete(self, item_id):
        item = (
            self._session.query(self._model_class)
            .filter(self._model_class.id == item_id)
            .first()
        )
        if item:
            self._session.delete(item)
            self._session.flush()
            return True
        else:
            return False
