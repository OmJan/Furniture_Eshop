# Generated by Django 4.2.5 on 2023-10-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0005_alter_client_title1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(upload_to='project/')),
            ],
        ),
    ]