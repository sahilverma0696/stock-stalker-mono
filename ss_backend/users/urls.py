# users/urls.py
from django.urls import path
from .views import UserCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/',obtain_auth_token),
    path('signup/', UserCreateView.as_view(), name='user-create'),
]
