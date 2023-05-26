from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    image = models.URLField(blank=True)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "1. User"

    def __str__(self):
        return self.username