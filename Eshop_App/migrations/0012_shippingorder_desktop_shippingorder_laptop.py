# Generated by Django 4.2.1 on 2023-06-28 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_App', '0011_shippingorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingorder',
            name='desktop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Eshop_App.desktoporder'),
        ),
        migrations.AddField(
            model_name='shippingorder',
            name='laptop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Eshop_App.laptoporder'),
        ),
    ]
