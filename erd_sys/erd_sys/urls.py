"""erd_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from erd_sys.Music_Instrument.models import Instrument
from django import urls
from django.contrib import admin
from django.urls import path , include
from Music_Instrument.urls import router
from rest_framework import routers

from Brand.urls import router as Brand_router
from Music_Instrument.urls import router as Instrument_router
from Music_Instrument.urls import router1 as InstrumentType_router
# from Music_Instrument.urls import 

router = routers.DefaultRouter()
router.registry.extend(Brand_router.registry)
router.registry.extend(Instrument_router.registry)
router.registry.extend(InstrumentType_router.registry)


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