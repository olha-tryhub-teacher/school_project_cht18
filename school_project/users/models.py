from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=15, unique=True)
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return self.student_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile_pics")
    role = models.CharField(max_length=10)
    class_name = models.CharField(max_length=10)
    age = models.DateField()
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=15, unique=True)
    subject = models.CharField(max_length=10)
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return self.teacher_name
