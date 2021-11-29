from django.shortcuts import render, redirect
from django.http.response import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def views_singup(request):
    return render(request, 'home_pages/login.html')

def singup(request):
    if request.POST:
        username = request.POST.get('username') # Recuperando os parametros enviados pelo formulário
        password = request.POST.get('password') # Recuperando os parametros enviados pelo formulário

        usuario = authenticate(username=username, password=password) # Fazendo a autenticação
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha invalido!")
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')
