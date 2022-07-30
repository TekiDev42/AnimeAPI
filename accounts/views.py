"""
API REST USER
"""
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from accounts.models import User
from accounts.serializers.RegisterSerializer import RegisterSerializer
from accounts.serializers.UserTokenObtainPairSerializer import UserTokenObtainPairSerializer


class UserTokenObtainView(TokenObtainPairView):
    renderer_classes = [JSONRenderer]
    serializer_class = UserTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    renderer_classes = [JSONRenderer]
