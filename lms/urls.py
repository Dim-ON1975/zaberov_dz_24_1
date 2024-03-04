from django.urls import path
from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views.course import CourseViewSet
from lms.views.lesson import LessonSerializeCreateAPIView, LessonSerializeUpdateAPIView, LessonSerializeDestroyAPIView, \
    LessonSerializeRetrieveAPIView, LessonSerializeListAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/', LessonSerializeListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonSerializeRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/create/', LessonSerializeCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/update/<int:pk>/', LessonSerializeUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonSerializeDestroyAPIView.as_view(), name='lesson_retrieve'),
              ] + router.urls
