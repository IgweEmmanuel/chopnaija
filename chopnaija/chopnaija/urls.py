"""
URL configuration for chopnaija project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerSplitView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('core.urls')),
    # path('', include(router.urls)),
    # path('api/core/', include('core.urls')),
    # path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    # path('api/schema/docs/', SpectacularSwaggerSplitView.as_view(url_name="schema")),
]
