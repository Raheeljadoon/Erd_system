# Generated by Django 3.2.6 on 2021-08-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0005_brands_brandid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='BrandId',
            field=models.IntegerField(),
        ),
    ]
