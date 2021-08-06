from django.http.response import HttpResponseBase
from django.shortcuts import render
# from django.views import generic
from django.http import HttpResponse
from rest_framework.serializers import Serializer
from .serializers import BrandSerializer
from rest_framework.renderers import JSONRenderer
from .models import Brands
from rest_framework import viewsets



class Brandviewset(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer











# def Brand_list(request ):

#     brand = Brands.objects.all()
#     serializer = BrandSerializer(brand , many = True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse (json_data , content_type = 'application/json')   
    

# def Brand_viewsDetail(request ,pk):

#     brand = Brands.objects.get(id = pk)
#     serializer = BrandSerializer(brand)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse (json_data , content_type = 'application/json')   
    



