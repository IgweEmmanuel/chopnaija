from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cart, CartItem
from store.models import Product
from .serializers import CartSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))
        
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=['post'])
    def remove_item(self, request, pk=None):
        """Remove an item from the cart.
        
        Args:
            request (Request): The request object.
            pk (int): The primary key of the cart.
        
        Returns:
            Response: The updated cart data.
        """
        cart = self.get_object()
        product_id = request.data.get('product')

        cart_item = get_object_or_404(CartItem, cart=cart, product__id=product_id)
        cart_item.delete()

        return Response(CartSerializer(cart).data)