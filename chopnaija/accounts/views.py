# from django.shortcuts import render
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# # from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import RegisterSerializer
# from rest_framework import status
# from drf_spectacular.utils import extend_schema

# class RegisterView(ViewSet):
#     # permission_classes = [IsAuthenticated]
#     @extend_schema(request=RegisterSerializer, responses={201:RegisterSerializer, 204:"No data provided", 400:"Bad Request"})
#     def create(self, request):
#         if request.data:
#             serializer = RegisterSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "No data provided"}, status=status.HTTP_204_NO_CONTENT)


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .permissions import IsVendor, IsCustomer
from django.contrib.auth.models import Group

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(UserViewSet, self).get_permissions()

    def perform_create(self, serializer):
        user = serializer.save()
        # Assign default group based on user type
        if user.is_vendor:
            group, _ = Group.objects.get_or_create(name='Vendors')
            user.groups.add(group)
        else:
            group, _ = Group.objects.get_or_create(name='Customers')
            user.groups.add(group)

class VendorProfileView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsVendor]

    def get_queryset(self):
        return User.objects.filter(is_vendor=True)

class CustomerProfileView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return User.objects.filter(is_customer=True)
