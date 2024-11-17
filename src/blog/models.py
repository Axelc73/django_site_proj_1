from django.db import models

class Creation(models.Model):

    nom = models.CharField(max_length=255)
    description = models.TextField()
# Create your models here.