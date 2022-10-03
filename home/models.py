from django.db import models

# Create your models here.
class EmployeeData(models.Model):
   name=models.CharField(max_length=100)
   Salary=models.CharField(max_length=100)
   department=models.CharField(max_length=100)