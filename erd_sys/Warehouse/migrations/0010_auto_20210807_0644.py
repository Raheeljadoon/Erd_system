# Generated by Django 3.2.6 on 2021-08-07 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Warehouse', '0009_delete_warehouse_instrument'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse_media',
            name='warehouse_code',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Warehouse.warehouse'),
        ),
        migrations.CreateModel(
            name='Warehouse_instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musical_instrumentid', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('Cost', models.FloatField(default=0)),
                ('Warehouse_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Warehouse.warehouse')),
            ],
        ),
    ]
