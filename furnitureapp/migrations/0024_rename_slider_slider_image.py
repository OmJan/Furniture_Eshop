# Generated by Django 4.2.6 on 2023-10-18 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0023_rename_image1_slider_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='slider',
            new_name='image',
        ),
    ]