# Generated by Django 4.2.5 on 2023-10-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0004_client_title1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='title1',
            field=models.CharField(default='', max_length=40),
        ),
    ]
