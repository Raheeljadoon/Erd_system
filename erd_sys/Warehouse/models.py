from django.db import models

class Warehouse(models.Model):

    Warehouse_code = models.IntegerField(default = 0)
    Warehouse_phone = models.CharField(max_length=255 ,blank=True, default='')
    Warehouse_address = models.CharField(max_length=255 ,blank=True, default='')
    Warehouse_maps = models.CharField(max_length=255 ,blank=True, default='')
    Warehouse_email = models.CharField( max_length=255,blank = True , default='')



class Warehouse_instrument(models.Model):

    Warehouse_instrumentCode = models.IntegerField(default = 0)
    musical_instrumentId = models.IntegerField(default = 0)
    Stock = models.IntegerField(default = 0)
    cost = models.BigAutoField(default=0)