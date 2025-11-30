from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя с дополнительными полями"""
    username = None  # Убираем поле username
    
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите ваш email"
    )
    
    avatar = models.ImageField(
        upload_to='users/avatars/',
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите ваш аватар"
    )
    
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Введите ваш номер телефона"
    )
    
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Страна",
        help_text="Введите вашу страну"
    )
    
    USERNAME_FIELD = 'email'  # Используем email для авторизации
    REQUIRED_FIELDS = []  # Убираем username из обязательных полей
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]
    
    def __str__(self):
        return self.email
