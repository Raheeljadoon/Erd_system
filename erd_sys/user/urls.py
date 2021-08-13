# from erd_sys.user.views import User_views
from django.urls import path , include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'signup', User_views)

router1 = routers.DefaultRouter()
router1.register(r'login', User_login_views)


