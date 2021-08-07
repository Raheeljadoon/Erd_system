
from django.contrib import admin
from .models import Media_model, Media_type


@admin.register(Media_model)

class adminBrand(admin.ModelAdmin):
    list_display2 = Media_model.objects.all()


@admin.register(Media_type)

class adminBrand(admin.ModelAdmin):
    list_display2 = Media_type.objects.all()





