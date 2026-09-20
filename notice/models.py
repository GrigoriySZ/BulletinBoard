from django.db import models
from django.contrib.auth.models import User


class Notice(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        help_text='Введите заголовок объявления'
    )
    content = models.TextField(
        verbose_name='Текст объявления',
        help_text='Введите тектс объявления'
    )
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Имя автора',
        related_name='notices',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = "Объявление"
            verbose_name_plural = "Объявления"

            ordering = ['-created_at']