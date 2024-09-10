from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=150, unique=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
