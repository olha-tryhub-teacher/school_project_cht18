from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    StudentName = models.CharField(max_length=15, unique=True)
    Class = models.CharField(max_length=10)
    def __str__(self):
        return self.User
