# from rest_framework import serializers
# from .models import CustomUser

# class CustomUserSerializer(serializers.ModelSerializer):
#     """
#     CustomUserSerializer
#     """
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'city', 'state', 'phone_number', 'address']


# serializers.py
from rest_framework import serializers
from .models import CustomUser
from .models import Profile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'otp', 'refresh_token']
        read_only_fields = ['uploaded_by', 'upload_date']
# user/serializers.py


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # or specify fields explicitly: ['image', 'full_name', 'country', 'about', 'date']