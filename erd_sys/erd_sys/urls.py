

from django import urls
from django.contrib import admin
from django.urls import path , include
from Music_Instrument.urls import router
from rest_framework import routers

from Brand.urls import router as Brand_router
from Music_Instrument.urls import router as Instrument_router
from Music_Instrument.urls import router1 as InstrumentType_router
from Warehouse.urls import router as Warehouse_router


router = routers.DefaultRouter()
router.registry.extend(Brand_router.registry)
router.registry.extend(Instrument_router.registry)
router.registry.extend(InstrumentType_router.registry)
router.registry.extend(Warehouse_router.registry)


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include(router.urls)),
]


















# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', include('Brand.urls')),
#     # path('',include('Music_Instrument.urls')),
# ]

# urlpatterns += router.urls