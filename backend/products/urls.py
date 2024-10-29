# from django.urls import path
# from .views import products

# urlpatterns = [
#     path('products/', products, name='products'),
# ]


# products/urls.py
# products/urls.py
# project/urls.py
from django.contrib import admin
from chopnaija.settings import base
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(router.urls)),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularSwaggerView,
#     SpectacularRedocView
# )
# from .views import ProductViewSet, CategoryViewSet

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'categories', CategoryViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
#     # API Schema URLs
#     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     # Swagger UI
#     path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     # ReDoc UI
#     path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]