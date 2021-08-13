from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import viewsets


class User_views(viewsets.ModelViewSet):

    queryset = User_signup.objects.all()
    serializer_class = User_serializer


class User_login_views(viewsets.ModelViewSet):

    queryset = User_login.objects.all()
    serializer_class =  User_loginSerializers