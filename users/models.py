from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    email_verify = models.BooleanField(default=False, verbose_name='верификация почты')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    settlement = models.CharField(max_length=100, verbose_name='населённый пункт', **NULLABLE)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', **NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def natural_key(self):
        """Для сериализации связанных данных"""
        return self.pk, self.email, self.email_verify, self.phone, self.settlement, self.avatar

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
