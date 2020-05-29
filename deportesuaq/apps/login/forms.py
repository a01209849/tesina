from django import forms
from django.contrib.auth.models import User
from django.contrib import messages

class Form_iniciar_sesion(forms.ModelForm):

    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(Form_iniciar_sesion, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuario', 'style': 'width: 80% !important;'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña', 'style': 'width: 80% !important;'})

    class Meta:
        model = User
        fields = ('username', 'password')
