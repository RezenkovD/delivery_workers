import factory

from models import User
from enums import UserRole

from .base_factory import BaseFactory


class UserFactory(BaseFactory):
    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    role = UserRole.DRIVER

    class Meta:
        model = User
