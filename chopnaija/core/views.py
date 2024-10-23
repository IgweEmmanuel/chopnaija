from django.shortcuts import render
from rest_framework import status
# Create your views here.aa
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser

@api_view(['GET'])
def get_users(request):
    """
    Get all users
    Args:
        request (dict): request object

    Returns:
        dict : users data
    """
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    """
    Create a new user
    Args:
        request (dict): request object

    Returns:
        dict : user data
    """
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)