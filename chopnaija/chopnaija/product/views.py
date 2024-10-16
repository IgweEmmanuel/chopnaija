from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
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