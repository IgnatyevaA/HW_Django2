from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm


class HomeView(ListView):
    """Контроллер для отображения главной страницы интернет-магазина"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования существующего продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'
