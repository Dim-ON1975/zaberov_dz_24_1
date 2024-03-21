from django import forms
from rest_framework import serializers

from lms.models import Course
from users.models import User, Payment
from users.serializers.payment import PaymentSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Скрыть пароль в профиле"""
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserSerializerList(serializers.ModelSerializer):
    payer = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


# class UserLimitedSerializer(serializers.ModelSerializer):
#     """Исключает отображение пароля и фамилии"""
#
#     class Meta:
#         model = User
#         exclude = ('password', 'last_name',)
