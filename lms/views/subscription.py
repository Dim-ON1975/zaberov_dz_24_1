from rest_framework import authentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from lms.models import Subscription, Course


class SubscriptionAPIView(APIView):
    """ Подписка пользователя на курс """

    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):

        # Пользователь
        user = self.request.user

        # id курса
        course_id = self.request.data.get('course_id')
        print(course_id)

        # Объект курса из базы
        course_item = get_object_or_404(Course, id=course_id)

        # Объекты подписок по текущему пользователю и курса
        subs_item = Subscription.objects.filter(subscriber=user, course=course_id)

        # Если подписка у пользователя на этот курс есть, то удаляем её.
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет, то создаём её.
        else:
            Subscription.objects.create(subscriber=user, course=course_item)
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})
