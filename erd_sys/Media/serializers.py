from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Media_model, Media_type

class Media_Serializer(serializers.ModelSerializer):

    class Meta :

        model = Media_model
        fields = '__all__'



class Media_type_Serializer(serializers.ModelSerializer):

    class Meta :
        model = Media_type

        fields = '__all__'
        