import factory
from factory.django import DjangoModelFactory

from .models import DoitUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = DoitUser

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
