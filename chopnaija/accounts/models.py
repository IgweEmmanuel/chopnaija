# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save

# # Create your models here.
# class User(AbstractUser):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = ['username', 'password']

#     def __str__(self):
#         return self.username
    
#     def save(self, *args, **kwargs):
#         email_username, full_name = self.email.split('@')[0], self.email.split('@')[1]
#         if self.username is "" or self.username is None:
#             self.username = email_username
#             super(User, self).save(*args, **kwargs)
    
# class Profile(AbstractUser):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.first_name + " " + self.last_name

#     def save(self, *args, **kwargs):
#         if self.first_name == "" or self.first_name == None:
#             self.first_name = self.user.username
#         if self.last_name == "" or self.last_name == None:
#             self.last_name = self.user.username
#         super(Profile, self).save(*args, **kwargs)

# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# def save_profile(sender, instance, created, **kwargs):
#     instance.profile.save()
    
# post_save.connect(create_profile, sender=User)
# post_save.connect(save_profile, sender=User)


from django.db import models
from django.contrib.auth.models import AbstractUser
# Signals to automatically create profiles upon user creation
from django.db.models.signals import post_save
from django.dispatch import receiver
from chopnaija.settings import base

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=1000,unique=True)
    is_vendor = models.BooleanField(default=False)  # Vendor/farmer role
    is_customer = models.BooleanField(default=False)  # General customer role
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
        # Adding related_name to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        email_username = self.email.split('@')[0]
        if self.username is "" or self.username is None:
            self.username = email_username
            super(User, self).save(*args, **kwargs)
            
            
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.first_name == "" or self.first_name == None:
            self.first_name = self.user.username
        if self.last_name == "" or self.last_name == None:
            self.last_name = self.user.username
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
