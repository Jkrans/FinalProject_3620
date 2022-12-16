
from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class LoginForm(UserCreationForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': "form-control",
#         'style': 'max-width: 25rem;',
#         'placeholder': 'Password'}))

#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'username': TextInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 25rem;',
#                 'placeholder': 'Username'
#             }),
#         }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control",
        'style': 'width: 30rem;',
        'placeholder': 'Email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'style': 'width: 30rem;',
        'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'style': 'width: 30rem;',
        'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Username'
            }),
        }
