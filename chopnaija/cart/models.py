from django.db import models
from accounts.models import User
from store.models import Product
from chopnaija import settings

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.base.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.cartitem_set.all())
        return total_price
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
    
    def get_total_price(self):
        return self.quantity * self.product.price
    