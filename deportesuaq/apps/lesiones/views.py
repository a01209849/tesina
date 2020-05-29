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
from apps.pacientes.models import Pacientes
from apps.pacientes.models import Antecedentes
from .models import Lesiones
from .forms import Form_crear_lesion
from .forms import Form_terminar_lesion


# Create your views here.
def Crear_lesion(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        usuarios = Usuarios.objects.all().order_by('id')
        form_crear_lesion = Form_crear_lesion()
        context = {
            'id_paciente': id_paciente,
            'form_crear_lesion': form_crear_lesion,
            'usuarios': usuarios,
        }
        return render(request, 'lesiones/crear_lesion.html', context)

def Guardar_lesion(request, id_paciente):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            paciente = get_object_or_404(Pacientes, id=id_paciente)
            form_lesion = Form_crear_lesion(request.POST)
            lesion = form_lesion.save(commit=False)
            lesion.paciente = paciente
            lesion.user = request.user
            lesion.fisioterapeuta = request.POST["fisioterapeuta"]
            lesion.save()
            messages.success(request, 'La lesión se creó exitosamente')
            return redirect('lesiones:perfil_lesion', lesion.id)
        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('pacientes:crear_lesion', id_paciente)

def Perfil_lesion(request, id_lesion):
    if not request.user.is_authenticated:#redirecciona al usuario si ya hay una sesion abierta
        return redirect('login:index')
    else:
        lesion = get_object_or_404(Lesiones, id=id_lesion)
        paciente = get_object_or_404(Pacientes, id=lesion.paciente_id)
        usuario = get_object_or_404(Usuarios, id=lesion.user_id)
        fisioterapeuta = get_object_or_404(Usuarios, id=lesion.fisioterapeuta)
        context = {
            'id_lesion': id_lesion,
            'lesion': lesion,
            'paciente': paciente,
            'usuario': usuario,
            'fisioterapeuta': fisioterapeuta,
        }
        return render(request, 'lesiones/perfil_lesion.html', context)

def Editar_lesion(request, id_lesion):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        lesion = get_object_or_404(Lesiones, id=id_lesion)
        usuarios = Usuarios.objects.all().order_by('id')
        form_crear_lesion = Form_crear_lesion(initial={'lesion': lesion.lesion, 'zona': lesion.zona, 'motivo': lesion.motivo,
        'inspeccion': lesion.inspeccion, 'palpacion': lesion.palpacion, 'goniometria': lesion.goniometria,
        'fuerza': lesion.fuerza, 'pruebas_especificas': lesion.pruebas_especificas, 'objetivo_corto': lesion.objetivo_corto,
        'objetivo_medio': lesion.objetivo_medio, 'objetivo_largo': lesion.objetivo_largo,
        'plan_tratamiento': lesion.plan_tratamiento, 'observaciones': lesion.observaciones})
        context = {
            'id_lesion': id_lesion,
            'form_crear_lesion': form_crear_lesion,
            'usuarios': usuarios,
        }
        return render(request, 'lesiones/editar_lesion.html', context)

def Guardar_editar_lesion(request, id_lesion):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_datos = Form_crear_lesion(request.POST)
            lesion = get_object_or_404(Lesiones, id=id_lesion)

            lesion.fisioterapeuta = request.POST['fisioterapeuta']
            lesion.lesion = form_datos['lesion'].value()
            lesion.zona = form_datos['zona'].value()
            lesion.motivo = form_datos['motivo'].value()
            lesion.inspeccion = form_datos['inspeccion'].value()
            lesion.palpacion = form_datos['palpacion'].value()
            lesion.goniometria = form_datos['goniometria'].value()
            lesion.fuerza = form_datos['fuerza'].value()
            lesion.pruebas_especificas = form_datos['pruebas_especificas'].value()
            lesion.objetivo_corto = form_datos['objetivo_corto'].value()
            lesion.objetivo_medio = form_datos['objetivo_medio'].value()
            lesion.objetivo_largo = form_datos['objetivo_largo'].value()
            lesion.plan_tratamiento = form_datos['plan_tratamiento'].value()
            lesion.observaciones = form_datos['observaciones'].value()
            lesion.fecha_modificacion = now()
            lesion.user = request.user
            lesion.save()

            messages.success(request, 'La lesion se actualizó exitosamente')
            return redirect('lesiones:perfil_lesion', id_lesion)
        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('lesiones:editar_lesion', id_lesion)

def Terminar_lesion(request, id_lesion):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        lesion = get_object_or_404(Lesiones, id=id_lesion)
        paciente = get_object_or_404(Pacientes, id=lesion.paciente_id)
        form_terminar_lesion = Form_terminar_lesion(initial={'observaciones': lesion.observaciones})
        context = {
            'id_lesion': id_lesion,
            'form_terminar_lesion': form_terminar_lesion,
        }
        return render(request, 'lesiones/terminar_lesion.html', context)

def Guardar_terminar_lesion(request, id_lesion):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form_datos = Form_terminar_lesion(request.POST)
            lesion = get_object_or_404(Lesiones, id=id_lesion)

            lesion.num_sesiones = form_datos['num_sesiones'].value()
            lesion.observaciones = form_datos['observaciones'].value()
            lesion.estatus = False
            lesion.fecha_modificacion = now()
            lesion.user = request.user
            lesion.save()

            messages.success(request, 'La lesion se finalizó exitosamente')
            return redirect('lesiones:perfil_lesion', id_lesion)
        else:
            messages.error(request, 'Hubo un error. Intentalo de nuevo.')
            return redirect('lesiones:terminar_lesion', id_lesion)

def Borrar_lesion(request, id_lesion):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        lesion = get_object_or_404(Lesiones, id=id_lesion)
        paciente = get_object_or_404(Pacientes, id=lesion.paciente_id)
        lesion.delete()
        messages.success(request, 'La lesión se borró exitosamente')
        return redirect('pacientes:perfil_paciente', paciente.id)
