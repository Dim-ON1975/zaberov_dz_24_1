from rest_framework import serializers

from lms.models import Course
from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    payments_list = serializers.SerializerMethodField()

    def get_payments_list(self, instance):
        payments_list = []

        for payment in Payment.objects.filter(payer=instance.pk):
            payments_list.append({
                "pk": payment.pk,
                "course_pay": payment.course_pay_id,
                "lesson_pay": payment.lesson_pay_id,
                "date_pay": payment.date_pay,
                "amount_pay": payment.amount_pay,
                "method_pay": payment.method_pay
            })
        return payments_list

    class Meta:
        model = User
        fields = '__all__'
