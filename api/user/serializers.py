from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data['data'] = {
            'id': user.id,
            "phone": user.phone
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
    

