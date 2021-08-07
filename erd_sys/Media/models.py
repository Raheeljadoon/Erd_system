from django.db import models

# Create your models here.
class Media_model(models.Model):

    Media_type = models.IntegerField(default=False)
    Media_name = models.CharField(max_length=255)
    Media_description = models.CharField(max_length=255)



class Media_type(models.Model):

    Media_name = models.CharField(max_length=255)

    

