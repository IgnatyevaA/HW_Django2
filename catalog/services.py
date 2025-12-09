from django.db.models import Q, QuerySet

from .models import Product


def get_products_by_category(category_id: int, user=None) -> QuerySet:
    """Возвращает продукты указанной категории с учетом прав пользователя."""
    base_qs = Product.objects.filter(category_id=category_id)

    if user and user.is_authenticated:
        products = base_qs.filter(
            Q(status=Product.Status.PUBLISHED) | Q(owner=user)
        ).distinct()
    else:
        products = base_qs.filter(status=Product.Status.PUBLISHED)

    return products.select_related("category", "owner")


