from django import forms
from django.contrib.auth.models import User
from .models import Pacientes
from .models import Antecedentes
from django.contrib import messages

class Form_crear_paciente(forms.ModelForm):
    SEXO_OPCIONES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    ESTADO_CIVIL_OPCIONES = (
        ('Soltero', 'Soltero(a)'),
        ('Casado', 'Casado(a)'),
        ('Viudo', 'Viudo(a)'),
        ('Divorciado', 'Divorciado(a)'),
        ('Union Libre', 'Unión libre'),
    )

    DEPORTES_OPCIONES = (
        ('TM', 'Tenis de mesa'),
        ('TKD', 'Tae kwon do'),
        ('FRF', 'Fútbol rápido femenil'),
        ('FRV', 'Fútbol rápido varonil'),
        ('BX', 'Boxeo'),
        ('L', 'Lucha'),
        ('A', 'Atletismo'),
        ('B', 'Beisbol'),
        ('TA', 'Tiro con arco'),
        ('VF', 'Voleibol femenil'),
        ('VV', 'Voleibol varonil'),
        ('SF', 'Soccer femenil'),
        ('SV', 'Soccer varonil'),
        ('HF', 'Handball femenil'),
        ('HV', 'Handball varonil'),
        ('BF', 'Basquetbol femenil'),
        ('BV', 'Basquetbol varonil'),
        ('AZ', 'Ajedrez'),
        ('K', 'Karate'),
        ('J', 'Judo'),
        ('LP', 'Levantamiento de pesas'),
        ('T', 'Tochito'),
        ('FA', 'Fútbol americano'),
        ('E', 'Esgrima'),
        ('S', 'Softball'),
        ('N', 'Ninguna'),
    )

    FACULTADES_OPCIONES = (
        ('FE', 'Enfermería'),
        ('FCA', 'Contaduría y Administración'),
        ('FD', 'Derecho'),
        ('I', 'Informática'),
        ('FCN', 'Ciencias Naturales'),
        ('ING', 'Ingeniería'),
        ('FLL', 'Lenguas y Letras'),
        ('FP', 'Psicología'),
        ('FCPS', 'Ciencias Políticas y Sociales'),
        ('FQ', 'Química'),
        ('FM', 'Medicina'),
        ('FBA', 'Bellas Artes'),
        ('FF', 'Filosofía'),
        ('EB', 'Escuela de Bachilleres'),
        ('N', 'Ninguna'),
    )

    nombre = forms.CharField(label='Nombre(s)', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    apellido_paterno = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    apellido_materno = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    nacimiento = forms.CharField(label='Fecha de Nacimiento')
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES)
    masa = forms.DecimalField()
    talla = forms.DecimalField()
    escolaridad = forms.CharField(max_length=30)
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL_OPCIONES)
    ocupacion = forms.CharField(max_length=30)
    domicilio = forms.CharField(max_length=250)
    telefono = forms.CharField()
    email = forms.EmailField(label="Email")
    facultad = forms.ChoiceField(choices=FACULTADES_OPCIONES)
    deporte = forms.ChoiceField(choices=DEPORTES_OPCIONES)


    def __init__(self, *args, **kwargs):
        super(Form_crear_paciente, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['apellido_paterno'].required = True
        self.fields['apellido_materno'].required = True
        self.fields['nacimiento'].required = True
        self.fields['edad'].required = True
        self.fields['sexo'].required = True
        self.fields['masa'].required = False
        self.fields['talla'].required = False
        self.fields['escolaridad'].required = False
        self.fields['estado_civil'].required = False
        self.fields['ocupacion'].required = False
        self.fields['domicilio'].required = False
        self.fields['email'].required = False
        self.fields['telefono'].required = True
        self.fields['deporte'].required = True
        self.fields['facultad'].required = False
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Nombre'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Apellido Paterno'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Apellido Materno'})
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'id':'id_end_date', 'dp_config':'{"id": "dp_2", "picker_type": "DATE", "linked_to": "dp_1", "options": {"showClose": true, "showClear": true, "showTodayButton": true, "format": "YYYY-MM-DD", "viewMode": "days", "useCurrent": false}}'})
        self.fields['edad'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Edad'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Sexo'})
        self.fields['masa'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Masa (kg)'})
        self.fields['talla'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Talla (mts)'})
        self.fields['escolaridad'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Escolaridad'})
        self.fields['estado_civil'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Estado civil'})
        self.fields['ocupacion'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Ocupación'})
        self.fields['domicilio'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Domicilio'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Telefono (10 dígitos)'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Email'})
        self.fields['facultad'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Facultad'})
        self.fields['deporte'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Deporte'})


    class Meta:
        model = Pacientes
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'nacimiento', 'edad', 'sexo', 'masa', 'talla', 'escolaridad', 'estado_civil', 'ocupacion', 'domicilio', 'telefono', 'email', 'facultad', 'deporte')

class Form_editar_antecedente(forms.ModelForm):
    TIPO_ANTECEDENTE_OPCIONES = (
        ('HF', 'Heredofamilidares'),
        ('PP', 'Personales Patológicos'),
        ('NP', 'Personales No Patológicos'),
    )
    nombre = forms.CharField(label='Nombre del Antecedente', widget=forms.TextInput(attrs={'size': 50, 'maxlength': 50}))
    tipo_antecedente = forms.ChoiceField(label="Tipo de Antecedente", choices=TIPO_ANTECEDENTE_OPCIONES)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'size': 250, 'maxlength': 250}))

    def __init__(self, *args, **kwargs):
        super(Form_editar_antecedente, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['tipo_antecedente'].required = True
        self.fields['descripcion'].required = True
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-antecedentes', 'placeholder': 'Nombre del antecedente'})
        self.fields['tipo_antecedente'].widget.attrs.update({'class': 'form-control', 'id': 'choice-antecedentes', 'placeholder': 'Elige una opción...'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea', 'placeholder': 'Descripción del antecedente'})

    class Meta:
        model = Antecedentes
        fields = ('nombre', 'tipo_antecedente', 'descripcion')
