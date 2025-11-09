from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from .models import Product


class HomeView(ListView):
    """Контроллер для отображения главной страницы интернет-магазина"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
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
