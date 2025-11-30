from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """Форма для создания и редактирования блоговой записи"""
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок статьи'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Введите содержимое статьи'}),
            'preview': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убеждаемся, что все поля имеют правильные классы
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['preview'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})

