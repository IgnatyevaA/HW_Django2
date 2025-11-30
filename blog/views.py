from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostListView(ListView):
    """Контроллер для отображения списка блоговых записей"""
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blogposts'

    def get_queryset(self):
        """Возвращает только опубликованные статьи"""
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    """Контроллер для отображения деталей блоговой записи"""
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        """Увеличивает счетчик просмотров при открытии статьи"""
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj


class BlogPostCreateView(CreateView):
    """Контроллер для создания новой блоговой записи"""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:blogpost_list')
    
    def form_valid(self, form):
        """Обработка успешной валидации формы"""
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    """Контроллер для обновления блоговой записи"""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'

    def get_success_url(self):
        """Перенаправляет на страницу отредактированной статьи"""
        return reverse('blog:blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    """Контроллер для удаления блоговой записи"""
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blogpost_list')
