# Generated by Django 4.2.7 on 2023-12-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='inventory_code',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
