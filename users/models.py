from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.constants import MAX_CHAR_LENGTH, MAX_EMAIL_LENGTH


class CustomUser(AbstractUser):
    """переопределяем модель пользователя."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        verbose_name='Электронная почта',)
    username = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        unique=True,
        verbose_name='Логин',
        validators=([RegexValidator(
            regex=r'^(?!me$).*$',
            message='Неподходящий логин. "me" использовать запрещено.')]))
    password = models.CharField(max_length=MAX_CHAR_LENGTH,
                                verbose_name='пароль',
                                )

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username
