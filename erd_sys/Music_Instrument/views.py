from django.db import models
from django.shortcuts import render

from .models import Instrument, Instrument_type
from .serializers import InstrumentSerializer, Instrument_typeSerializer
from rest_framework import viewsets


class Instrumentviewsets(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer




class Instrument_type_viewsets(viewsets.ModelViewSet):

    queryset = Instrument_type.objects.all()
    serializer_class = Instrument_typeSerializer




