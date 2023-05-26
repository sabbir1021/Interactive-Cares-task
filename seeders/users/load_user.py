from accounts.models import User
from seeders.users.factories import UserFactory

NUM_USER = 30


def run():
    User.objects.all().delete()
    for _ in range(NUM_USER):
        UserFactory()
    return
