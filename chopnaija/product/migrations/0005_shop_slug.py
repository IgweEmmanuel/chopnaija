# Generated by Django 5.1.2 on 2024-10-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_rename_quanty_type_product_quantity_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
