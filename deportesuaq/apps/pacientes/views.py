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
from django import forms
from apps.usuarios.models import Usuarios
from apps.lesiones.models import Lesiones
from .models import Pacientes
from .models import Antecedentes
from .forms import Form_crear_paciente
from .forms import Form_editar_antecedente
import csv

# Create your views here.
def Index(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        pacientes = Pacientes.objects.all().order_by('id')
        usuarios = Usuarios.objects.all().order_by('id')
        context = {
            'pacientes': pacientes,
            'usuarios': usuarios,
        }
        return render(request, 'pacientes/pacientes.html', context)

#---------------------------- PACIENTES ----------------------------------------

def Nuevo_paciente(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        form_crear_paciente = Form_crear_paciente()
        date_input = 'nacimiento'
        context = {
            'form_crear_paciente': form_crear_paciente,
            'date_input': date_input,
        }
        return render(request, 'pacientes/crear_paciente.html', context)

def Guardar_paciente(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_paciente = Form_crear_paciente(request.POST)
            id_email = form_paciente['email'].value()
            if Pacientes.objects.filter(email=id_email):
                messages.error(request, 'El paciente ya existe')
                return redirect('pacientes:nuevo_paciente')
            else:
                paciente = form_paciente.save(commit=False)
                paciente.save()
                paciente = get_object_or_404(Pacientes, email=id_email)
                paciente.user = request.user
                paciente.save()
                messages.success(request, 'El paciente se creó exitosamente')
                return redirect('pacientes:antecedentes_paciente', paciente.id)
        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('pacientes:nuevo_paciente')

def Borrar_paciente(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        paciente = get_object_or_404(Pacientes, id=id_paciente)
        paciente.delete()
        messages.success(request, 'El usuario se borró exitosamente')
        return redirect('pacientes:index')

def Perfil_paciente(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        paciente = get_object_or_404(Pacientes, id=id_paciente)
        user = get_object_or_404(User, username=paciente.user)
        usuario = get_object_or_404(Usuarios, user=user.id)
        hfs = Antecedentes.objects.filter(paciente=paciente.id, tipo_antecedente="HF")
        pps = Antecedentes.objects.filter(paciente=paciente.id, tipo_antecedente="PP")
        nps = Antecedentes.objects.filter(paciente=paciente.id, tipo_antecedente="NP")
        lesiones = Lesiones.objects.filter(paciente=paciente.id).order_by('id')
        fisioterapeutas = Usuarios.objects.all().order_by('id')
        context = {
            'paciente': paciente,
            'usuario': usuario,
            'lesiones': lesiones,
            'fisioterapeutas': fisioterapeutas,
            'hfs': hfs,
            'pps': pps,
            'nps': nps,
        }
        return render(request, 'pacientes/perfil_paciente.html', context)

#-------------------- CAMBIAR DATOS PACIENTE ------------------------------

def Editar_paciente(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        paciente = get_object_or_404(Pacientes, id=id_paciente)
        form_crear_paciente = Form_crear_paciente(initial={'nombre': paciente.nombre, 'apellido_paterno': paciente.apellido_paterno,
        'apellido_materno': paciente.apellido_materno, 'nacimiento': paciente.nacimiento, 'edad': paciente.edad,
        'sexo': paciente.sexo, 'masa': paciente.masa, 'talla': paciente.talla, 'escolaridad': paciente.escolaridad,
        'estado_civil': paciente.estado_civil, 'ocupacion': paciente.ocupacion, 'domicilio': paciente.domicilio,
        'telefono': paciente.telefono, 'email': paciente.email, 'facultad': paciente.facultad, 'deporte': paciente.deporte})
        context = {
            'id_paciente': id_paciente,
            'paciente': paciente,
            'form_crear_paciente': form_crear_paciente,
        }
        return render(request, 'pacientes/editar_paciente.html', context)

def Guardar_editar_paciente(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_datos = Form_crear_paciente(request.POST)
            paciente = get_object_or_404(Pacientes, id=id_paciente)

            paciente.nombre = form_datos['nombre'].value()
            paciente.apellido_paterno = form_datos['apellido_paterno'].value()
            paciente.apellido_materno = form_datos['apellido_materno'].value()
            paciente.nacimiento = form_datos['nacimiento'].value()
            paciente.edad = form_datos['edad'].value()
            paciente.sexo = form_datos['sexo'].value()
            paciente.masa = form_datos['masa'].value()
            paciente.talla = form_datos['talla'].value()
            paciente.escolaridad = form_datos['escolaridad'].value()
            paciente.estado_civil = form_datos['estado_civil'].value()
            paciente.ocupacion = form_datos['ocupacion'].value()
            paciente.domicilio = form_datos['domicilio'].value()
            paciente.telefono = form_datos['telefono'].value()
            paciente.email = form_datos['email'].value()
            paciente.facultad = form_datos['facultad'].value()
            paciente.deporte = form_datos['deporte'].value()
            paciente.fecha_modificacion = now()
            paciente.user = request.user
            paciente.save()

            messages.success(request, 'El paciente se actualizó exitosamente')
            return redirect('pacientes:perfil_paciente', id_paciente)
        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('pacientes:editar_paciente', id_paciente)

#------------------------------ ANTECEDENTES -----------------------------------

def Antecedentes_paciente(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        paciente = get_object_or_404(Pacientes, id=id_paciente)
        id_paciente = paciente.id
        context = {
            'id_paciente': id_paciente,
        }
        return render(request, 'pacientes/crear_antecedentes.html', context)

def Guardar_antecedentes(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            paciente = get_object_or_404(Pacientes, id=id_paciente)
            cantidad = int(request.POST["cantidad"])

            for i in range(cantidad):
                nombre = request.POST["nombre" + str(i)]
                tipo = request.POST["tipo" + str(i)]
                descripcion = request.POST["descripcion" + str(i)]
                Antecedentes.objects.create(paciente=paciente, tipo_antecedente=tipo, nombre=nombre, descripcion=descripcion)

            messages.success(request, 'El antecedente se creó exitosamente')
            return redirect('pacientes:perfil_paciente', id_paciente)
        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('pacientes:antecedentes_paciente', id_paciente)

def Editar_antecedente(request, id_antecedente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        antecedente = get_object_or_404(Antecedentes, id=id_antecedente)
        form_editar_antecedente = Form_editar_antecedente(initial={'nombre': antecedente.nombre,
        'tipo_antecedente': antecedente.tipo_antecedente, 'descripcion': antecedente.descripcion})
        context = {
            'antecedente': antecedente,
            'form_editar_antecedente': form_editar_antecedente,
        }
        return render(request, 'pacientes/editar_antecedente.html', context)

def Guardar_editar_antecedente(request, id_antecedente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            antecedente = get_object_or_404(Antecedentes, id=id_antecedente)
            form_datos = Form_editar_antecedente(request.POST)
            antecedente.nombre = form_datos['nombre'].value()
            antecedente.tipo_antecedente = form_datos['tipo_antecedente'].value()
            antecedente.descripcion = form_datos['descripcion'].value()
            antecedente.save()
            messages.success(request, 'El antecedente se actualizó exitosamente')
            return redirect('pacientes:perfil_paciente', antecedente.paciente_id)

        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('pacientes:editar_antecedente', id_antecedente)

def Descargar_lesiones(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lesiones.csv"'
        writer = csv.writer(response)
        writer.writerow(['id','Edad','Sexo','Masa (kg)','Talla (mts)','Deporte','Lesion','Zona',])
        pacientes = Pacientes.objects.all().order_by('id')
        for paciente in pacientes:
            lesiones = Lesiones.objects.filter(paciente_id=paciente.id)
            for lesion in lesiones:
                row = [lesion.id,paciente.edad, paciente.sexo, paciente.masa, paciente.talla, paciente.deporte, lesion.lesion, lesion.zona]
                writer.writerow(row)
        return response

def Borrar_antecedente(request, id_antecedente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        antecedente = get_object_or_404(Antecedentes, id=id_antecedente)
        paciente = get_object_or_404(Pacientes, id=antecedente.paciente_id)
        antecedente.delete()
        messages.success(request, 'El antecedente se borró exitosamente')
        return redirect('pacientes:perfil_paciente', paciente.id)
