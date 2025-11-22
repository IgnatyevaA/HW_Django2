from django import forms
from django.core.exceptions import ValidationError
from .models import Product


# Список запрещенных слов
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'category', 'price', 'created_at', 'updated_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'updated_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        # Стилизация поля name
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        
        # Стилизация поля description
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание продукта',
            'rows': 5
        })
        
        # Стилизация поля photo
        self.fields['photo'].widget.attrs.update({
            'class': 'form-control'
        })
        
        # Стилизация поля category
        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })
        
        # Стилизация поля price
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта',
            'type': 'number',
            'min': '0',
            'step': '1'
        })
        
        # Стилизация поля created_at
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control'
        })
        
        # Стилизация поля updated_at
        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_name(self):
        """Валидация поля name на наличие запрещенных слов"""
        name = self.cleaned_data.get('name')
        if name:
            name_lower = name.lower()
            for word in FORBIDDEN_WORDS:
                if word in name_lower:
                    raise ValidationError(f'Название продукта не может содержать запрещенное слово: "{word}"')
        return name

    def clean_description(self):
        """Валидация поля description на наличие запрещенных слов"""
        description = self.cleaned_data.get('description')
        if description:
            description_lower = description.lower()
            for word in FORBIDDEN_WORDS:
                if word in description_lower:
                    raise ValidationError(f'Описание продукта не может содержать запрещенное слово: "{word}"')
        return description

    def clean_price(self):
        """Валидация поля price - цена не может быть отрицательной"""
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price

