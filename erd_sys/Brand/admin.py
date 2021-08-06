from django.contrib import admin

from .models import Brands

@admin.register(Brands)

class adminBrand(admin.ModelAdmin):
    list_display = ('id','BrandName','BrandDescription','BrandWebsite')

