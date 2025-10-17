from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Контроллер для отображения главной страницы интернет-магазина"""
    return render(request, 'catalog/home.html')


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
        return HttpResponse(f"""
        <div style="text-align: center; padding: 50px; font-family: Arial, sans-serif;">
            <h2>Спасибо за обращение, {name}!</h2>
            <p>Ваше сообщение успешно отправлено.</p>
            <p>Мы свяжемся с вами по телефону {phone} в ближайшее время.</p>
            <a href="/contacts/" style="color: #007bff;">Вернуться к контактам</a>
        </div>
        """)
    
    return render(request, 'catalog/contacts.html')
