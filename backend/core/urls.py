from django.urls import path
from .views import CustomUserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'user', CustomUserViewSet)
# router.register(r'categories', CategoryViewSet)



urlpatterns = [
    path('', include(router.urls), name='get_users'),
    path('api/', include(router.urls), name='create_user'),
]
