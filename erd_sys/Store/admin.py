from django.contrib import admin
from .models import *


@admin.register(Store_model)

class adminBrand(admin.ModelAdmin):
    list_display3 = Store_model.objects.all()


@admin.register(Store_musical_instrument)

class adminBrand(admin.ModelAdmin):
    list_display3 = Store_musical_instrument.objects.all()




@admin.register(store_media)

class adminBrand(admin.ModelAdmin):
    list_display3 = store_media.objects.all()

