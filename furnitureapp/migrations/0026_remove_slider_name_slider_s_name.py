# Generated by Django 4.2.6 on 2023-10-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0025_slider_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='name',
        ),
        migrations.AddField(
            model_name='slider',
            name='s_name',
            field=models.CharField(default='slider', max_length=50),
        ),
    ]