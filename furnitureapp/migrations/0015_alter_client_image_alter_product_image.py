# Generated by Django 4.2.5 on 2023-10-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0014_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(upload_to='upload/client/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/products/'),
        ),
    ]
