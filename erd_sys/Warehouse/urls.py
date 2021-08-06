from django.urls import path , include
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register (r'warehouse',Warehouseview)

router1 = routers.DefaultRouter()
router1.register(r'warehouseinstrument',Warehouse_instrument_views)




