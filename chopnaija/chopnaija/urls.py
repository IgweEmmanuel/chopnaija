"""
URL configuration for chopnaija project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from chopnaija.product import views

router = DefaultRouter()
router.register(r"category", views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
