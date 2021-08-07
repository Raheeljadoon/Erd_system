from .views import *
from django.urls import path , include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'store',Store_model_views)

router1 = routers.DefaultRouter()
router.register(r'storeinstrument',Store_musica_instr_views)


router2 = routers.DefaultRouter()
router.register(r'storemedia',Store_media_view)