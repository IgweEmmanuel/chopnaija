# Generated by Django 5.1.2 on 2024-10-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Vegetables", "VEGETABLES"),
                            ("Fruits", "FRUITS"),
                            ("Meat", "MEAT"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]