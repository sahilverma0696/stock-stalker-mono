# Create your views here.
# users/views.py
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

