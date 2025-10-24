from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Имя товара", 
        help_text="Введите наиманование товара")
    description = models.TextField(
        verbose_name="Описание товара", 
        help_text="Введите описание товара")
    photo = models.ImageField(
        upload_to="catalog/photo", 
        blank=True, null=True, 
        verbose_name="Фото", 
        help_text="Загрузите фото товара")
    category = models.CharField(
        max_length=100, verbose_name="Название категории товара", 
        help_text="Введите категорию товара")
    price = models.IntegerField(
        verbose_name="Цена товара", help_text="Введите цену за товар")
    created_at = models.DateField(
        verbose_name="Дата создания товара",
        help_text="Введите дату создания товара",
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения товара",
        help_text="Введите дату последнего изменения товара",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category"]


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Имя товара", 
        help_text="Введите наиманование товара")
    description = models.TextField(
        verbose_name="Описание товара", 
        help_text="Введите описание товара")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]