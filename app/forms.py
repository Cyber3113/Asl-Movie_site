from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Foydalanuvchi nomi"),
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Foydalanuvchi nomi'})
    )
    password = forms.CharField(
        label=_("Parol"),
        widget=forms.PasswordInput(attrs={'placeholder': 'Parol'})
    )
