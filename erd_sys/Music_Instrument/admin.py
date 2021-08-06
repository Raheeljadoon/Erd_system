from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Instrument , Instrument_type

@admin.register(Instrument)

class adminInstrument(admin.ModelAdmin):
    list_display1 = ('Instruments_typeID','Instruments_Name','Instruments_Description')


@admin.register(Instrument_type)
class adminInstrument(admin.ModelAdmin):
    list_display1 = ('Instruments_BrandID','Instruments_Name','Instruments_Description')
