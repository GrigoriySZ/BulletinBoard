from django.db import models

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
    author_name = models.CharField(
        max_length=50,
        verbose_name='Имя автора',
        help_text='Введите имя автора объявления'
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