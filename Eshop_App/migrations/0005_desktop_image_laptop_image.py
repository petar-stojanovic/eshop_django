# Generated by Django 4.2.1 on 2023-06-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_App', '0004_laptop_desktop'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
