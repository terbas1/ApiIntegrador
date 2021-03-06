# Generated by Django 2.1.2 on 2018-10-26 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(max_length=500, primary_key=True, serialize=False)),
                ('usuarioAdmi', models.CharField(max_length=100)),
                ('passwordAdmi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(max_length=500, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(max_length=500, primary_key=True, serialize=False)),
                ('nombreApellido', models.CharField(max_length=300)),
                ('correo', models.EmailField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('cecular', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialEstudiante',
            fields=[
                ('id', models.AutoField(max_length=500, primary_key=True, serialize=False)),
                ('dolencias', models.CharField(max_length=700)),
                ('receta', models.CharField(max_length=700)),
                ('proximaCita', models.DateField(verbose_name='date_published')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idcodigo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombreApellido', models.CharField(max_length=300)),
                ('fechaNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=100)),
                ('carrera', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='historialestudiante',
            name='codigoEstudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Example.Usuario'),
        ),
        migrations.AddField(
            model_name='historialestudiante',
            name='idCita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Example.Cita'),
        ),
        migrations.AddField(
            model_name='cita',
            name='codigoEstudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Example.Usuario'),
        ),
        migrations.AddField(
            model_name='cita',
            name='idDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Example.Doctor'),
        ),
    ]
