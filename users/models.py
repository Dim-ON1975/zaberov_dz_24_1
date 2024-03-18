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

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    METHOD_PAY_CHOICES = (
        ('cash', 'наличные'),
        ('transfer', 'перевод'),
    )
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payer', verbose_name='плательщик')
    course_pay = models.ForeignKey('lms.Course', on_delete=models.CASCADE, related_name='course_pay', verbose_name='курс')
    lesson_pay = models.ForeignKey('lms.Lesson', on_delete=models.CASCADE, **NULLABLE, related_name='lesson_pay',
                                   verbose_name='урок')
    date_pay = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    amount_pay = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method_pay = models.CharField(max_length=8, choices=METHOD_PAY_CHOICES, verbose_name='способ оплаты')

    def __str__(self):
        return (f'{self.payer}: {self.course_pay if self.course_pay else self.lesson_pay} '
                f'({self.date_pay, self.amount_pay, self.method_pay})')

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
