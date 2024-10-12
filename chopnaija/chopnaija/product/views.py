from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response

class CategoryView(viewsets.ViewSet):
    """Category view

    Args:
        viewsets: views for client
    """
    queryset = Category.objects.all()
    
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)