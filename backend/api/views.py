from django.shortcuts import render
from api import serializer as api_serializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from django.conf import settings
from core.models import CustomUser, Profile
import secrets




# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer
    
# ----------------------------------------
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
# ----------------------------------------


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer


def generate_secret_otp(length=6):
    otp = ''.join([str(secrets.randbelow(10)) for _ in range(length)])
    return otp

class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def get_object(self):
        email = self.kwargs['email']
        user = CustomUser.objects.filter(email=email).first()

        if user:
            uuid64 = user.pk
            user.otp = generate_secret_otp()
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)
            user.refresh_token = refresh_token
            user.save()

            link = f"http://localhost:5173/create-new-password/?otp={user.otp}&uuid64={uuid64}&refresh_token={refresh_token}"

            context_dictionary = {
                "link": link,
                "username": user.username,
            }            

            subject = "Password Reset"
            text_body = render_to_string("email/password_reset.txt", context_dictionary)
            html_body = render_to_string("email/password_reset.html", context_dictionary)
            msg =  EmailMultiAlternatives(subject=subject, from_email=settings.DEFAULT_FROM_EMAIL, to=[user.email], body=text_body)
            msg.attach_alternative(html_body, "text/html")
            msg.send()
            print('link ======= ', link)
        return user

class PasswordChangeAPIView(generics.CreateAPIView):
    permission_class = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def create(self, request, *args, **kwargs):
        otp = request.data['otp']
        uuid64 = request.data['uuid64']
        password = request.data['password']

        user = CustomUser.objects.get(otp=otp, uuid64=uuid64)
        if user:
            user.set_password(password)
            user.otp = ''
            user.save()
        
            return Response({'Message': 'Password Changed Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message': 'User Does not Exist!'}, status=status.HTTP_404_NOT_FOUND)   