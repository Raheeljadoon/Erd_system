
from django.shortcuts import render
from rest_framework import viewsets
from . serializer import WarehouseSerializer, Warehouse_Instrument_serializer
from .models import Warehouse, Warehouse_instrument


class Warehouseview(viewsets.ModelViewSet):

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class Warehouse_instrument_views(viewsets.ModelViewSet):

    queryset = Warehouse_instrument.objects.all()

    serializer_class = Warehouse_Instrument_serializer
