from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now
from phone_field import PhoneField

# Create your models here.
class Pacientes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    nacimiento = models.DateField()
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    masa = models.DecimalField(decimal_places=2, max_digits=5)
    talla = models.DecimalField(decimal_places=2, max_digits=5)
    escolaridad = models.CharField(max_length=30)
    estado_civil = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=200)
    telefono = PhoneField()
    email = models.EmailField(max_length=100)
    facultad = models.CharField(max_length=5, default='N')
    deporte = models.CharField(max_length=5, default='N')
    fecha_ingreso = models.DateField(default=now())
    fecha_modificacion = models.DateField(default=now())

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Pacientes, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

class Antecedentes(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    tipo_antecedente = models.CharField(max_length=2)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.user
