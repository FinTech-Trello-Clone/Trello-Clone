from django.shortcuts import render

from api.user.models import User
from .serializers import UserRegisterSerialzier, UserUpdateSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.models import TokenUser

class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerialzier
    
class UserEditApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsUser)
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return super().get_queryset()


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)