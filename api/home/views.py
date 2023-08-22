from django.shortcuts import render
from api.home.models import (
    Board,
    TaskCondition ,
    TaskItem,
    BoardMember,
    SubTask

)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,

)
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from api.home.serializers import (
    BoardCreateSerializer,
    TaskConditionSerializer,
    TaskItemSerializer,
    SubTaskSerializer,
    BoardMemberSerializer
)
from rest_framework.views import APIView
# Create your views here.
class BoardApi(
    ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer


    def get_queryset(self):
        user = self.request.user
        queryset = Board.objects.filter(creator=user)
        return queryset

class BoardMemberApi(ListCreateAPIView):
    permission_classes= (IsAuthenticated, )
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

class BoardMemberEditApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

class BoardEditApi(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Board.objects.filter(creator=user)
        return queryset


class TaskConditionApi(
    ListCreateAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskCondition.objects.all()
    serializer_class = TaskConditionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = TaskCondition.objects.filter(creator=user)
        return queryset


class TaskConditionsEdit(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskCondition.objects.all()
    serializer_class = TaskConditionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = TaskCondition.objects.filter(creator=user)
        return queryset




class TaskItemApi(
    ListCreateAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = TaskItem.objects.filter(creator=user)
        return queryset




class TaskItemEdit(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


    def get_queryset(self):
        user = self.request.user
        queryset = TaskItem.objects.filter(creator=user)
        return queryset



class SubTaskApi(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

class SubTaskEditApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

