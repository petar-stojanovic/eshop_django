# Generated by Django 4.2.1 on 2023-06-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
