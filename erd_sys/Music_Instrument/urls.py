from django import urls
from django.urls import path , include
from .views import *
from rest_framework import routers




router = routers.DefaultRouter()
router.register(r'instrument', Instrumentviewsets)


router1 = routers.DefaultRouter()
router1.register(r'instrumenttype', Instrument_type_viewsets)

# urlpatterns = [
#     path('',include(router.urls)),



#     # path('api-auth/', include('rest_framework.urls')),
# ]


# urlpatterns += router.urls