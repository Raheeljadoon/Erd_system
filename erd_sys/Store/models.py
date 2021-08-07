from django.db import models
from django.db.models.fields import FloatField

class Store_model(models.Model):

    store_phone = models.CharField(max_length=255)

    store_email = models.CharField(max_length=255)

    store_map = models.CharField(max_length=255)

    store_address = models.CharField(max_length=255)



class Store_musical_instrument(models.Model):

    storeID = models.IntegerField()

    musical_instrumentId = models.IntegerField()

    stock = models.IntegerField()

    cost = models.FloatField()



class store_media(models.Model):

    storeID = models.IntegerField()

    mediaID = models.IntegerField()

    stock = models.IntegerField()

    cost = FloatField()