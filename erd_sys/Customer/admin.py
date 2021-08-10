from django.contrib import admin
from .models import *


@admin.register(Customer_model)

class adminBrand(admin.ModelAdmin):
    list_display3 = Customer_model.objects.all()


@admin.register(Customer_Instrument_invoice)

class adminBrand(admin.ModelAdmin):
    list_display3 = Customer_Instrument_invoice.objects.all()



@admin.register(Customer_media_invoice)

class adminBrand(admin.ModelAdmin):
    list_display3 =Customer_media_invoice.objects.all()





@admin.register(Bank)

class adminBrand(admin.ModelAdmin):
    list_display3 =Bank.objects.all()