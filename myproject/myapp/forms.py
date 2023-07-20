from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
