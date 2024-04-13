from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50,
        blank=True, null=True)
    email = models.EmailField(max_length=50,
        blank=True, null=True)
    username = models.CharField(unique= True, max_length=50,
        blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username

