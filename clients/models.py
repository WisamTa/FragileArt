from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=128)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    business_type = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class StudentData(models.Model):
   name=models.CharField(max_length=100)
   standard=models.CharField(max_length=100)
   section=models.CharField(max_length=100)
