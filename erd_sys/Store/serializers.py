from rest_framework import serializers
from .models import Store_model,Store_musical_instrument, store_media


class Store_model_serializer(serializers.ModelSerializer):

    class Meta :
         model = Store_model

         fields = '__all__'


class Store_musical_instr_serializer(serializers.ModelSerializer):


       class Meta :
         model = Store_musical_instrument

         fields = '__all__'


class Store_media_serializer(serializers.ModelSerializer):

       class Meta :
         model = store_media

         fields = '__all__'


