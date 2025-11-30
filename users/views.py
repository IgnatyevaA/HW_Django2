from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import UserRegisterForm, UserLoginForm


class RegisterView(FormView):
    """Представление для регистрации пользователя"""
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Обработка успешной валидации формы регистрации"""
        user = form.save()
        login(self.request, user)
        try:
            self.send_welcome_email(user.email)
        except Exception as e:
            # Если отправка письма не удалась, регистрация все равно должна пройти успешно
            # В production можно добавить логирование ошибки
            pass
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Отправка приветственного письма пользователю"""
        from django.conf import settings
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)


class UserLoginView(LoginView):
    """Представление для авторизации пользователя"""
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')


class UserLogoutView(LogoutView):
    """Представление для выхода пользователя из системы"""
    next_page = reverse_lazy('home')
