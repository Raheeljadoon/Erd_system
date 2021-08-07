
from django.contrib import admin
from .models import Media_model


@admin.register(Media_model)

class adminBrand(admin.ModelAdmin):
    list_display2 = Media_model.objects.all()





