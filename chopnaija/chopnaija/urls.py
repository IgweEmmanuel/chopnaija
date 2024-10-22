"""
URL configuration for chopnaija project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerSplitView
from rest_framework.routers import DefaultRouter
from store.views import CategoryView, StoreView, ProductView
from cart.views import CartViewSet

router = DefaultRouter()
router.register(r"category", CategoryView, basename="category")
# router.register(r"category/<category_slug>", views.CategoryView, basename="category-slug")
router.register(r"store", StoreView, basename="store")
router.register(r"product", ProductView, basename="product")
router.register(r"cart", CartViewSet, basename="cart")
# router.register(r"demo", views.DemoView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include('accounts.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerSplitView.as_view(url_name="schema")),
]
