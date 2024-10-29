# from django.contrib import admin
# from .models import Product

# admin.site.register(Product)


# products/admin.py
from django.contrib import admin
from .models import Category, Product, ProductDetail, NutritionInfo


class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 1

class NutritionInfoInline(admin.StackedInline):
    model = NutritionInfo

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_available', 'rating']
    list_filter = ['is_available', 'category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductDetailInline, NutritionInfoInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}