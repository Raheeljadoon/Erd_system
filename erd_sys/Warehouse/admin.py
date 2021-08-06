from django.contrib import admin
from .models import Warehouse

@admin.register(Warehouse)
class adminWarehouse(admin.ModelAdmin):
    list_display1 = Warehouse.objects.all()

