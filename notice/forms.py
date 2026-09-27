from django import forms
from .models import Notice

class NoticeCreateForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите заголовок...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Введите текст объявления...'
            }),
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содаржание',
        }