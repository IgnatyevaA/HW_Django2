from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    """Контроллер для отображения главной страницы интернет-магазина"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def product_detail(request, pk):
    """Контроллер для отображения страницы с подробной информацией о товаре"""
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    """Контроллер для отображения страницы контактов и обработки формы обратной связи"""
    if request.method == 'POST':
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
    
    return render(request, 'catalog/contacts.html')
