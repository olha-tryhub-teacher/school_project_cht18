from django.conf import settings
from django.db import models


# --- ІНФОРМАЦІЯ / ОГОЛОШЕННЯ ГРУПИ (КЛАСУ) ---
class GroupInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст оголошення")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата оновлення"
    )
    is_important = models.BooleanField(
        default=False, verbose_name="Важливе оголошення"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="group_announcements",
        verbose_name="Автор",
    )

    class Meta:
        verbose_name = "Оголошення групи"
        verbose_name_plural = "Оголошення групи"
        ordering = ["-is_important", "-created_at"]

    def __str__(self):
        return self.title


# --- ОПИТУВАННЯ ТА ГОЛОСУВАННЯ (POLLS) ---
class Poll(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Тема опитування / Питання"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Детальний опис"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активне для голосування"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_polls",
        verbose_name="Автор опитування",
    )

    class Meta:
        verbose_name = "Опитування"
        verbose_name_plural = "Опитування"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Опитування",
    )
    text = models.CharField(
        max_length=255, verbose_name="Текст варіанта відповіді"
    )

    class Meta:
        verbose_name = "Варіант відповіді"
        verbose_name_plural = "Варіанти відповідей"

    def __str__(self):
        return f"{self.poll.title} — {self.text}"

    # Зручний метод для підрахунку кількості голосів за цей варіант
    def get_votes_count(self):
        return self.votes.count()


class Vote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_votes",
        verbose_name="Користувач",
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Опитування",
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Обраний варіант",
    )
    voted_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата голосування"
    )

    class Meta:
        verbose_name = "Голос"
        verbose_name_plural = "Голоси"
        # Один користувач може проголосувати в кожному опитуванні лише 1 раз
        unique_together = ("user", "poll")

    def __str__(self):
        return f"{self.user} проголосував у '{self.poll.title}'"