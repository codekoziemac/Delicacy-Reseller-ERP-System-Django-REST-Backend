# Generated by Django 4.2.7 on 2023-12-31 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_inventory_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='expiry_date',
        ),
        migrations.AddField(
            model_name='item',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
