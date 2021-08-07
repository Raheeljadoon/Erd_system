from django.shortcuts import render

from .models import Media_model
from .serializers import Media_Serializer
from rest_framework import viewsets

class Media_views(viewsets.ModelViewSet):

    queryset = Media_model.objects.all()

    serializer_class = Media_Serializer