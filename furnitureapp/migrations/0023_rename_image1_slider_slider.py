# Generated by Django 4.2.6 on 2023-10-18 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0022_project_project_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='image1',
            new_name='slider',
        ),
    ]
