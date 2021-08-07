from django.contrib import admin
from .models import Warehouse , Warehouse_Media , Warehouse_instrument

@admin.register(Warehouse)
class adminWarehouse(admin.ModelAdmin):
    list_display1 = Warehouse.objects.all()



@admin.register(Warehouse_instrument)
class adminWarehouse(admin.ModelAdmin):
    list_display1 = Warehouse_instrument.objects.all()




@admin.register(Warehouse_Media)
class adminWarehouse(admin.ModelAdmin):
    list_display1 = Warehouse_Media.objects.all()




