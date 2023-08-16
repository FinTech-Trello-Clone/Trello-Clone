from django.urls import path
from .views import (
    BoardApi,
    BoardEditApi,
    TaskConditionApi,
    TaskConditionsEdit,
    TaskItemApi,
    TaskItemEdit

)

urlpatterns = [
    path('board/create/', BoardApi.as_view()),
    path('board/edit/<int:pk>/',BoardEditApi.as_view()),
    path('board/get/<int:pk>/',BoardEditApi.as_view()),
    path('board/delete/<int:pk>/',BoardEditApi.as_view()),

    path('task/create/',TaskConditionApi.as_view()),
    path('task/edit/<int:pk>/',TaskConditionsEdit.as_view()),
    path('task/get/<int:pk>/',TaskConditionsEdit.as_view()),
    path('task/delete/<int:pk>/',TaskConditionsEdit.as_view()),

    path('taskitem/create/',TaskItemApi.as_view()),
    path('taskitem/edit/<int:pk>/',TaskItemEdit.as_view()),
    path('taskitem/get/<int:pk>/',TaskItemEdit.as_view()),
    path('taskitem/delete/<int:pk>/',TaskItemEdit.as_view()),


]