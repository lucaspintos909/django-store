from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm

from django.contrib.auth.models import User

def index(request):

    products=[ # ESTO ES PARA PRUEBAS, QUITAR AL INCLUIR BD
            {'title': 'Camiseta', 'price' : 750, 'stock': True},
            {'title': 'Buzo', 'price' : 1500, 'stock': True},
            {'title': 'Crocks', 'price' : 1200, 'stock': False},
            {'title': 'Campera', 'price' : 1340, 'stock': True},
            {'title': 'Mochila Adidas', 'price' : 2600, 'stock': False},
            {'title': 'Mochila Nike', 'price' : 3000, 'stock': True},
            {'title': 'Gorro de lana', 'price' : 800, 'stock': False}
    ]

    context= {
        'title': 'Django Store',
        'text_button': 'Prueba',
        'products': products
    }

    return render(request, 'index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido a Django Store {}'.format(user.username.upper()))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos.')
    
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request,'Sesion cerrada.')
    return redirect('login')

def register(request):
    form = RegisterForm( request.POST or None )

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = User.objects.create_user(username, email, password)

        if user:
            login(request, user)
            messages.success(request, "Usuario creado satisfactoriamente")
            return redirect('index')
        else:
            messages.error(request, "El usuario no ha podido ser creado, verifique los datos e intentelo nuevamente.")
            return redirect('register')

    return render(request, 'users/register.html',{
        'form': form
    })