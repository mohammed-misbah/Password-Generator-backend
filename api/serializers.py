from rest_framework.serializers import ModelSerializer
from .models import GeneratePassword
from rest_framework import serializers

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratePassword
        fields = ['id', 'username', 'password']

class PasswordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratePassword
        fields = ['id','username','password']

