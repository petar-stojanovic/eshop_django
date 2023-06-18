# Generated by Django 4.2.1 on 2023-06-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_App', '0005_desktop_image_laptop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='laptop',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
