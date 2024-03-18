from django.urls import path
from users.apps import UsersConfig

from users.views.user import UserSerializeListAPIView, UserSerializeRetrieveAPIView, UserSerializeCreateAPIView, \
    UserSerializeUpdateAPIView, UserSerializeDestroyAPIView
from users.views.payment import PaymentSerializeListAPIView

app_name = UsersConfig.name

urlpatterns = [
    # Пользователь CRUD
    path('user/', UserSerializeListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserSerializeRetrieveAPIView.as_view(), name='user_get'),
    path('user/create/', UserSerializeCreateAPIView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserSerializeUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserSerializeDestroyAPIView.as_view(), name='user_retrieve'),
    # Оплата - Read (List)
    path('user/payment/', PaymentSerializeListAPIView.as_view(), name='user_payment'),
]
