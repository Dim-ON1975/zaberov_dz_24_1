from rest_framework import serializers

from lms.models import Course, Lesson



class CourseSerializer(serializers.ModelSerializer):
    lessons_list = serializers.SerializerMethodField()
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance.pk).count()

    def get_lessons_list(self, instance):
        lessons_list = []
        for lesson in Lesson.objects.filter(course=instance.pk):
            lessons_list.append({
                "pk": lesson.pk,
                "title": lesson.title,
                "description": lesson.description,
                "video": lesson.video_url
            })
        return lessons_list

    class Meta:
        model = Course
        fields = ('creator', 'title', 'description', 'lesson_count', 'lessons_list',)
