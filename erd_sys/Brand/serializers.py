from rest_framework import serializers
from .models import Brands


# class BrandSerializer(serializers.Serializer):

#     # BrandId = serializers.IntegerField()
#     BrandName =  serializers.CharField(max_length=100, default='')
#     BrandDescription = serializers.CharField(max_length=255 , default='')
#     BrandWebsite = serializers.CharField(max_length=255, default='')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'