from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from blog.models import BlogPost
from catalog.models import Product


class Command(BaseCommand):
    help = "Создает группы модераторов и контент-менеджеров с необходимыми правами."

    product_group_name = "Модератор продуктов"
    content_group_name = "Контент-менеджер"

    def handle(self, *args, **options):
        self._setup_product_moderators()
        self._setup_content_managers()
        self.stdout.write(self.style.SUCCESS("Группы и права успешно настроены."))

    def _setup_product_moderators(self):
        group, _ = Group.objects.get_or_create(name=self.product_group_name)
        product_ct = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(
            content_type=product_ct,
            codename__in=["can_unpublish_product", "delete_product"],
        )
        group.permissions.add(*permissions)

    def _setup_content_managers(self):
        group, _ = Group.objects.get_or_create(name=self.content_group_name)
        blog_ct = ContentType.objects.get_for_model(BlogPost)
        permissions = Permission.objects.filter(
            content_type=blog_ct,
            codename__in=["add_blogpost", "change_blogpost", "delete_blogpost"],
        )
        group.permissions.add(*permissions)

