from database import SessionLocal
from models import User
from repositories.interfaces import UserInterface


class UserSQLRepository(UserInterface):
    def get_all(self):
        session = SessionLocal()
        users = session.query(User).all()
        session.close()
        return users

    def get_by_id(self, id):
        session = SessionLocal()
        user = session.query(User).filter(User.id == id).first()
        session.close()
        return user

    def create(self, item):
        session = SessionLocal()
        session.add(item)
        session.commit()
        session.close()

    def update(self, item):
        session = SessionLocal()
        existing_user = session.query(User).filter(User.id == item.id).first()
        if existing_user:
            existing_user.first_name = item.first_name
            existing_user.last_name = item.last_name
            existing_user.password = item.password
            existing_user.role = item.role
            session.commit()
        session.close()

    def delete(self, id):
        session = SessionLocal()
        user = session.query(User).filter(User.id == id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()
