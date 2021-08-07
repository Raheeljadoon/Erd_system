# Generated by Django 3.2.6 on 2021-08-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Warehouse', '0003_alter_warehouse_instrument_warehouse_instrumentcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse_Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_ID', models.IntegerField(default=False)),
                ('stock', models.IntegerField(default=False)),
                ('cost', models.FloatField(default=False)),
                ('warehouse_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Warehouse.warehouse_instrument')),
            ],
        ),
    ]