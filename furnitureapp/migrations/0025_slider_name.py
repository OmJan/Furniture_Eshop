# Generated by Django 4.2.6 on 2023-10-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0024_rename_slider_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
