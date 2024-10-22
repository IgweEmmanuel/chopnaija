from rest_framework import serializers
from .models import Store, Category, Product, QuantityVariant, ColorVariant, SizeVariant
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
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


class ProductSerializer(serializers.ModelSerializer):
    # Assuming category and shop are related models
    category = CategorySerializer()
    store = StoreSerializer()

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        # Extract nested data
        category_data = validated_data.pop('category')
        store_data = validated_data.pop('store')
        
        # Fetch category and store instances (or create if they don't exist)
        category = Category.objects.get_or_create(slug=category_data)
        store = Store.objects.get_or_create(slug=store_data)
        
        # Now create the Product object
        product = Product.objects.create(category=category, store=store, **validated_data)
        return product
