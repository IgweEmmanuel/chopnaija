from rest_framework import serializers
from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """
    ProductSerializer
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'description', 'price', 'image']
