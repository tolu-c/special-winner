from rest_framework import serializers
from .models import PrivateFile
from django.contrib.auth.models import User


class PrivateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
