from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def loginPage(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        user_db  = User.objects.filter(email=username).first()
        if user is not None:
            login(request,user)
            return redirect('frame')
        elif user_db is None:
            messages.info(request, 'Não há nenhuma conta associada a este email.')
        else:
            messages.info(request, 'Credenciais incorretas, verifique novamente.')
        return render(request, "users/login.html")

def signUpPage(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')
    print(email)
    if request.method == 'POST':
        user_exists = User.objects.filter(email = email).exists()
        if user_exists is True:
            messages.info(request, 'Conta já existe!')
        elif password != re_password:
            messages.info(request, 'Senhas diferentes!')
        else:
            User.objects.create_user(email = email, password = password)
            return render(request, "home.html")
    


    return render(request, "users/signUp.html")