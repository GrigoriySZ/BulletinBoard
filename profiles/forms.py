from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите email'
            }),
        label='Электронная почта'
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Введите имя пользователя'
                }
            )
        }
        labels = {
            'username': 'Имя пользователя',
            'placeholder': 'Электронная почта'
        }

class ProfileForm(forms.ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        digits_only = re.sub(r'\D', '', phone)
        if len(digits_only) < 10:
            raise ValidationError('Введите корректный номер телефона (минимум 10 цифр)')
        return phone
    
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'phone']
        widgets = {
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Раскажите о себе',
                    'rows': 4
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'form-input',
                    'accept': 'image/*'
                }
            ),
            'phone': forms.TelInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': '+7 (999) 000-00-00', 
                    'pattern': r'^\+?[0-9\s\-\(\)]{10-18}$',
                    'autocomplete': 'tel'
                }
            )
        }
        labels = {
            'bio': 'Биография',
            'avatar': 'Аватар',
            'phone': 'Номер телефона'
        }