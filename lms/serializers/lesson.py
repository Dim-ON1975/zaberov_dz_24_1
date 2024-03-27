from rest_framework import serializers

from lms.models import Lesson
from lms.validators import VideoURLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        # Валидация
        validators = [
            # Проверка на использование допустимых url в адресе видео
            VideoURLValidator(field='video_url'),
        ]
