from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 50)
    idi = models.IntegerField()
    ispresent = models.BooleanField()

