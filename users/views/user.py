from rest_framework import generics
from users.models import User
from users.serializers.user import UserSerializer, UserSerializerList
from rest_framework.permissions import IsAuthenticated


class UserSerializeListAPIView(generics.ListAPIView):
    serializer_class = UserSerializerList
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserSerializeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserSerializeCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Хеширование пароля при создании пользователя"""
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserSerializeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserSerializeDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
