from django.urls import path , include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()

router.register(r'media', Media_views)




router1 = routers.DefaultRouter()
router1.register(r'mediatype', Media_type_views)