from django import template

register = template.Library()


@register.filter
def is_product_moderator(user):
    """Проверяет, является ли пользователь модератором продуктов."""
    try:
        if not user or not hasattr(user, 'is_authenticated'):
            return False
        if not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        return user.groups.filter(name="Модератор продуктов").exists()
    except (AttributeError, TypeError):
        return False


@register.filter
def is_content_manager(user):
    """Проверяет, является ли пользователь контент-менеджером."""
    try:
        if not user or not hasattr(user, 'is_authenticated'):
            return False
        if not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        return user.groups.filter(name="Контент-менеджер").exists()
    except (AttributeError, TypeError):
        return False

