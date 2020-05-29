from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now
from phone_field import PhoneField

# Create your models here.
class Usuarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    tipo_usuario = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    nacimiento = models.DateField()
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    telefono = PhoneField(blank=True, help_text='Número de contacto')
    fecha_ingreso = models.DateField(default=now())
    fecha_modificacion = models.DateField(default=now())

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Usuarios, self).save(*args, **kwargs)

    def __str__(self):
        return self.user
