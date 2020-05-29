from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.utils.timezone import now
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Form_crear_usuario
from .forms import Form_nuevo_usuario
from .forms import Form_cambiar_contrasena
from .forms import Form_cambiar_datos
from django import forms
from .models import Usuarios

# Create your views here.
def Index(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        usuarios = User.objects.all().order_by('id')
        datos_usuarios = Usuarios.objects.all().order_by('user')

        context = {
            'usuarios': usuarios,
            'datos_usuarios': datos_usuarios,
        }
        return render(request, 'usuarios/usuarios.html', context)

#--------------------- CREAR NUEVO USUARIO -------------------------------

def Nuevo_usuario(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        form_nuevo_usuario = Form_nuevo_usuario()
        context = {
            'form_nuevo_usuario': form_nuevo_usuario,
        }
        return render(request, 'usuarios/nuevo_usuario.html', context)

#Permite al administrador crear cuentas de empleado
def Crear_usuario(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_usuario = Form_nuevo_usuario(request.POST)
            user_test = form_usuario['username'].value()
            if form_usuario['username'].value() == '' or form_usuario['password'].value() == '' or form_usuario['password2'].value() == '':
                messages.error(request, 'Debes llenar todos los campos')
            if User.objects.filter(username=user_test):
                messages.error(request, 'La cuenta ya existe')
            if form_usuario.is_valid():
                cd = form_usuario.cleaned_data
                password = cd['password']
                password2 = cd['password2']
                if password == password2:
                    if len(password) < 8:
                        messages.error(request, 'La contraseña debe tener al menos 8 caracteres')
                    else:
                        usuario = form_usuario.save(commit=False)
                        usuario.set_password(raw_password=password)
                        usuario.save()
                        user = get_object_or_404(User, username=user_test)
                        messages.success(request, 'La cuenta se creó exitosamente')
                        return redirect('usuarios:crear_datos_usuario', user.id )
                else:
                    messages.error(request, 'Las contraseñas no coinciden')
                return redirect('usuarios:nuevo_usuario')
            else:
                return redirect('usuarios:nuevo_usuario')
        else:
            return redirect('usuarios:nuevo_usuario')

#-------------------- CREAR NUEVO USUARIO - DATOS ------------------------

def Crear_datos_usuario(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        form_crear_usuario = Form_crear_usuario()
        date_input = 'nacimiento'
        context = {
            'form_crear_usuario': form_crear_usuario,
            'id_user': id_user,
            'date_input': date_input,
        }
        return render(request, 'usuarios/datos_usuario.html', context)

def Guardar_datos_usuario(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_usuario = Form_crear_usuario(request.POST)
            user = get_object_or_404(User, id=id_user)
            Usuarios.objects.create(user=user, nombre=form_usuario['nombre'].value(), apellido_paterno=form_usuario['apellido_paterno'].value(), apellido_materno=form_usuario['apellido_materno'].value(), tipo_usuario=form_usuario['tipo_usuario'].value(),
            email=form_usuario['email'].value(), nacimiento=form_usuario['nacimiento'].value(), edad=form_usuario['edad'].value(), sexo=form_usuario['sexo'].value(), telefono=form_usuario['telefono'].value())
            return redirect('usuarios:index')
        else:
            return redirect('usuarios:crear_datos_usuario', id_user)

#-------------------- CAMBIAR DATOS USUARIO ------------------------------

def Cambiar_datos(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        user = get_object_or_404(User, id=id_user)
        usuario = get_object_or_404(Usuarios, user=user)
        form_cambiar_datos = Form_cambiar_datos(initial={'nombre': usuario.nombre, 'apellido_paterno': usuario.apellido_paterno,
        'apellido_materno': usuario.apellido_materno, 'tipo_usuario': usuario.tipo_usuario, 'email': usuario.email,
        'nacimiento': usuario.nacimiento, 'edad': usuario.edad, 'sexo': usuario.sexo, 'telefono': usuario.telefono})
        context = {
            'id_user': id_user,
            'usuario': usuario,
            'form_cambiar_datos': form_cambiar_datos,
        }
        return render(request, 'usuarios/cambiar_datos.html', context)

def Guardar_cambio_datos(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_datos = Form_cambiar_datos(request.POST)
            user = get_object_or_404(User, id=id_user)
            usuario = get_object_or_404(Usuarios, user=user)

            usuario.nombre = form_datos['nombre'].value()
            usuario.apellido_paterno = form_datos['apellido_paterno'].value()
            usuario.apellido_materno = form_datos['apellido_materno'].value()
            usuario.tipo_usuario = form_datos['tipo_usuario'].value()
            usuario.email = form_datos['email'].value()
            usuario.nacimiento = form_datos['nacimiento'].value()
            usuario.edad = form_datos['edad'].value()
            usuario.sexo = form_datos['sexo'].value()
            usuario.telefono = form_datos['telefono'].value()
            usuario.fecha_modificacion = now()
            usuario.save()

        return redirect('usuarios:index')

#------------------- CAMBIAR CONTRASEÑA USUARIOS -------------------------

def Cambiar_contrasena(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        user = get_object_or_404(User, id=id_user)
        form_cambiar_contrasena = Form_cambiar_contrasena()
        context = {
            'user': user,
            'form_cambiar_contrasena': form_cambiar_contrasena,
        }
        return render(request, 'usuarios/cambiar_contrasena.html', context)

def Guardar_contrasena(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        user = get_object_or_404(User, id=id_user)
        form_usuario = Form_cambiar_contrasena(request.POST)

        if form_usuario['password'].value() == '' or form_usuario['password2'].value() == '':
            messages.error(request, 'Debes llenar todos los campos')
            return redirect('usuarios:cambiar_contrasena', id_user)

        password = form_usuario['password'].value()
        password2 = form_usuario['password2'].value()

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('usuarios:cambiar_contrasena', id_user)

        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres')
            return redirect('usuarios:cambiar_contrasena', id_user)

        user.set_password(raw_password=password)
        user.save()
        messages.success(request, 'La contraseña se cambió exitosamente')

        user = authenticate(request, username=user.username,password=password)

        if user is not None:
            login(request,user)
            return redirect('usuarios:index')

        else:
            messages.error(request, 'Ocurrió un error con tu cuenta, ingresa nuevamente.')
            return redirect('login:index')

#------------------------- BORRAR USUARIO --------------------------------

def Borrar_usuario(request, id_user):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        user = get_object_or_404(User, id=id_user)
        user.delete()
        messages.success(request, 'El usuario se borró exitosamente')
        return redirect('usuarios:index')
