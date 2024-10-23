from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'city', 'state', 'phone_number', 'address', 'password1', 'password2'),
        }),
    )
    pass

admin.site.register(CustomUser, CustomUserAdmin)
