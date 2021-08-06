from django.db import models

class Brands(models.Model) :
    # BrandId = models.IntegerField()
    BrandName =  models.CharField(max_length=100,blank=True, default='')
    BrandDescription = models.CharField(max_length=255 ,blank=True, default='')
    BrandWebsite = models.CharField(max_length=255, blank=True,default='')




