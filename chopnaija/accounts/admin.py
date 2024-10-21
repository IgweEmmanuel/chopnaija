from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'is_vendor', 'is_customer', 'is_staff')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
