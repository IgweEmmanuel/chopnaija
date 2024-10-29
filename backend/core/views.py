# from django.shortcuts import render
# from rest_framework import status
# # Create your views here.aa
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import CustomUserSerializer
# from .models import CustomUser

# @api_view(['GET'])
# def get_users(request):
#     """
#     Get all users
#     Args:
#         request (dict): request object

#     Returns:
#         dict : users data
#     """
#     users = CustomUser.objects.all()
#     serializer = CustomUserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_user(request):
#     """
#     Create a new user
#     Args:
#         request (dict): request object

#     Returns:
#         dict : user data
#     """
#     serializer = CustomUserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Viewset for CustomUser model
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset to only include the currently authenticated user's data.
        """
        if self.request.user.is_staff:
            raise PermissionDenied("You cannot access admin user data.")
        return self.queryset.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        """
        Ensure the currently authenticated user is set as the owner of the created object.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Ensure the currently authenticated user can only update their own data.
        """
        if serializer.instance.id != self.request.user.id:
            raise PermissionDenied("You can only update your own user data.")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Prevent the deletion of the superuser account.
        """
        if instance.is_superuser:
            raise PermissionDenied("You cannot delete the superuser account.")
        if instance.id != self.request.user.id:
            raise PermissionDenied("You can only delete your own user account.")
        instance.delete()