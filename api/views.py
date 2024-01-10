from django.db import models
import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GeneratePassword
from .serializers import PasswordSerializer
from rest_framework.decorators import api_view

class PasswordGenerate(APIView):
    serializer_class = PasswordSerializer
    def post(self, request):
        data = request.data
        username = data.get('username')
        password_length = int(data.get('password_length', 8))
        include_uppercase = data.get('uppercase', True)
        include_lowercase = data.get('lowercase', True)
        include_numbers = data.get('numbers', True)
        special_characters = data.get('special_characters', True)

        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_numbers:
            characters += string.digits
        if special_characters:
            characters += string.punctuation

        if not characters:
            return Response({'error': "No character type selected"}, status=status.HTTP_400_BAD_REQUEST)

        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_data = {
            'username': username,
            'password': password
        }

        if GeneratePassword.objects.filter(username=username).exists():
            GeneratePassword.objects.filter(username=username).update(password=password)
            return Response({"status": "Password updated", "password": password}, status=status.HTTP_200_OK)
        else:
            serializer = self.serializer_class(data=password_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordListView(APIView):
    def get(self,request):
        passwords = GeneratePassword.objects.all()
        serializer = PasswordSerializer(passwords, many=True)
        return Response(serializer.data)
    

class PasswordDeleteView(APIView):
    def delete(self, request, pk):
        try:
            generate_password = GeneratePassword.objects.get(id=pk)
            generate_password.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GeneratePassword.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
   