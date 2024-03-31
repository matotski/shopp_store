from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

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
        fields = ['first_name','last_name','username','password','email']

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input'}),required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'image','username', 'email',]
