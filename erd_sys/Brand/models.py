from django.db import models

class Brands(models.Model) :
    # BrandId = models.IntegerField()
    BrandName =  models.CharField(max_length=100 )
    BrandDescription = models.CharField(max_length=255 )
    BrandWebsite = models.CharField(max_length=255)




