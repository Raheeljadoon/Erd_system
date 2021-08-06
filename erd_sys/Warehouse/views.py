
from django.shortcuts import render
from rest_framework import viewsets
from . serializer import WarehouseSerializer
from .models import Warehouse


class Warehouseview(viewsets.ModelViewSet):

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer