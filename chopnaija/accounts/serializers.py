from rest_framework import serializers
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'is_vendor', 'is_customer', 'profile', 'created_at', 'updated_at']
        read_only_fields = ['is_vendor', 'is_customer', 'created_at', 'updated_at']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        instance = super().update(instance, validated_data)

        # Update the profile data if exists
        if profile_data:
            profile = instance.profile
            profile.address = profile_data.get('address', profile.address)
            profile.phone_number = profile_data.get('phone_number', profile.phone_number)
            profile.save()
        return instance
    
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password', 'confirm_password', 'is_vendor', 'is_customer']

#     def create(self, validated_data):
#         if validated_data['password'] != validated_data['confirm_password']:
#             raise serializers.ValidationError("Passwords do not match")
#         validated_data.pop('confirm_password')
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             password=validated_data['password'],
#             is_vendor=validated_data.get('is_vendor', False),
#             is_customer=validated_data.get('is_customer', False)
#         )
#         # user.set_password(validated_data['password'])
#         # user.save()
#         return user
