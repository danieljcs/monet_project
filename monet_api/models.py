from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class ControlRegistro(models.Model):
    tipo_registro = models.IntegerField(validators=[MaxValueValidator(9)])
    nit_entidad_recaudador = models.IntegerField(validators=[MaxValueValidator(9999999999999)])
    nombre_entidad_recaudador = models.CharField(max_length=20, null=True,blank=True)
    codigo_convenio = models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    fecha_transmision  = models.IntegerField(validators=[MaxValueValidator(99999999)])
    secuencia_envio = models.CharField(max_length=1)
    fecha_vencimiento  = models.IntegerField(validators=[MaxValueValidator(99999999)])
    numero_registros = models.IntegerField(validators=[MaxValueValidator(99999999)])
    valor_total_transacciones = models.IntegerField(validators=[MaxValueValidator(99999999999999999)])

class ControlDetalle(models.Model):
    #OPCIONES POR DEFECTO PARA INDICADOR DE VALIDACION
    OPCIONES_INDICADOR = [
        ("S", "SI"),
        ("N", "NO"),
        ]
    #OPCIONES PARA LOS TIPOS DE TRANSACCION
    OPCIONES_TIPO_TRANSACCION = [
        (57, "Cuenta Corriente"),
        (67, "Cuenta Ahorros"),
        (77, "TC VISA"),
        (87, "TC MASTER"),
        (97, "AMEX")
        ]
    control = models.ForeignKey(ControlRegistro, on_delete=models.PROTECT)
    tipo_registro = models.IntegerField(validators=[MaxValueValidator(9)])
    nit_entidad_pagador = models.CharField(max_length=13, null=True,blank=True)
    nombre_entidad_pagador = models.CharField(max_length=20, null=True,blank=True)
    cuenta_bancaria_pagador = models.CharField(max_length=9, null=True,blank=True)
    numero_cuenta = models.CharField(max_length=17, null=True,blank=True)
    tipo_transaccion = models.CharField(choices=OPCIONES_TIPO_TRANSACCION,max_length=2, null=True,blank=True)
    valor_transaccion = models.IntegerField(validators=[MaxValueValidator(99999999999999999)])
    indicador_validacion = models.CharField(choices=OPCIONES_INDICADOR,max_length=1 , null=True,blank=True)
    referencia_1 = models.CharField(max_length=30, null=True,blank=True)
    referencia_2 = models.CharField(max_length=30, null=True,blank=True)
    fecha_vencimiento  = models.IntegerField(validators=[MaxValueValidator(99999999)], null=True,blank=True)
    periodos_facturados = models.CharField(max_length=2, null=True,blank=True)
    ciclo = models.CharField(max_length=3, null=True,blank=True)

