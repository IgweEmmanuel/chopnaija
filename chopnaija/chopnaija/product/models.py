from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel,TreeForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.variant_name
class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name
    

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.size_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    is_digital = models.BooleanField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    stock = models.IntegerField(default=100)
    quanty_type = models.ForeignKey(QuantityVariant, on_delete=models.PROTECT, null=True, blank=True)
    color_type = models.ForeignKey(ColorVariant, on_delete=models.PROTECT, null=True, blank=True)
    size_type = models.ForeignKey(SizeVariant, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
