# Generated by Django 4.2 on 2023-05-27 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0004_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='items',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
