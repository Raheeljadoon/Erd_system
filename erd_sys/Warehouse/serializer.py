from django.db import models
from .models import Warehouse
from rest_framework import serializers


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'