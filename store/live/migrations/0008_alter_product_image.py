# Generated by Django 4.2 on 2023-05-28 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0007_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]