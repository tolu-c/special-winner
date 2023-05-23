from rest_framework import serializers
from .models import PrivateFile
from django.contrib.auth.models import User


class PrivateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFile
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, clean_data):
        user_obj = User.objects.create_user(
            email=clean_data['email'], password=clean_data['password'], username=clean_data['username'])
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = User.objects.get(email=clean_data['email'])
        if user.check_password(clean_data['password']):
            return user
        raise serializers.ValidationError('Incorrect Credentials')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
