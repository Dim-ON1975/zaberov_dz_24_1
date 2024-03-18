from rest_framework import serializers

from lms.models import Course
from users.models import User, Payment
from users.serializers.payment import PaymentSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerList(serializers.ModelSerializer):
    payer = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
