from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import UserRegisterSerializer
from django.contrib.auth import login
from django.http import JsonResponse
# Create your views here.
def welcome(request):
    message = "Welcome to our Django-React Native app!"
    return JsonResponse({'message': message})

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = serializer.save()
                login(request, user)  # Log in the user
                return Response({'msg': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if user.password == password:  # Check if the provided password matches the stored password
            login(request, user)
            serializer = UserRegisterSerializer(user)
            return Response({'user': serializer.data, 'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED), views.py