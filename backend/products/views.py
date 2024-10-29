# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Product
# from .serializers import ProductSerializer

# @api_view(['GET'])
# def products(request):
#     """
#     Get all products
#     """
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# products/views.py
# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from .models import Product, Category
# from .serializers import ProductSerializer, CategorySerializer

# class ProductViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         category = self.request.query_params.get('category', None)
#         if category:
#             queryset = queryset.filter(category__slug=category)
#         return queryset.prefetch_related('images', 'details').select_related('category', 'nutrition')

#     @action(detail=False, methods=['get'])
#     def featured(self, request):
#         """Get featured products (you can customize this based on your needs)"""
#         products = self.get_queryset().filter(is_available=True)[:5]
#         serializer = self.get_serializer(products, many=True)
#         return Response(serializer.data)

# class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'










# from rest_framework import viewsets, status, permissions
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from django.shortcuts import get_object_or_404
# from django.db import transaction
# from .models import Product, Category, ProductImage, ProductDetail, NutritionInfo
# from .serializers import (
#     ProductSerializer, CategorySerializer, ProductImageSerializer,
#     ProductDetailSerializer, NutritionInfoSerializer
# )

# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]
#     parser_classes = (MultiPartParser, FormParser)

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         category = self.request.query_params.get('category', None)
#         if category:
#             queryset = queryset.filter(category__slug=category)
        
#         # Optimize queries with select_related and prefetch_related
#         return queryset.prefetch_related(
#             'images',
#             'details'
#         ).select_related(
#             'category',
#             'nutrition'
#         )

#     @transaction.atomic
#     def create(self, request, *args, **kwargs):
#         """Create a product with all related data"""
#         # Extract related data
#         images_data = request.FILES.getlist('images', [])
#         details_data = request.data.get('details', [])
#         nutrition_data = request.data.get('nutrition', {})
#         category_slug = request.data.get('category')

#         # Validate category
#         try:
#             category = Category.objects.get(slug=category_slug)
#         except Category.DoesNotExist:
#             return Response(
#                 {'error': 'Category not found'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         # Create product
#         product_data = request.data.copy()
#         product_data['category'] = category.id
#         serializer = self.get_serializer(data=product_data)
#         serializer.is_valid(raise_exception=True)
#         product = serializer.save()

#         # Create product images
#         for index, image_data in enumerate(images_data):
#             ProductImage.objects.create(
#                 product=product,
#                 image=image_data,
#                 is_primary=(index == 0)
#             )

#         # Create product details
#         for detail in details_data:
#             ProductDetail.objects.create(
#                 product=product,
#                 title=detail.get('title', '')
#             )

#         # Create nutrition info
#         if nutrition_data:
#             NutritionInfo.objects.create(
#                 product=product,
#                 calories=nutrition_data.get('calories', ''),
#                 fat=nutrition_data.get('fat', ''),
#                 protein=nutrition_data.get('protein', ''),
#                 carbs=nutrition_data.get('carbs', '')
#             )

#         # Refresh product data with all related objects
#         product = self.get_queryset().get(id=product.id)
#         return Response(
#             self.get_serializer(product).data,
#             status=status.HTTP_201_CREATED
#         )

#     @transaction.atomic
#     def update(self, request, *args, **kwargs):
#         """Update product and related data"""
#         instance = self.get_object()
#         partial = kwargs.pop('partial', False)

#         # Handle category update
#         category_slug = request.data.get('category')
#         if category_slug:
#             try:
#                 category = Category.objects.get(slug=category_slug)
#                 request.data['category'] = category.id
#             except Category.DoesNotExist:
#                 return Response(
#                     {'error': 'Category not found'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#         # Update basic product data
#         serializer = self.get_serializer(
#             instance, 
#             data=request.data, 
#             partial=partial
#         )
#         serializer.is_valid(raise_exception=True)
#         product = serializer.save()

#         # Handle image updates
#         if 'images' in request.FILES:
#             if request.data.get('replace_images', False):
#                 instance.images.all().delete()
            
#             images_data = request.FILES.getlist('images')
#             for index, image_data in enumerate(images_data):
#                 ProductImage.objects.create(
#                     product=instance,
#                     image=image_data,
#                     is_primary=(index == 0 and instance.images.count() == 0)
#                 )

#         # Update product details
#         if 'details' in request.data:
#             instance.details.all().delete()
#             for detail in request.data.get('details', []):
#                 ProductDetail.objects.create(
#                     product=instance,
#                     title=detail.get('title', '')
#                 )

#         # Update nutrition info
#         nutrition_data = request.data.get('nutrition')
#         if nutrition_data:
#             NutritionInfo.objects.update_or_create(
#                 product=instance,
#                 defaults={
#                     'calories': nutrition_data.get('calories', ''),
#                     'fat': nutrition_data.get('fat', ''),
#                     'protein': nutrition_data.get('protein', ''),
#                     'carbs': nutrition_data.get('carbs', '')
#                 }
#             )

#         # Refresh product data with all related objects
#         product = self.get_queryset().get(id=product.id)
#         return Response(self.get_serializer(product).data)

#     def destroy(self, request, *args, **kwargs):
#         """Delete product and all related data"""
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(detail=True, methods=['post'])
#     def set_primary_image(self, request, slug=None):
#         """Set primary image for product"""
#         product = self.get_object()
#         image_id = request.data.get('image_id')
        
#         if not image_id:
#             return Response(
#                 {'error': 'Image ID is required'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             with transaction.atomic():
#                 product.images.all().update(is_primary=False)
#                 image = product.images.get(id=image_id)
#                 image.is_primary = True
#                 image.save()
#             return Response({'message': 'Primary image updated successfully'})
#         except ProductImage.DoesNotExist:
#             return Response(
#                 {'error': 'Image not found'},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#     @action(detail=False, methods=['get'])
#     def featured(self, request):
#         """Get featured products"""
#         products = self.get_queryset().filter(is_available=True)[:5]
#         serializer = self.get_serializer(products, many=True)
#         return Response(serializer.data)

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]

#     def get_queryset(self):
#         return Category.objects.prefetch_related('products')





# from rest_framework import viewsets, status, permissions
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from django.shortcuts import get_object_or_404
# from django.db import transaction
# from .models import Product, Category, ProductDetail, NutritionInfo
# from .serializers import (
#     ProductSerializer, CategorySerializer, ProductDetailSerializer, NutritionInfoSerializer
# )


# from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
# from drf_spectacular.types import OpenApiTypes


# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff
    
# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet for managing products and their related data.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]
#     parser_classes = (MultiPartParser, FormParser)

#     @extend_schema(
#         summary="List all products",
#         parameters=[
#             OpenApiParameter(
#                 name="category",
#                 type=str,
#                 description="Filter products by category slug",
#                 required=False
#             ),
#         ],
#         responses={200: ProductSerializer(many=True)}
#     )
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     @extend_schema(
#         summary="Create a new product",
#         request={
#             'multipart/form-data': {
#                 'type': 'object',
#                 'properties': {
#                     'name': {'type': 'string'},
#                     'slug': {'type': 'string'},
#                     'category': {'type': 'integer'},
#                     'description': {'type': 'string'},
#                     'price': {'type': 'number'},
#                     'unit': {'type': 'string'},
#                     'stock': {'type': 'integer'},
#                     'is_available': {'type': 'boolean'},
#                     'rating': {'type': 'number'},
#                     'images': {
#                         'type': 'array',
#                         'items': {'type': 'string', 'format': 'binary'}
#                     },
#                     'details': {
#                         'type': 'array',
#                         'items': {
#                             'type': 'object',
#                             'properties': {
#                                 'title': {'type': 'string'}
#                             }
#                         }
#                     },
#                     'nutrition': {
#                         'type': 'object',
#                         'properties': {
#                             'calories': {'type': 'string'},
#                             'fat': {'type': 'string'},
#                             'protein': {'type': 'string'},
#                             'carbs': {'type': 'string'}
#                         }
#                     }
#                 }
#             }
#         },
#         examples=[
#             OpenApiExample(
#                 'Valid Product Creation',
#                 value={
#                     'name': 'Organic Apples',
#                     'slug': 'organic-apples',
#                     'category': 'fruits',
#                     'description': 'Fresh organic apples',
#                     'price': '4.99',
#                     'unit': 'kg',
#                     'stock': 100,
#                     'is_available': True,
#                     'details': [
#                         {'title': '100% Organic'},
#                         {'title': 'Locally Sourced'}
#                     ],
#                     'nutrition': {
#                         'calories': '52',
#                         'fat': '0.2g',
#                         'protein': '0.3g',
#                         'carbs': '14g'
#                     }
#                 }
#             )
#         ]
#     )
#     def create(self, request, *args, **kwargs):
#         print(request.data)
#         return super().create(request, *args, **kwargs)

#     @extend_schema(
#         summary="Set primary image for product",
#         request={
#             'application/json': {
#                 'type': 'object',
#                 'properties': {
#                     'image_id': {'type': 'integer'}
#                 },
#                 'required': ['image_id']
#             }
#         },
#         responses={
#             200: {'type': 'object', 'properties': {'message': {'type': 'string'}}},
#             400: {'type': 'object', 'properties': {'error': {'type': 'string'}}},
#             404: {'type': 'object', 'properties': {'error': {'type': 'string'}}}
#         }
#     )
#     @action(detail=True, methods=['post'])
#     def set_primary_image(self, request, slug=None):
#         """Set the primary image for a product"""
#         return super().set_primary_image(request, slug)

#     @extend_schema(
#         summary="Get featured products",
#         responses={200: ProductSerializer(many=True)}
#     )
#     @action(detail=False, methods=['get'])
#     def featured(self, request):
#         """Get a list of featured products"""
#         return super().featured(request)

# class CategoryViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet for managing product categories.
#     """
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]

#     @extend_schema(
#         summary="List all categories",
#         responses={200: CategorySerializer(many=True)}
#     )
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     @extend_schema(
#         summary="Create a new category",
#         request=CategorySerializer,
#         responses={201: CategorySerializer}
#     )
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)







from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from django.db import transaction
from .models import Product, Category, ProductDetail, NutritionInfo
from .serializers import (
    ProductSerializer, CategorySerializer, ProductDetailSerializer,
    NutritionInfoSerializer
)

# class IsAdminOrReadOnly:
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return request.user and request.user.is_staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAdminOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(summary='List all products')
    def list(self, request, *args, **kwargs):
        """List products with optional category filter"""
        queryset = self.filter_queryset(self.get_queryset())
        category_slug = request.query_params.get('category', None)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(summary='Create products')
    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @extend_schema(summary='Access products by slug')
    @action(detail=True, methods=['post'])
    def set_primary_image(self, request, slug=None):
        product = self.get_object()
        image_id = request.data.get('image_id')
        if image_id:
            try:
                product.images = image_id
                product.save()
                return Response({'message': 'Primary image set successfully'})
            except:
                return Response({'error': 'Error setting primary image'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Image ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        queryset = self.get_queryset().filter(is_available=True).order_by('-reviews_count')[:10]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    # permission_classes = [IsAdminOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)