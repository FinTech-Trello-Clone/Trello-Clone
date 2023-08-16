from rest_framework import serializers
from .models import (
    Board,
    TaskCondition,
    TaskItem,
)


class BoardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ("id", "title",)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['creator'] = user
        board = Board.objects.create(**validated_data)
        return board

        
class TaskConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskCondition
        fields = ("id", "title", "creator", "created_at", "board",)



    def create(self, validated_data):
        user = self.context['request'].user
        linked_board = validated_data.get('board')

        if linked_board.creator == user:
            validated_data['creator'] = user
            task_condition = TaskCondition.objects.create(**validated_data)
            return task_condition
        else:
            raise serializers.ValidationError("You can only link to your own boards !!!")
        

class TaskItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskItem
        fields = ("id", "title", "created_at", "creator", "task_condition",)

    def create(self, validated_data):
        user = self.context['request'].user
        task_condition = validated_data.get('task_condition')

        if task_condition.creator == user:
            validated_data['creator'] = user
            task_item = TaskItem.objects.create(**validated_data)
            return task_item
        else:
            raise serializers.ValidationError("You can only link to your own Tasks !!!")
        