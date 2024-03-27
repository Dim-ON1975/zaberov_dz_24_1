from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='создатель')
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lms/courses/previews/', **NULLABLE, verbose_name='логотип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE, verbose_name='создатель')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='lesson')
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lms/lessons/previews/', **NULLABLE, verbose_name='логотип')
    video_url = models.URLField(verbose_name='видео')

    def __str__(self):
        return f'{self.course}: {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    """ Модель подписки пользователя на курс """
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE, verbose_name='подписчик',
                                   related_name='subscriber')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                               related_name='subscription')

    def __str__(self):
        return f'{self.subscriber}: {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
