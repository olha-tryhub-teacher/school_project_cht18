from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=10, verbose_name="Імя")
    description = models.TextField(verbose_name="Опис")



class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Учень", related_name="student_grades")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет", related_name="subject_grades")
    grade = models.CharField(max_length=20, verbose_name="Оцінка")
    date = models.DateTimeField(null=True, blank=True, verbose_name="Дата")
    comment = models.TextField(blank=True, null=True, verbose_name="Коментар")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ким написаний коментар", related_name="created_comments")