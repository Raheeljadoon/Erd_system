from django.db import models
from Brand.models import Brands



class Instrument(models.Model):
    Instruments_typeId = models.IntegerField(default=0)
    Instruments_Name = models.CharField(max_length=255)
    Instruments_Description = models.CharField(max_length=255 )



class Instrument_type(models.Model):


    Instruments_BrandID = models.ForeignKey(Brands, on_delete=models.CASCADE)
    Instruments_Name = models.CharField(max_length=255 )
    Instruments_Description = models.CharField(max_length=255 )






