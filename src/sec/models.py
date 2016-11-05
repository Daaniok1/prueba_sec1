from __future__ import unicode_literals

from django.db import models
from sec.choices import *

class contenido(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(null=True)
	status = models.BooleanField()

	def __str__(self):
		return self.nombre

class pregunta(models.Model):
	id_pregunta = models.CharField(max_length=50)
	contenido = models.ForeignKey(contenido)
	tipo_pregunta = models.IntegerField(choices = tipoPregunta, default=1)
	dificultad = models.IntegerField(choices = dificultadPregunta, default=1)
	pregunta = models.TextField()
	imagen = models.ImageField(upload_to='images/data', blank=True, null=True)
	respuesta = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField()

	def __str__(self):
	 	return self.id_pregunta

class asignatura(models.Model):
	nrc = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	ejes = models.IntegerField(choices = ejesAsignatura)
	regimen = models.IntegerField(choices = regimenAsignatura, default=1)
	nivel = models.IntegerField(choices = nivelAsignatura, default=1)
	horas_teoricas = models.IntegerField()
	horas_practicas = models.IntegerField(blank=True, null=True)
	status = models.BooleanField()

	def __str__(self):
		return self.nrc

class evaluacion(models.Model):
	id_evaluacion = models.CharField(max_length=50)
	asignatura = models.ForeignKey(asignatura)
	tipoEvaluacion = models.IntegerField(choices = tipo_evaluacion, default=1)
	descripcion = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField()

	def __str__(self):
		return self.id_evaluacion