from django.db import models
from django.contrib.auth.models import User

class Especialidades(models.Model):

    especialidad=models.CharField(max_length=50)
    adulto = models.BooleanField()
    pediatrico = models.BooleanField()

    def __str__(self):
        return f"Especialidad: {self.especialidad} - Adulto {self.adulto} - Pediatrico {self.pediatrico}"


class Laboratorio(models.Model):
    test= models.CharField(max_length=30)
    sangre = models.BooleanField()
    orina = models.BooleanField()
    heces = models.BooleanField(blank=True, null=True)
    otro = models.BooleanField()

    def __str__(self):
        return f"Test: {self.test} - Sangre {self.sangre} - Orina {self.orina} - Heces {self.heces} - Otro {self.otro}"
   

class Staff(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Profesión: {self.profesion}"


class Imagenes(models.Model):
    estudio= models.CharField(max_length=50)

    def __str__(self):
        return f"Estudio: {self.estudio}"


class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
      return f"{self.user} - {self.imagen}"