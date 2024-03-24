from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control py-4', 'placeholder':'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control py-4', 'placeholder':'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class': 'form-control py-4', 'placeholder':'Введите email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
    username = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control py-4', 'placeholder':'Введите логин'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','email']