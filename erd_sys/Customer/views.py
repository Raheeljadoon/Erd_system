# from erd_sys.Customer.serializers import Cutomer_serializer
from django.shortcuts import render
from .serializers import *

from .models import *
from .models import *
from rest_framework import viewsets



class Cutomer_views(viewsets.ModelViewSet):

    queryset = Customer_model.objects.all()

    serializer_class = Cutomer_serializer


class Customer_instrument_invoice_views(viewsets.ModelViewSet):

    queryset = Customer_Instrument_invoice.objects.all()

    serializer_class = Customer_instrument_invoice_Serializer


class Customer_media_invoice_views(viewsets.ModelViewSet):

    queryset = Customer_media_invoice.objects.all()

    serializer_class = Customer_media_invoice_Serializer


class Bank_views(viewsets.ModelViewSet):

    queryset = Bank.objects.all()

    serializer_class = Bank_serializer



