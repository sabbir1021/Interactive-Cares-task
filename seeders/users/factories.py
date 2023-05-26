# For creating test data
import factory.fuzzy
from django.contrib.auth.hashers import make_password
from factory.django import DjangoModelFactory

from accounts.models import User

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("email")
    is_active = True
    password = factory.LazyFunction(lambda: make_password("default"))
