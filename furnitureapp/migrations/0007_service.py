# Generated by Django 4.2.5 on 2023-10-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0006_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servie_name', models.CharField(max_length=50)),
            ],
        ),
    ]
