from rest_framework import serializers
from .models import Shop, Category, Product, QuantityVariant, ColorVariant, SizeVariant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = "__all__"
        
class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = "__all__"

class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = "__all__"

from rest_framework import serializers
from .models import Product, Category, Shop

class ProductSerializer(serializers.ModelSerializer):
    # Assuming category and shop are related models
    category = CategorySerializer()
    shop = ShopSerializer()

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        # Extract nested data
        category_data = validated_data.pop('category')
        shop_data = validated_data.pop('shop')
        
        # Fetch category and shop instances (or create if they don't exist)
        category = Category.objects.get(slug=category_data)
        shop = Shop.objects.get(slug=shop_data)
        
        # Now create the Product object
        product = Product.objects.create(category=category, shop=shop, **validated_data)
        return product
