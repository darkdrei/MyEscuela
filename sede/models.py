# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class Sector(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class

class Departamento(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Municipio(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Zona(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class TipoJornada(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class TipoCalendario(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class TipoRecuperacion(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Recuperacion"
        verbose_name_plural = "Recuperaciones"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class TipoNivelacion(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Nivelacion"
        verbose_name_plural = "Nivelaciones"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Institucion(models.Model):
    codigo = models.CharField(max_length=100, verbose_name='Codigo Dane')
    nombre = models.CharField(max_length=200)
    resolucion = models.CharField(max_length=800, verbose_name='resolución')
    departamento = models.ForeignKey(Departamento)
    municipios = models.ForeignKey(Municipio)
    zona = models.ForeignKey(Zona)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    sector= models.ForeignKey(Sector)
    calendario = models.ForeignKey(TipoCalendario)
    icfes = models.CharField(max_length=100, verbose_name='Codigo icfes')
    jornadas = models.ManyToManyField(TipoJornada,verbose_name='Tipo de jornadas')
    sedes = models.IntegerField(verbose_name='Número de sedes')
    genero = models.IntegerField(choices=((1,'Mixto'),(2,'Masculino'),(3,'Femenino')), verbose_name='Genero de población atendida')
    subsidiados = models.IntegerField(choices=((1,'Mixto'),(2,'Masculino'),(3,'Femenino')),verbose_name='Ofrece cupos subsidiados')
    cap_exepcionales = models.IntegerField(choices=((1,'Si'),(2,'No')),verbose_name='Educación para capacidades excepcionales')
    escudo = models.ImageField(upload_to="avatar", null=True, blank=True,verbose_name='Escudo institucion')
    web= models.CharField(max_length=150,verbose_name='Página web')
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Institucion"
        verbose_name_plural = "Instituciones"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Sede(models.Model):
    institucion = models.ForeignKey(Institucion, verbose_name='Institución')
    dane = models.CharField(max_length=100, verbose_name='Codigo Dane de la institución')
    codigo_antiguo = models.CharField(max_length=100, verbose_name='Codigo antiguo')
    consecutivo = models.CharField(max_length=100, verbose_name='Consecutivo')
    nombre = models.CharField(max_length=100, verbose_name='Consecutivo de la sede')
    municipios = models.ForeignKey(Municipio)
    zona = models.ForeignKey(Zona, null=True, blank=True)
    direccion = models.CharField(max_length=400, verbose_name='Dirección', null=True, blank=True)
    telefono = models.CharField(max_length=10, verbose_name='Dirección', null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Configuracion(models.Model):
    institucion = models.ForeignKey(Institucion)
    year = models.IntegerField(default=datetime.datetime.today().year, verbose_name='Año')
    bloqueo_periodo = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Inhabilitar periodo despues de cierre de fechas')
    visualizacion_descriptores = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Visualizacion de los descriptores entre docenstes del mismo grado')
    visualizacion_descriptores = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Visualizacion de los descriptores entre docenstes del mismo grado')
    visualizacion_descriptores_nivel = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Visualizacion de los descriptores entre docenstes del mismo nivel educativo')
    notas_docente = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Edicion de notas despues de ser subidas')
    recuperacion = models.ForeignKey(TipoRecuperacion, verbose_name='Tipo de recuperacion')
    recuperacion_porcentaje_final = models.FloatField(default=0, verbose_name='Nota final porcentaje')
    recuperacion_porcentaje_recuperacion = models.FloatField(default=0, verbose_name='Nota recuperacion porcentaje')
    nivelacion = models.ForeignKey(TipoNivelacion, verbose_name='Tipo de nivelacion')
    estudiante_boletin = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Habilitar impresión de boletines a estudiantes')
    director_boletin = models.BooleanField(choices=((1,'Si'),(2,'No')), verbose_name='Habilitar impresión de boletines a directores de grupos')

    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"
    # end class

    def __unicode__(self):
        return u'%s' % (self.institucion.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def

#end class
