# from django.db import models
# from django.utils.text import slugify
# from chopnaija import settings
# # from mptt.models import MPTTModel,TreeForeignKey

# class Product(models.Model):
#     """
#     Product
#     """
#     CATEGORY = (("Vegetables", "VEGETABLES"), ("Fruits", "FRUITS"), ("Meat", "MEAT"))
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, blank=True, null=True)
#     category = models.CharField(max_length=255, choices=CATEGORY, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
    
#     def __str__(self):
#         """
#         String representation of the product
#         """
#         return self.name
    
#     def save(self, *args, **kwargs):
#         """
#         Save the product
#         """
#         if not self.slug:
#             self.slug = slugify(self.name)
#             unique_slug = self.slug
#             counter = 1
#             while Product.objects.filter(slug=unique_slug).exists():
#                 unique_slug = f"{self.slug}-{counter}"
#                 counter += 1
#             self.slug = unique_slug
#         super().save(*args, **kwargs)


# # products/models.py
# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name

# # class ProductImage(models.Model):
# #     image = models.ImageField(upload_to='images/')
# #     is_primary = models.BooleanField(default=False)
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"Image for {self.product.name}"

# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     images = models.ImageField(upload_to='images/', null=True, blank=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     slug = models.SlugField(unique=True, default='', null=True, blank=True)
#     description = models.TextField(max_length=1000, blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     unit = models.CharField(max_length=50, default='each', null=True, blank=True)  # each, kg, lb, etc.
#     stock = models.PositiveIntegerField(default=0, null=True, blank=True)
#     is_available = models.BooleanField(default=True, null=True, blank=True)
    
#     rating = models.DecimalField(
#         max_digits=3, 
#         decimal_places=2,
#         validators=[MinValueValidator(0), MaxValueValidator(5)],
#         default=0, null=True, blank=True
#     )
#     reviews_count = models.PositiveIntegerField(default=0, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class ProductDetail(models.Model):
#     product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)  # e.g., "100% Organic", "Locally Sourced"
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title} - {self.product.name}"

# class NutritionInfo(models.Model):
#     product = models.OneToOneField(Product, related_name='nutrition', on_delete=models.CASCADE)
#     calories = models.CharField(max_length=50)
#     fat = models.CharField(max_length=50)
#     protein = models.CharField(max_length=50)
#     carbs = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Nutrition info for {self.product.name}"





from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, default='', null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, default='each', null=True, blank=True)  # each, kg, lb, etc.
    stock = models.PositiveIntegerField(default=0, null=True, blank=True)
    is_available = models.BooleanField(default=True, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0, null=True, blank=True
    )
    reviews_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # e.g., "100% Organic", "Locally Sourced"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.product.name}"

class NutritionInfo(models.Model):
    product = models.OneToOneField(Product, related_name='nutrition', on_delete=models.CASCADE)
    calories = models.CharField(max_length=50)
    fat = models.CharField(max_length=50)
    protein = models.CharField(max_length=50)
    carbs = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nutrition info for {self.product.name}"