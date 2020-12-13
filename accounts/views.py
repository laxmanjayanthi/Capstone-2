from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("main")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('User created successfully ')
                return redirect('login')

        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    else:
        return render(request, 'login.html')


def shop(request):
    if request.method == 'GET':
        return redirect('/shop')
    else:
        return render(request, 'main.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        return render(request, 'main.html')

def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')
    else:
        return render(request, 'main.html')


def single(request):
    if request.method == 'GET':
        return render(request, 'single.html')
    else:
        return render(request, 'main.html')

def o404(request):
    if request.method == 'GET':
        return render(request, 'o404.html')
    else:
        return render(request, 'main.html')

