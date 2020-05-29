from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect #LIBRERIAS ESPECIALES PARA EL LOGIN A PARTIR DE ESTE PUNTO
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import Form_iniciar_sesion


def Index(request): #vista de inicio y primera pagina de la app
    #if not request.user.is_authenticated:#redirecciona al usuario si ya hay una sesion abierta
        form_iniciar_sesion = Form_iniciar_sesion()
        context = {
            'form_iniciar_sesion': form_iniciar_sesion
        }
        return render(request, 'login/login.html', context)
    #else:
        #return render(request, 'login/index.html', {}

def Inicio(request): #vista de inicio y primera pagina de la app
    if not request.user.is_authenticated:#redirecciona al usuario si ya hay una sesion abierta
        return redirect('login:index')
    else:
        return render(request, 'login/index.html', {})

@login_required
def User_logout(request): #funcion para cerrar la sesion del usuario y se redirecciona al index
    logout(request)
    return redirect('login:index')


def User_login(request): # Funcion para validar la existencia de la cuenta de usuario
    if (request.method == 'POST'):
        form = Form_iniciar_sesion(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(request, username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)

                return redirect('login:inicio')
            else:
                return HttpResponse('Cuenta inactiva')
        else:
            messages.error(request, 'Usuario o Contraseña incorrectos!')
            return redirect('login:index')
    else:
        return render(request,'login/login.html',{})
