from django import forms
from django.contrib.auth.models import User
from .models import Usuarios
from django.contrib import messages

class Form_crear_usuario(forms.ModelForm):
    SEXO_OPCIONES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    TIPO_USUARIO_OPCIONES = (
        ('S', 'Supervisor'),
        ('F', 'Fisioterapeuta'),
    )
    nombre = forms.CharField(label='Nombre(s)', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    apellido_paterno = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    apellido_materno = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    tipo_usuario = forms.ChoiceField(label="Tipo de usuario", choices=TIPO_USUARIO_OPCIONES)
    email = forms.EmailField(label="Email")
    nacimiento = forms.CharField(label='Fecha de Nacimiento')
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES)
    telefono = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(Form_crear_usuario, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['apellido_paterno'].required = True
        self.fields['apellido_materno'].required = True
        self.fields['tipo_usuario'].required = True
        self.fields['email'].required = True
        self.fields['telefono'].required = True
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Nombre'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Apellido Paterno'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Apellido Materno'})
        self.fields['tipo_usuario'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Tipo de Usuario'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Email'})
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'id':'id_end_date', 'dp_config':'{"id": "dp_2", "picker_type": "DATE", "linked_to": "dp_1", "options": {"showClose": true, "showClear": true, "showTodayButton": true, "format": "YYYY-MM-DD", "viewMode": "days", "useCurrent": false}}'})
        self.fields['edad'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Edad'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Sexo'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Telefono (10 dígitos)'})


    class Meta:
        model = Usuarios
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'tipo_usuario', 'email', 'nacimiento', 'edad', 'sexo', 'telefono')

class Form_nuevo_usuario(forms.ModelForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(Form_nuevo_usuario, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['password2'].required = True
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Confirmar Contraseña'})

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

class Form_cambiar_contrasena(forms.ModelForm):
    password = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(Form_cambiar_contrasena, self).__init__(*args, **kwargs)
        self.fields['password'].required = True
        self.fields['password2'].required = True
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Nueva contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Confirmar Contraseña'})

    class Meta:
        model = User
        fields = ('password', 'password2')

class Form_cambiar_datos(forms.ModelForm):
    SEXO_OPCIONES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    TIPO_USUARIO_OPCIONES = (
        ('S', 'Supervisor'),
        ('F', 'Fisioterapeuta'),
    )
    nombre = forms.CharField(label='Nombre(s)', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    apellido_paterno = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    apellido_materno = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'size': 30, 'maxlength': 30}))
    tipo_usuario = forms.ChoiceField(label="Tipo de usuario", choices=TIPO_USUARIO_OPCIONES)
    email = forms.EmailField(label="Email")
    nacimiento = forms.CharField(label='Fecha de Nacimiento')
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES)
    telefono = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(Form_cambiar_datos, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['apellido_paterno'].required = True
        self.fields['apellido_materno'].required = True
        self.fields['tipo_usuario'].required = True
        self.fields['email'].required = True
        self.fields['telefono'].required = True
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Nombre'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Apellido Paterno'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Apellido Materno'})
        self.fields['tipo_usuario'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Tipo de Usuario'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Email'})
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'id':'id_end_date', 'dp_config':'{"id": "dp_2", "picker_type": "DATE", "linked_to": "dp_1", "options": {"showClose": true, "showClear": true, "showTodayButton": true, "format": "YYYY-MM-DD", "viewMode": "days", "useCurrent": false}}'})
        self.fields['edad'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Edad'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Sexo'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Telefono (10 dígitos)'})

    class Meta:
        model = Usuarios
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'tipo_usuario', 'email', 'nacimiento', 'edad', 'sexo', 'telefono')
