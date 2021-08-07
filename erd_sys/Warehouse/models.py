from django.db import models
from django.db.models.base import Model

class Warehouse(models.Model):

    Warehouse_code = models.IntegerField( default=0)
    Warehouse_phone = models.CharField(max_length=255 )
    Warehouse_address = models.CharField(max_length=255 )
    Warehouse_maps = models.CharField(max_length=255 )
    Warehouse_email = models.CharField( max_length=255)



class Warehouse_instrument(models.Model):

    Warehouse_code = models.ForeignKey(Warehouse , on_delete=models.CASCADE )
    musical_instrumentid = models.IntegerField(default=0 )
    stock = models.IntegerField(default = 0)
    Cost = models.FloatField(default=0)
    



class Warehouse_Media(models.Model):
    warehouse_code = models.ForeignKey(Warehouse, on_delete=models.CASCADE , default="")
    media_ID = models.IntegerField(default = False)
    stock = models.IntegerField(default = False)
    cost = models.FloatField(default=False)