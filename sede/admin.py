# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
# Register your models here.


class SectorAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class SectorAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class MunicipioAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class ZonaAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class TipoJornadaAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class TipoCalendarioAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class TipoRecuperacionAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class TipoNivelacionAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class InstitucionlacionAdmin(admin.ModelAdmin):
    list_display=['codigo','nombre','icfes','calendario','sedes']
#end class

class SedeAdmin(admin.ModelAdmin):
    list_display=['institucion','consecutivo','nombre','direccion','municipios','direccion']
#end class

class ConfiguracionAdmin(admin.ModelAdmin):
    list_display=['institucion','year','bloqueo_periodo','visualizacion_descriptores','visualizacion_descriptores','visualizacion_descriptores_nivel']
#end class

admin.site.register(models.Sector, SectorAdmin)
admin.site.register(models.Departamento, DepartamentoAdmin)
admin.site.register(models.Municipio, MunicipioAdmin)
admin.site.register(models.Zona, ZonaAdmin)
admin.site.register(models.TipoJornada, TipoJornadaAdmin)
admin.site.register(models.TipoCalendario, TipoCalendarioAdmin)
admin.site.register(models.TipoRecuperacion, TipoRecuperacionAdmin)
admin.site.register(models.TipoNivelacion, TipoNivelacionAdmin)
admin.site.register(models.Institucion, InstitucionlacionAdmin)
admin.site.register(models.Sede, SedeAdmin)
admin.site.register(models.Configuracion, ConfiguracionAdmin)
