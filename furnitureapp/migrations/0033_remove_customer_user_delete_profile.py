# Generated by Django 4.2.5 on 2023-10-31 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0032_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]