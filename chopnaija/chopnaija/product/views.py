from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Shop, Product
from .serializers import CategorySerializer, ShopSerializer, ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

class CategoryView(viewsets.ViewSet):
    """Category view

    Args:
        viewsets: views for client access to database data
    """
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class ShopView(viewsets.ViewSet):
    """Category view

    Args:
        viewsets: views for client access to database data
    """
    queryset = Shop.objects.all()
    
    @extend_schema(responses=ShopSerializer)
    def list(self, request):
        serializer = ShopSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ProductView(viewsets.ViewSet):
    """Product view

    Args:
        viewsets: views for client access to database data
    """
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)