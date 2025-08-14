from django.contrib.auth import get_user_model
from django.db import models

from task_manager.statuses.models import Status

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name="Статус",
        related_name="tasks"
    )
    labels = models.ManyToManyField(
        'labels.Label',
        related_name='tasks',
        blank=True,
        verbose_name="Метки"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Автор",
        related_name="authored_tasks"
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Исполнитель",
        related_name="executed_tasks",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
