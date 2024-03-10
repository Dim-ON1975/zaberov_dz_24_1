from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title', 'description', 'preview',)
    list_filter = ('creator', 'title', 'description',)
    search_fields = ('creator', 'title', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'description', 'preview', 'video_url')
    list_filter = ('course', 'title', 'description',)
    search_fields = ('course', 'title', 'description',)


