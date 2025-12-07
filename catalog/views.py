from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Product


class OwnerRequiredMixin:
    """Mixin to restrict access to product owner."""

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner is None:
            product.owner = request.user
            product.save(update_fields=['owner'])
        if product.owner != request.user:
            raise PermissionDenied("Вы не являетесь владельцем продукта.")
        return super().dispatch(request, *args, **kwargs)


class OwnerOrModeratorMixin:
    """Mixin to restrict actions to owner or product moderators."""

    moderator_group_name = "Модератор продуктов"

    def has_moderator_rights(self, user):
        if not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        return user.groups.filter(name=self.moderator_group_name).exists()

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not self.has_moderator_rights(request.user):
            raise PermissionDenied("Недостаточно прав для удаления продукта.")
        return super().dispatch(request, *args, **kwargs)


class HomeView(ListView):
    """Контроллер для отображения главной страницы интернет-магазина"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(status=Product.Status.PUBLISHED)


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения страницы с подробной информацией о товаре"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsView(View):
    """Контроллер для отображения страницы контактов и обработки формы обратной связи"""
    
    def get(self, request):
        return render(request, 'catalog/contacts.html')
    
    def post(self, request):
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Здесь можно добавить логику сохранения данных в базу данных
        # или отправки email уведомления
        
        # Возвращаем сообщение об успешной отправке
        context = {
            'name': name,
            'phone': phone,
            'message': message
        }
        return render(request, 'catalog/contact_success.html', context)


class ProductListView(ListView):
    """Контроллер для отображения списка всех продуктов"""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(status=Product.Status.PUBLISHED)
        if self.request.user.is_authenticated:
            queryset = Product.objects.filter(
                Q(status=Product.Status.PUBLISHED) | Q(owner=self.request.user)
            ).distinct()
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    """Контроллер для редактирования существующего продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(LoginRequiredMixin, OwnerOrModeratorMixin, DeleteView):
    """Контроллер для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Контроллер для отмены публикации продукта модератором"""

    permission_required = 'catalog.can_unpublish_product'
    raise_exception = True

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.status = Product.Status.DRAFT
        product.save(update_fields=['status'])
        return redirect('product_detail', pk=product.pk)
