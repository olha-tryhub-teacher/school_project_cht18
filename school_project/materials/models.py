from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Material(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to="materials/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    material_type = models.CharField(
        max_length=20,
        choices=[
            ("file", "Файл"),
            ("link", "Посилання"),
            ("video", "Відео"),
        ]
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    



