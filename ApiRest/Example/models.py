from django.db import models

class Usuario (models.Model):

    idcodigo=models.CharField(primary_key=True, max_length=100, null=False)
    nombreApellido=models.CharField(max_length=300, null=False)
    fechaNacimiento=models.DateField(null=False)
    correo=models.EmailField(max_length=100)
    carrera=models.CharField(max_length=100)
    celular=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    usuario=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Administrador(models.Model):
    id = models.AutoField(primary_key=True, max_length=500, null=False)
    usuarioAdmi = models.CharField(max_length=100)
    passwordAdmi = models.CharField(max_length=100)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True, max_length=500, null=False)
    nombreApellido=models.CharField(max_length=300)
    correo=models.EmailField(max_length=100)
    especialidad=models.CharField(max_length=100)
    cecular=models.CharField(max_length=20)

class Cita(models.Model):
    id=models.AutoField(primary_key=True, max_length=500, null=False)
    fecha=models.DateField(null=False)
    hora=models.TimeField(null=False)
    idDoctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    codigoEstudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class HistorialEstudiante (models.Model):
    id=models.AutoField(max_length=500, null=False, primary_key=True)
    idCita=models.ForeignKey(Cita, on_delete=models.CASCADE)
    dolencias=models.CharField(max_length=700)
    receta=models.CharField(max_length=700)
    proximaCita=models.DateField('date_published',blank=False)
    codigoEstudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)



