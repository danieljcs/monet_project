from django.contrib import admin
from .models import *

# Register your models here.
#SE AGREGA MODELO DE CONTROL DE REGISTROS Y SE DEFINE CUALES CAMPOS VA MOSTRAR
@admin.register(ControlRegistro)
class ControlRegistroAdmin(admin.ModelAdmin):
    list_display = ('tipo_registro','nit_entidad_recaudador','nombre_entidad_recaudador','codigo_convenio','fecha_transmision','secuencia_envio','fecha_vencimiento','numero_registros','valor_total_transacciones')

#SE AGREGA MODELO DE CONTROL DE DETALLE Y SE DEGFINES CUALES CAMPOS VA MOSTRAR
@admin.register(ControlDetalle)
class ControlDetalleAdmin(admin.ModelAdmin):
    list_display = ('control','tipo_registro','nit_entidad_pagador','nombre_entidad_pagador','cuenta_bancaria_pagador','numero_cuenta','tipo_transaccion','valor_transaccion','indicador_validacion','referencia_1','referencia_2','fecha_vencimiento','periodos_facturados','ciclo')

