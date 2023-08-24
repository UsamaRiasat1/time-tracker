from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='username',
    )

    email = models.EmailField(
        unique=True,
        verbose_name='email address',
    )

    password = models.CharField(
        max_length=128,
        verbose_name='password',
    )

    USERNAME_FIELD = 'username'
