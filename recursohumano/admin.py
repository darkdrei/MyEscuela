# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models


class NivelEducacionAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class CargoAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class NivelEducativoAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class NivelEnsenanzaAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class GradoEscalafonAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class AreaAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class TipoVinculacionAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class TrabajadorAdmin(admin.ModelAdmin):
    list_display=['identificacion','first_name','last_name','sexo','nivel_educativo']
#end class

class PermisoAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado']
#end class

class PermisosTrabajadorAdmin(admin.ModelAdmin):
    list_display=['trabajador','sede','permiso']
#end class

admin.site.register(models.NivelEducacion, NivelEducacionAdmin)
admin.site.register(models.Cargo, CargoAdmin)
admin.site.register(models.NivelEducativo, NivelEducativoAdmin)
admin.site.register(models.NivelEnsenanza, NivelEnsenanzaAdmin)
admin.site.register(models.GradoEscalafon, GradoEscalafonAdmin)
admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.TipoVinculacion, TipoVinculacionAdmin)
admin.site.register(models.Trabajador, TrabajadorAdmin)
admin.site.register(models.Permiso, PermisoAdmin)
admin.site.register(models.PermisosTrabajador, PermisosTrabajadorAdmin)
