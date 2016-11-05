from django.contrib import admin
from sec.models import *


class contenidoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'status')
	list_filter = ('status',)

class preguntaAdmin(admin.ModelAdmin):
	list_display = ('id_pregunta', 'tipo_pregunta','contenido', 'dificultad' ,'status', 'created_at', 'updated_at')
	list_filter = ('status', 'tipo_pregunta', 'dificultad',)

class asignaturaAdmin(admin.ModelAdmin):
	list_display = ('nrc', 'nombre', 'ejes', 'nivel' ,'status')
	list_filter = ('status', 'ejes',)

class evaluacionAdmin(admin.ModelAdmin):
	list_display = ('id_evaluacion', 'tipoEvaluacion', 'asignatura' ,'status', 'created_at', 'updated_at')
	list_filter = ('status', 'tipoEvaluacion', 'asignatura',)


admin.site.register(contenido, contenidoAdmin)
admin.site.register(pregunta, preguntaAdmin)
admin.site.register(asignatura, asignaturaAdmin)
admin.site.register(evaluacion, evaluacionAdmin)