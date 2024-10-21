from django.shortcuts import render
from rest_framework import viewsets, views, permissions
from rest_framework.response import Response
from .models import Category, Shop, Product, QuantityVariant, ColorVariant, SizeVariant
from .serializers import CategorySerializer, ShopSerializer, ProductSerializer, QuantitySerializer, ColorVariantSerializer, SizeVariantSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User


class DemoView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"success": "You are authenticated"})

class CategoryView(viewsets.ViewSet):
    """Category view

    Args:
        viewsets: views for client access to database data
    """
    queryset = Category.objects.all()
    
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(responses=CategorySerializer)
    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                one_query = Category.objects.get(id=pk)
                serializer = CategorySerializer(one_query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({"error": "No category or category ID found"}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({"error": "Category ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_path='by-slug/(?P<slug>[^/.]+)')
    @extend_schema(responses=CategorySerializer)
    def slug_retrieve(self, request, slug=None):
        if slug is not None:
            try:
                slug_query = Category.objects.get(slug=slug)
                serializer = CategorySerializer(slug_query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({"error": "No category"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Cateory name cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
    

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
    
class QuantityView(viewsets.ViewSet):
    queryset = QuantityVariant.objects.all()
    
    @extend_schema(responses=QuantitySerializer)
    def list(self, request):
        serializer = QuantitySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ColorView(viewsets.ViewSet):
    queryset = ColorVariant.objects.all()
    
    @extend_schema(responses=ColorVariantSerializer)
    def list(self, request):
        serializer = ColorVariantSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class SizeView(viewsets.ViewSet):
    queryset = SizeVariant.objects.all()
    
    @extend_schema(responses=SizeVariantSerializer)
    def list(self, request):
        serializer = SizeVariantSerializer(self.queryset, many=True)
        return Response(serializer.data)

    
class ProductView(viewsets.ViewSet):
    """Product view

    Args:
        viewsets: views for client access to database data
    """
   
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        queryset = Product.objects.all()
        if queryset is not None:
        
            category = request.query_params.get('category')
            shop = request.query_params.get('shop')
            if category:
                queryset = queryset.filter(category__category_name=category)
            if shop:
                queryset = queryset.filter(shop__shop_name=shop)
            if queryset.exists():
                serializer = ProductSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
            return Response({"error": "No product found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "No product found"}, status=status.HTTP_400_BAD_REQUEST)
            
    @extend_schema(responses=ProductSerializer)
    def retrieve(self, request, pk=None):
        if pk is not None:
            try:
                product_query = Product.objects.get(id=pk)
                serializer = ProductSerializer(product_query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"error": "No product or product ID found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], url_path='by-slug/(?P<slug>[^/.]+)')
    @extend_schema(responses=ProductSerializer)
    def slug_retrieve(self, request, slug=None):
        if slug is not None:
            try:   
                slug_product = Product.objects.get(name=slug)
                serializer = ProductSerializer(slug_product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"error": "No product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Wrong product name"}, status=status.HTTP_400_BAD_REQUEST)
        
    @extend_schema(request=ProductSerializer, responses={201:ProductSerializer, 400:"Bad Request"})
    def create(self, request):
        if request:
            try:
                serializer = ProductSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": "Could not create product " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No data provided"}, status=status.HTTP_204_NO_CONTENT)