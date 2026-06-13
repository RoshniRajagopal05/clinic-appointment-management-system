
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('RECEPTIONIST', 'Receptionist'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='RECEPTIONIST'
    )

    def __str__(self):
        return self.username