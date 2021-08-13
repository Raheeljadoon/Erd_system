# from django.db import transaction
from rest_framework import serializers
from .models import *
# from  import RegisterSerializer

# # from user.models import GENDER_SELECTION


# class CustomRegisterSerializer(RegisterSerializer):
#     gender = serializers.ChoiceField(choices=GENDER_SELECTION)
#     phone_number = serializers.CharField(max_length=30)

#     # Define transaction.atomic to rollback the save operation in case of error
#     @transaction.atomic
#     def save(self, request):
#         user = super().save(request)
#         user.gender = self.data.get('gender')
#         user.phone_number = self.data.get('phone_number')
#         user.save()
#         return user

class User_serializer(serializers.ModelSerializer):
    class Meta :
        model = User_signup
        fields = '__all__'

class User_loginSerializers(serializers.ModelSerializer):

    class Meta :
        model = User_login
        fields = '__all__'
