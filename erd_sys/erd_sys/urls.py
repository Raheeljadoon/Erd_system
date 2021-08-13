


from django import urls
from django.contrib import admin
from django.urls import path , include
from Music_Instrument.urls import router
from rest_framework import routers

from Brand.urls import router as Brand_router
from Music_Instrument.urls import router as Instrument_router
from Music_Instrument.urls import router1 as InstrumentType_router
from Warehouse.urls import router as Warehouse_router
from Warehouse.urls import router1 as Warehouse_instrument_router
from Warehouse.urls import router2 as Warehouse_media_router
from Media.urls import router as Media_router
from Media.urls import router1 as media_type_router
from Store.urls import router as store_router
from Store.urls import router1 as storemusicinst_router
from Store.urls import router2 as store_media_router
from Customer.urls import router as customer_router
from Customer.urls import router1 as customer_instin_router
from Customer.urls import router2 as customer_media_invoice_router
from Customer.urls import router3 as bank_router
from user.urls import router as user_router
from user.urls import router1 as login_router









router = routers.DefaultRouter()
router.registry.extend(Brand_router.registry)

router.registry.extend(Instrument_router.registry)
router.registry.extend(InstrumentType_router.registry)

router.registry.extend(Warehouse_router.registry)
router.registry.extend(Warehouse_instrument_router.registry)
router.registry.extend(Warehouse_media_router.registry)

router.registry.extend(Media_router.registry)
router.registry.extend(media_type_router.registry)

router.registry.extend(store_router.registry)
router.registry.extend(storemusicinst_router.registry)
router.registry.extend(store_media_router.registry)


router.registry.extend(customer_router.registry)
router.registry.extend(customer_instin_router.registry)
router.registry.extend(customer_media_invoice_router.registry)
router.registry.extend(bank_router.registry)

router.registry.extend(user_router.registry)
router.registry.extend(login_router.registry)




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