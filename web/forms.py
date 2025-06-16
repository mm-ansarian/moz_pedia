from django import forms
from .models import Article, CustomUser


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'dir':'rtl',
            'id': 'username-input',
            'placeholder': 'نام کاربری‌تان را وارد کنید.',
        })
    )
    first_name = forms.CharField(
        max_length=150,
        label='نام',
        widget=forms.TextInput(attrs={
            'dir':'rtl',
            'id': 'first-name-input',
            'placeholder': 'نام‌تان را وارد کنید.',
        })
    )
    last_name = forms.CharField(
        max_length=150,
        label='نام خانوادگی',
        widget=forms.TextInput(attrs={
            'dir':'rtl',
            'id': 'last-name-input',
            'placeholder': 'نام خانوادگی‌تان را وارد کنید.',
        })
    )
    email = forms.EmailField(
        max_length=150,
        label='ایمیل',
        widget=forms.TextInput(attrs={
            'dir':'rtl',
            'id': 'email-input',
            'placeholder': ' ایمیل‌تان را وارد کنید.',
        })
    )
    password = forms.CharField(
        max_length=128, 
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'dir': 'rtl',
            'id': 'password-input',
            'placeholder': 'رمز عبورتان را وارد کنید.',
        })
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'dir':'rtl',
            'id': 'username-input',
            'placeholder': 'نام کاربری‌تان را وارد کنید.',
        })
    )
    password = forms.CharField(
        max_length=128, 
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'dir': 'rtl',
            'id': 'password-input',
            'placeholder': 'رمز عبورتان را وارد کنید.',
        })
    )


class ArticleForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=60)
    description = forms.CharField(widget=forms.Textarea, min_length=15, max_length=400)
    content = forms.CharField(widget=forms.Textarea, min_length=50, max_length=10000)
