from django.db import models

class Warehouse(models.Model):

    Warehouse_code = models.IntegerField(default = 0)
    Warehouse_phone = models.CharField(max_length=255 ,blank=True, default='')
    Warehouse_address = models.CharField(max_length=255 ,blank=True, default='')
    Warehouse_maps = models.CharField(max_length=255 ,blank=True, default='')
    Warehouse_email = models.CharField( max_length=255,blank = True , default='')
