from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from Store.models import Store_musical_instrument , Store_model
from Media.models import Media_model



class Customer_model(models.Model):
    # id = models.IntegerField(ForeignKey)
    Name = models.CharField(max_length=255 )
    Address = models.CharField(max_length=255)
    TelephoneNO = models.CharField(max_length=255)
    DateOfBirth = models.DateField()

    def __str__(self) -> str:
        return "id "+ str(self.id ) +  self.Name 


    # def __init__(self) :
    #     return id




class Customer_Instrument_invoice(models.Model):

    customerID = models.ForeignKey(Customer_model,on_delete=CASCADE)
    musical_instrumentId = models.ForeignKey(Store_musical_instrument,on_delete=CASCADE)
    date = models.DateTimeField()
    storeId = models.ForeignKey(Store_model,on_delete=CASCADE)

    



class Customer_media_invoice(models.Model):

    customerID = models.ForeignKey(Customer_model, on_delete=CASCADE)
    mediaID = models.ForeignKey(Media_model,on_delete=CASCADE)
    date = models.DateTimeField()
    storeID = models.ForeignKey(Store_model,on_delete=CASCADE)



class Bank(models.Model):
    bankID = models.IntegerField()
    customerID = models.ForeignKey(Customer_model,on_delete=CASCADE)
    bank_Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Sortcode = models.IntegerField()
    AccountNO = models.IntegerField()







