from django.urls import path
from django.urls.conf import include
from Brand import views
from rest_framework import routers
from .views import *




router = routers.DefaultRouter()
router.register(r'brand', Brandviewset)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

# urlpatterns = [
#     path('brand/', views.Brand_list ),
#     path('brand/<int:pk>', views.Brand_viewsDetail ),
    
# ]
