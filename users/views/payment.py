from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import serializers
from users.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentSerializeListAPIView(generics.ListAPIView):
    """Вывод информации об оплате"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    # Фильтрация и сортировка
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_pay', 'lesson_pay', 'method_pay',)
    ordering_fields = ('date_pay',)
