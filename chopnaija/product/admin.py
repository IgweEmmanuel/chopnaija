from django.contrib import admin
from .models import Shop, Product, Category, QuantityVariant, ColorVariant, SizeVariant

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)