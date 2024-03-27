from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    # Количество уроков курса
    lesson_count = serializers.SerializerMethodField()
    # Все уроки курса
    lesson = LessonSerializer(many=True, read_only=True)
    # Пользователь подписан на курс
    subscription = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        """ Количество уроков по курсу """
        return obj.lesson.count()

    def get_subscription(self, obj):
        """ Информация о подписке на курс """
        user = self.context['request'].user.pk
        if Subscription.objects.filter(subscriber_id=user, course_id=obj.pk):
            return True
        return False

    class Meta:
        model = Course
        fields = '__all__'
