# Generated by Django 3.2.6 on 2021-08-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0007_remove_brands_brandid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='BrandDescription',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandWebsite',
            field=models.CharField(max_length=255),
        ),
    ]