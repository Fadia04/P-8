# Generated by Django 4.0.4 on 2022-04-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(max_length=50),
        ),
    ]
