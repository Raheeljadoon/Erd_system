from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from .models import Instrument, Instrument_type

class InstrumentSerializer(serializers.ModelSerializer):

    class Meta :
        model = Instrument
        fields = '__all__' 
        



class Instrument_typeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument_type
        fields = '__all__'
       

