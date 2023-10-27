from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Articles


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('/login', )
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials. Please try again.'})
    return render(request, 'login.html', {})


def create_view(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            article = Articles.objects.create(title=title, content=content)
            messages.success(request, ('Article Created Successfully!'))
            return render(request, 'create.html', {'success_message': 'Article created Successfully'})

        else:
            return render(request, 'create.html', {'error_message': 'Both title and content are required.'})
    return render(request, 'create.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')