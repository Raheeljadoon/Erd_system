from .models import Store_model, Store_musical_instrument, store_media
from django.shortcuts import render

from .serializers import Store_musical_instr_serializer, Store_media_serializer , Store_model_serializer
from rest_framework import serializers, viewsets

class Store_model_views(viewsets.ModelViewSet):

    queryset = Store_model.objects.all()

    serializer_class = Store_model_serializer



class Store_musica_instr_views(viewsets.ModelViewSet):

    queryset = Store_musical_instrument.objects.all()

    serializer_class = Store_musical_instr_serializer



class Store_media_view(viewsets.ModelViewSet):

        queryset = store_media.objects.all()

        serializer_class = Store_media_serializer



