from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from lms.models import Course
from lms.paginators import LmsPaginator
from lms.permissions import IsModerator, IsCreator
from lms.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LmsPaginator

    def perform_create(self, serializer):
        """Привязка пользователя к создаваемому курсу"""
        new_course = serializer.save()
        new_course.creator = self.request.user
        new_course.save()

    def get_permissions(self):
        """Ограничения ролей"""
        if self.action in ('list', 'retrieve', 'update', 'partial_update',):
            self.permission_classes = [IsCreator | IsModerator]
        if self.action in ('create',):
            self.permission_classes = [~IsModerator]
        if self.action in ('destroy',):
            self.permission_classes = [IsCreator | ~IsModerator]
        return super().get_permissions()
