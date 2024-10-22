from django.db import models
from django.utils.text import slugify
from chopnaija import settings
# from mptt.models import MPTTModel,TreeForeignKey

class Product(models.Model):
    CATEGORY = (("Vegetables", "VEGETABLES"), ("Fruits", "FRUITS"), ("Meat", "MEAT"))
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.CharField(max_length=255, choices=CATEGORY, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
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
