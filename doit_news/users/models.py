from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import DEFAULT_LENGTH_CHAR_FIELD


class DoitUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=DEFAULT_LENGTH_CHAR_FIELD, verbose_name='Имя')
    last_name = models.CharField(max_length=DEFAULT_LENGTH_CHAR_FIELD, verbose_name='Фамилия')
    username = models.CharField(max_length=DEFAULT_LENGTH_CHAR_FIELD, unique=True, verbose_name='Имя пользователя')
    password = models.CharField(max_length=DEFAULT_LENGTH_CHAR_FIELD, verbose_name='Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['date_joined']

    def __str__(self):
        return self.get_full_name()
