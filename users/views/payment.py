from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from users.models import Payment
from users.serializers.payment import PaymentSerializer


class PaymentSerializeListAPIView(generics.ListAPIView):
    """Вывод пробега с фильтрацией по машинам или мотоциклам с сортировкой по году"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    # Фильтрация и сортировка
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_pay', 'lesson_pay', 'method_pay',)
    ordering_fields = ('date_pay',)
