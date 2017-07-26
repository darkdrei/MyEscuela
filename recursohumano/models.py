# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuario import models as usuario
from sede import models as sede
# Create your models here.
ESTADO_CIVIL =(
(1,'Soltero/a'),
(2,'Comprometido/a'),
(3,'Casado/a'),
(4,'Divorciado/a'),
(5,'Union libre'),
(6,'Viudo/a')
)

SEXO = (
(1,'Masculino'),
(2,'Femenino')
)

class NivelEducacion(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Nivel de Educacion"
        verbose_name_plural = "Niveles de Educacion"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Cargo(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class NivelEducativo(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class

class NivelEnsenanza(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Nivel de enseñanza"
        verbose_name_plural = "Niveles de enseñanza"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class GradoEscalafon(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Grado escalafon"
        verbose_name_plural = "Grados escalafones"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Area(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class TipoVinculacion(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tipo de vinculacion"
        verbose_name_plural = "Tipo de vinculaciones"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Trabajador(usuario.Persona):
    exped_departamento = models.ForeignKey(sede.Departamento, verbose_name='Dpto de Expericion')
    exped_municipio = models.ForeignKey(sede.Municipio, verbose_name='Mun de Expericion')
    lugar_nacimiento = models.CharField(max_length=150,verbose_name='Lugar de nacimiento', null=True, blank=True)
    celular = models.CharField(max_length=10,null=True, blank=True)
    estado_civil= models.IntegerField(choices=ESTADO_CIVIL, verbose_name='Estado civil')
    vinculacion = models.DateField(verbose_name='Fecha de vinculacion')
    desvinculacion = models.DateField(verbose_name='Fecha de desvinculación')
    sexo = models.IntegerField(choices=SEXO)
    cargo = models.ForeignKey(Cargo)
    habilitado = models.ManyToManyField(NivelEnsenanza)
    nivel_educativo = models.ForeignKey(NivelEducacion,verbose_name='Nivel educativo')
    escalafon_grado = models.ForeignKey(GradoEscalafon, verbose_name='Grado escalafon')
    areas = models.ManyToManyField(Area, verbose_name='Areas de ensenanza')
    vinculacion =models.ForeignKey(TipoVinculacion, verbose_name='Tipo de vinculacion')

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Permiso(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end

class PermisosTrabajador(models.Model):
    trabajador = models.ForeignKey(Trabajador)
    sede = models.ForeignKey(sede.Sede)
    permiso = models.ForeignKey(Permiso)

    class Meta:
        verbose_name = "Permiso Trabajador"
        verbose_name_plural = "Permisos de trabajadores "
    # end class

    def __unicode__(self):
        return u'%s %s --> %s' % (self.trabajador.first_name,self.trabajador.last_name,self.permiso.nombre)
    # end def

    def __str__(self):
        return u'%s %s --> %s' % (self.trabajador.first_name,self.trabajador.last_name,self.permiso.nombre)
    # end def
#end class
