from rest_framework import generics

from lms.models import Lesson
from lms.paginators import LmsPaginator
from lms.permissions import IsModerator, IsCreator
from lms.serializers.lesson import LessonSerializer
from rest_framework.permissions import IsAuthenticated


class LessonSerializeListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsCreator]
    pagination_class = LmsPaginator


class LessonSerializeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsCreator | IsModerator]


class LessonSerializeCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        """Привязка пользователя к создаваемому уроку"""
        new_lesson = serializer.save()
        new_lesson.creator = self.request.user
        new_lesson.save()


class LessonSerializeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsCreator | IsModerator]


class LessonSerializeDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsCreator | ~IsModerator]
