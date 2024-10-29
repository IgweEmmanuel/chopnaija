from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    """
    CustomUserAdmin
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'city', 'state', 'phone_number', 'address', 'password1', 'password2'),
        }),
    )
    pass
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'country', 'about', 'date']
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)

