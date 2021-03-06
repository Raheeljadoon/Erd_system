from django.db import models
from django.db.models import fields
from .models import Warehouse,   Warehouse_Media , Warehouse_instrument
from rest_framework import serializers


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'



class Warehouse_Instrument_serializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse_instrument
        fields = '__all__'



class Warehouse_media_Serializer(serializers.ModelSerializer):

    class Meta :
        model = Warehouse_Media
        fields = '__all__'