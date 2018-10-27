from django.shortcuts import render

# Create your views here.
from .models import Usuario, Administrador, Cita, Doctor, HistorialEstudiante
from .serializers import UsuarioSerializer, AdministradorSerializer, CitaSerializer, DoctorSerializer, HistorialEstudianteSerializer
from rest_framework import viewsets


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


class HistorialEstudianteViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstudiante.objects.all()
    serializer_class = HistorialEstudianteSerializer
