from django.db import models


class BlogPost(models.Model):
    """Модель блоговой записи"""
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи"
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое статьи"
    )
    preview = models.ImageField(
        upload_to="blog/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью статьи"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания статьи"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Признак публикации",
        help_text="Опубликована ли статья"
    )
    views_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Количество просмотров статьи"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["-created_at"]
