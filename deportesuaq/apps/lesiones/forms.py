from django import forms
from .models import Lesiones
from django.contrib import messages

class Form_crear_lesion(forms.ModelForm):

    ZONA_OPCIONES = (
        ('Cervicales', 'Cervicales'),
        ('Dorsales', 'Dorsales'),
        ('Lumbares', 'Lumbares'),
        ('Sacro', 'Sacro'),
        ('Hombro', 'Hombro'),
        ('Codo', 'Codo'),
        ('Brazo', 'Brazo'),
        ('Antebrazo', 'Antebrazo'),
        ('Muneca', 'Muñeca'),
        ('Mano', 'Mano'),
        ('Falanges', 'Falanges'),
        ('Cadera', 'Cadera'),
        ('Muslo', 'Muslo'),
        ('Pierna', 'Pierna'),
        ('Rodilla', 'Rodilla'),
        ('Tobillo', 'Tobillo'),
        ('Pie', 'Pie'),
        ('Ortejos', 'Ortejos'),
        ('Coxis', 'Coxis'),
    )

    LESION_OPCIONES = (
        ('Esguince Grado I', 'Esguince Grado I'),
        ('Esguince Grado II', 'Esguince Grado II'),
        ('Esguince Grado III', 'Esguince Grado III'),
        ('Contractura', 'Contractura'),
        ('Sobrecarga Muscular', 'Sobrecarga Muscular'),
        ('Tendinopatia', 'Tendinopatía'),
        ('Luxacion', 'Luxación'),
        ('Fractura', 'Fractura'),
        ('Fisura', 'Fisura'),
        ('Distension Grado I', 'Distensión Grado I'),
        ('Distension Grado II', 'Distensión Grado II'),
        ('Distension Grado III', 'Distensión Grado III'),
        ('Meniscopatia', 'Meniscopatía'),
        ('Contusion', 'Contusión'),
        ('Lumbalgia', 'Lumbalgia'),
        ('Cervicalgia', 'Cervicalgia'),
        ('Periostitis', 'Periostitis'),
        ('Prequirurjico', 'Prequirúrjico'),
        ('Postquirurjico', 'Postquirúrjico'),
        ('Inestabilidad', 'Inestabilidad'),
    )

    lesion = forms.ChoiceField(choices=LESION_OPCIONES)
    zona = forms.ChoiceField(choices=ZONA_OPCIONES)
    motivo = forms.CharField(label='Motivo de Consulta', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    inspeccion = forms.CharField(label='Inspección', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    palpacion = forms.CharField(label='Palpación', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    goniometria = forms.CharField(label='Goniometría', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    fuerza = forms.CharField(label='Fuerza', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    pruebas_especificas = forms.CharField(label='Pruebas Específicas', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    objetivo_corto = forms.CharField(label='Objetivos a Corto Plazo', widget=forms.Textarea(attrs={'size': 512, 'maxlength': 512}))
    objetivo_medio = forms.CharField(label='Objetivos a Medio Plazo', widget=forms.Textarea(attrs={'size': 512, 'maxlength': 512}))
    objetivo_largo = forms.CharField(label='Objetivos a Largo Plazo', widget=forms.Textarea(attrs={'size': 512, 'maxlength': 512}))
    plan_tratamiento = forms.CharField(label='Plan de Tratamiento', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))
    observaciones = forms.CharField(label='Observacioines', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))


    def __init__(self, *args, **kwargs):
        super(Form_crear_lesion, self).__init__(*args, **kwargs)
        self.fields['lesion'].required = True
        self.fields['zona'].required = True
        self.fields['motivo'].required = True
        self.fields['inspeccion'].required = False
        self.fields['palpacion'].required = False
        self.fields['goniometria'].required = False
        self.fields['fuerza'].required = False
        self.fields['pruebas_especificas'].required = False
        self.fields['objetivo_corto'].required = True
        self.fields['objetivo_medio'].required = True
        self.fields['objetivo_largo'].required = True
        self.fields['plan_tratamiento'].required = True
        self.fields['observaciones'].required = False
        self.fields['lesion'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Lesión'})
        self.fields['zona'].widget.attrs.update({'class': 'form-control', 'id': 'choice', 'placeholder': 'Zona del cuerpo'})
        self.fields['motivo'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Motivo de Consulta'})
        self.fields['inspeccion'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Inspección'})
        self.fields['palpacion'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Palpación'})
        self.fields['goniometria'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Goniometria'})
        self.fields['fuerza'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Fuerza'})
        self.fields['pruebas_especificas'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Pruebas Específicas'})
        self.fields['objetivo_corto'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Objetivos a corto plazo'})
        self.fields['objetivo_medio'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Objetivos a medio plazo'})
        self.fields['objetivo_largo'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Objetivos a largo plazo'})
        self.fields['plan_tratamiento'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Plan de Tratamiento'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Observaciones adicionales...', 'value': ''})


    class Meta:
        model = Lesiones
        fields = ('lesion', 'zona', 'motivo', 'inspeccion', 'palpacion', 'goniometria', 'fuerza', 'pruebas_especificas', 'objetivo_corto', 'objetivo_medio', 'objetivo_largo', 'plan_tratamiento', 'observaciones')

class Form_terminar_lesion(forms.ModelForm):
    num_sesiones = forms.IntegerField()
    observaciones = forms.CharField(label='Observacioines', widget=forms.Textarea(attrs={'size': 1024, 'maxlength': 1024}))

    def __init__(self, *args, **kwargs):
        super(Form_terminar_lesion, self).__init__(*args, **kwargs)
        self.fields['num_sesiones'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla', 'placeholder': 'Número de sesiones'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control', 'id': 'plantilla-textarea-lesion', 'placeholder': 'Observaciones adicionales...'})

    class Meta:
        model = Lesiones
        fields = ('num_sesiones', 'observaciones')
