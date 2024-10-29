# from rest_framework import serializers
# from .models import Product
# from rest_framework import serializers


# class ProductSerializer(serializers.ModelSerializer):
#     """
#     ProductSerializer
#     """
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'slug', 'category', 'description', 'price', 'image']




# products/serializers.py
from rest_framework import serializers
from .models import Category, Product, ProductDetail, NutritionInfo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id', 'title']

class NutritionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionInfo
        fields = ['calories', 'fat', 'protein', 'carbs']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    details = ProductDetailSerializer(many=True, read_only=True)
    nutrition = NutritionInfoSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 
            'category',
            'name',
            'slug',
            'description',
            'price',
            'unit',
            'stock',
            'is_available',
            'rating',
            'reviews_count',
            'images',
            'details',
            'nutrition',
            'created_at',
            'updated_at'
        ]





# from rest_framework import serializers
# from .models import Category, Product, ProductDetail, NutritionInfo

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ProductDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductDetail
#         fields = ('title', 'created_at')

# class NutritionInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NutritionInfo
#         fields = ('calories', 'fat', 'protein', 'carbs', 'created_at', 'updated_at')

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#     category_id = serializers.PrimaryKeyRelatedField(
#         source='category', queryset=Category.objects.all(), write_only=True
#     )

#     class Meta:
#         model = Product
#         fields = (
#             'id', 'category', 'category_id', 'images', 'name', 'slug', 'description',
#             'price', 'unit', 'stock', 'is_available', 'rating', 'reviews_count',
#             'created_at', 'updated_at', 'nutrition', 'details'
#         )

#     def create(self, validated_data):
#         category = validated_data.pop('category', None)
#         product = Product.objects.create(category=category, **validated_data)
#         return product

#     def update(self, instance, validated_data):
#         category = validated_data.pop('category', None)
#         if category:
#             instance.category = category
#         return super().update(instance, validated_data)