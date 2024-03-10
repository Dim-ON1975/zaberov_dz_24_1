from rest_framework import viewsets

from users.models import User
from users.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
