# Generated by Django 4.2.5 on 2023-10-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(upload_to='upload/image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/roducts/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to='upload/project/'),
        ),
    ]
