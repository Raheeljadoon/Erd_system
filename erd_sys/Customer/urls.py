from django.urls import path , include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'customer',Cutomer_views)



router1 = routers.DefaultRouter()

router1.register(r'customerinstrumentinvoice',Customer_instrument_invoice_views)


router2 = routers.DefaultRouter()

router2.register(r'customermediainvoice',Customer_media_invoice_views)



router3 = routers.DefaultRouter()

router3.register(r'bank',Bank_views)
