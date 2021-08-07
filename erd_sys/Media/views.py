from django.db import models
from django.shortcuts import render

from .models import Media_model, Media_type
from .serializers import Media_Serializer, Media_type_Serializer
from rest_framework import viewsets

class Media_views(viewsets.ModelViewSet):

    queryset = Media_model.objects.all()

    serializer_class = Media_Serializer


class Media_type_views(viewsets.ModelViewSet):

    queryset = Media_type.objects.all()
    serializer_class = Media_type_Serializer