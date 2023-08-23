from rest_framework import serializers
from .models import (
    Board,
    BoardMember,
    TaskCondition,
    TaskItem,
    SubTask
)
from api.utilitie.serializer import CustomAbstractSerializer

class BoardCreateSerializer(CustomAbstractSerializer):
    class Meta:
        model = Board
        fields = ("id", "title", "creator")

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['creator'] = user
        board = Board.objects.create(**validated_data)
        return board


class TaskConditionSerializer(CustomAbstractSerializer):

    class Meta:
        model = TaskCondition
        fields = ("id", "title", "creator", "board", "description")


    def create(self, validated_data):
        user = self.context['request'].user
        linked_board = validated_data.get('board')

        if linked_board.creator == user:
            validated_data['creator'] = user
            task_condition = TaskCondition.objects.create(**validated_data)
            return task_condition
        else:
            raise serializers.ValidationError("You can only link to your own boards !!!")
        

class TaskItemSerializer(CustomAbstractSerializer):

    class Meta:
        model = TaskItem
        fields = ("id", "title", "creator", "task_condition")

    def create(self, validated_data):
        user = self.context['request'].user
        task_condition = validated_data.get('task_condition')

        if task_condition.creator == user:
            validated_data['creator'] = user
            task_item = TaskItem.objects.create(**validated_data)
            return task_item
        else:
            raise serializers.ValidationError("You can only link to your own Tasks !!!")

class SubTaskSerializer(CustomAbstractSerializer):
    class Meta:
        model = SubTask
        fields = ("id", "title", "task_item")

class BoardMemberSerializer(CustomAbstractSerializer):
    class Meta:
        model = BoardMember
        fields = ("id", "board", "member")
    
    def create(self, validated_data):
        user = self.context['request'].user
        board = validated_data.get("board")
        member = validated_data['member']
        board_members = BoardMember.objects.filter(board_id = board.id)

        for board_member  in board_members:
            if board_member.member == member:
                raise serializers.ValidationError("User exists")
        
        if member != user:
            board_member = BoardMember.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("Error saving user")
        