from rest_framework import serializers
from .models import Shop, Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"