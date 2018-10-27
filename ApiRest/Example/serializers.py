from .models import Usuario,Administrador,Cita,Doctor,HistorialEstudiante
from rest_framework import serializers


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('idcodigo', 'nombreApellido', 'fechaNacimiento', 'correo', 'carrera', 'celular', 'estado', 'usuario', 'password')

class AdministradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Administrador
        fields = ('id', 'usuarioAdmi', 'passwordAdmi')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'nombreApellido', 'correo','especialidad','cecular')

class CitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cita
        fields = ('id', 'fecha', 'hora','idDoctor','codigoEstudiante')

class HistorialEstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistorialEstudiante
        fields = ('id', 'idCita', 'dolencias','receta','proximaCita','codigoEstudiante')
