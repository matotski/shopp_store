from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse

app_name='users'

def login(request):
    context = {
        'title': 'myramasa666',

    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
        context = {
        'form':form,
        }
    return render(request,'login.html', context=context)

def register(request):
    return render(request,'users/register.html')
