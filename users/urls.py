from django.urls import path
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views.user import UserViewSet
from users.views.payment import PaymentSerializeListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
                  path('user/payment/', PaymentSerializeListAPIView.as_view(), name='user_payment'),
              ] + router.urls
