from django.db import models
from django.contrib.auth.models import User
from apps.pacientes.models import Pacientes
from django.utils import timezone
from django.utils.timezone import now
from phone_field import PhoneField

# Create your models here.
class Lesiones(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    fisioterapeuta = models.IntegerField(null=True)
    lesion = models.CharField(max_length=30)
    zona = models.CharField(max_length=20)
    motivo = models.CharField(max_length=1024)
    inspeccion = models.CharField(max_length=1024, null=True)
    palpacion = models.CharField(max_length=1024, null=True)
    goniometria = models.CharField(max_length=1024, null=True)
    fuerza = models.CharField(max_length=1024, null=True)
    pruebas_especificas = models.CharField(max_length=1024, default="", null=True)
    objetivo_corto = models.CharField(max_length=512, null=True)
    objetivo_medio = models.CharField(max_length=512, null=True)
    objetivo_largo = models.CharField(max_length=512, null=True)
    plan_tratamiento = models.CharField(max_length=1024)
    observaciones = models.CharField(max_length=1024, default="", null=True)
    num_sesiones = models.IntegerField(default=0)
    fecha_valoracion = models.DateField(default=now())
    fecha_modificacion = models.DateField(default=now())
    estatus = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Lesiones, self).save(*args, **kwargs)

    def __str__(self):
        return self.user
