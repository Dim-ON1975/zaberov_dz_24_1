from rest_framework import serializers

from lms.models import Course, Lesson
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    # Количество уроков курса
    lesson_count = serializers.SerializerMethodField()
    # Все уроки курса
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance.pk).count()

    class Meta:
        model = Course
        fields = '__all__'
