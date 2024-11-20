from django.db import models

class Creation(models.Model):

    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=False, blank=False)
# Create your models here.