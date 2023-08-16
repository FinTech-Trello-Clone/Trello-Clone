from django.shortcuts import render
from .serializers import UserRegisterSerialzier
from rest_framework.generics import CreateAPIView


class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerialzier
    

