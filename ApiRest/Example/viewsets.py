from rest_framework import viewsets

from .serializers import UsuarioSerializer,HistorialEstudianteSerializer,CitaSerializer,DoctorSerializer,AdministradorSerializer
from .models import HistorialEstudiante,Administrador,Usuario,Cita,Doctor

class UsuarioViewSet(viewsets.ModelViewSet):

    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer


class AdministradorViewSet(viewsets.ModelViewSet):

    queryset = Administrador.objects.all().order_by('-date_joined')
    serializer_class = AdministradorSerializer

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all().order_by('-date_joined')
    serializer_class = DoctorSerializer

class CitaViewSet(viewsets.ModelViewSet):

    queryset = Cita.objects.all().order_by('-date_joined')
    serializer_class = CitaSerializer

class HistorialEstudianteViewSet(viewsets.ModelViewSet):

    queryset = HistorialEstudiante.objects.all().order_by('-date_joined')
    serializer_class = HistorialEstudianteSerializer