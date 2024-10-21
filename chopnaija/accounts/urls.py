from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import DefaultRouter
# ffrom django.urls import path, include
from .views import UserViewSet, VendorProfileView, CustomerProfileView

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users' )
router.register(r'vendors', VendorProfileView, basename='vendors')
router.register(r'customers', CustomerProfileView, basename='customers')
# router.register(r'register', RegisterView, basename='register')
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
