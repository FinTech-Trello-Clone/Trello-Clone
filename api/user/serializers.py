from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import User
from api.home.serializers import BoardCreateSerializer
from api.home.models import Board, BoardMember
from django.db.models import Q


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_board(self,user):
        boards = Board.objects.select_related('creator',).filter(
            Q(creator=user) | Q(board_member__member=user)
        )
        return boards

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        boards = self.get_board(user).values("id", 'title')
        data['data'] = {
            'id': user.id,
            "phone": user.phone,
            "boards": boards
        }
        return data


class UserRegisterSerialzier(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True, required=True)
    password2 = serializers.CharField(max_length=255, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone','password1', 'password2')

    def validate(self, attrs):
        data = super().validate(attrs)
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if (not password1 or not password2) or (password1 != password2):
            raise serializers.ValidationError("Paswords not given or not mutch")
        return data

    def create(self, validated_data):
        user = User(
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password1'])
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            validated_data.pop('password')
        for key, value in validated_data.items():
            setattr(instance,key, value)
        instance.save()
        return instance
    