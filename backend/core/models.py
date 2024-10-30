from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets
from django.db.models.signals import post_save
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    otp = models.CharField(max_length=100, null=True, blank=True)
    refresh_token = models.CharField(max_length=1000, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)

    def save(self, *args, **kwargs):
        email_username, full_name = self.email.split('@')
        if self.username == "" or self.username == None:
            self.username = email_username
        if self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        if self.otp == "" or self.otp == None:
            d = 6
            dt = ''.join([str(secrets.randbelow(10)) for _ in range(d)])
            self.otp = dt
        super(CustomUser, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_folder', default='user_image.jpeg', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)