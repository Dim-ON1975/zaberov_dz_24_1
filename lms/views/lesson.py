from rest_framework import generics

from lms.models import Lesson
from lms.serializers.lesson import LessonSerializer


class LessonSerializeListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonSerializeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonSerializeCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonSerializeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonSerializeDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
