# Generated by Django 5.1.2 on 2024-10-19 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_productimage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="quanty_type",
            new_name="quantity_type",
        ),
    ]