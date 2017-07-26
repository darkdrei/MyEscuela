# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import User
# Create your models here.

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Persona(User):
    tipo = models.ForeignKey(TipoDocumento, verbose_name='Tipo de documento')
    identificacion = models.CharField(max_length=20, unique=True, validators=[validators.RegexValidator(re.compile('^([1-9]+[0-9]*){7,20}$'), ('No valida'), 'invalid')])
    direccion = models.CharField(max_length=300, null=True, blank=True)
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True,blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)
    # end def

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)
    # end def
# end class
