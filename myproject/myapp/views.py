from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


# Create your views here.
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def secret_page(request):
    return HttpResponse('<h1>Secret</h1>')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username, raw_password)
            login(request, user)
            print('test1')
            return redirect('home')
    else:
        print('test2')
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('login')