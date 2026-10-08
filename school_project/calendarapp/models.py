from django.db import models

# Create your models here.

class CalendarDay(models.Model):
    date = models.DateField(verbose_name="Дата")
    notes = models.TextField(blank=True, null=True, verbose_name="Заметки")

    def __str__(self):
        return f"День: {self.date}"

class CalendarEvent(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Подія")
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f"Подія на {self.date}"


