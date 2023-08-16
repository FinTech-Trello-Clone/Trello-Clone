from django.db import models

from api.user.models import User

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=13)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class TaskCondition(models.Model):
    title = models.CharField(max_length=13)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
class TaskItem(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task_condition = models.ForeignKey(TaskCondition, on_delete=models.CASCADE)

class BoardMember(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)