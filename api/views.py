from django.db import models
import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GeneratePassword
from rest_framework.decorators import api_view
from django.http import JsonResponse

def generate_random_password(length=8, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


@api_view(['GET', 'POST'])
def save_password(request):
    generated_password = generate_random_password()
    obj = GeneratePassword.objects.create(password=generated_password)
    print("New object created with ID:", obj.id)
    return JsonResponse({'msg': 'Password saved successfully', 'password': generated_password, 'id': obj.id}, status=201)


class PasswordListView(APIView):
    def get(self, request):
        passwords = GeneratePassword.objects.all()
        password_list = []
        print("list of password is", passwords)
        for password in passwords:
            password_data = {
                'id': password.id,
                'password': password.password,
            }
            password_list.append(password_data)

        return Response(password_list)
    

class PasswordDeleteView(APIView):
    def delete(self, request, pk):
        try:
            generate_password = GeneratePassword.objects.get(id=pk)
            generate_password.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GeneratePassword.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
   