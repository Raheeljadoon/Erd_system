from django.db.models import fields
from rest_framework import serializers
from .models import *


class Cutomer_serializer(serializers.ModelSerializer):
    class Meta:

        model = Customer_model

        fields = '__all__' 


   
class Customer_instrument_invoice_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Customer_Instrument_invoice
        fields = '__all__'



class Customer_media_invoice_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Customer_media_invoice
        fields = '__all__'


class Bank_serializer(serializers.ModelSerializer):

    class Meta:

        model = Bank
        fields = '__all__'