from django.core.management.base import BaseCommand, CommandError
import os
import os.path
import datetime
from monet_api.models import *

class Command(BaseCommand):
    def handle(self, *app_labels, **options):
        try:
            #SE OBTIENE LA RUTA RAIZ DE LA CUAL SE VA LLAMAR EL ARCHIVO TXT
            scriptpath = os.path.dirname(__file__)
            filename = os.path.join(scriptpath, '../../../static/archivo.txt') #SE DEFINE LA RUTA INTERNA EN LA CUAL ESTA UBICADO EL ARCHIVO TXT
            file =open(filename) # SE ABRE EL ARCHIVO


            #SE CREA EL REGISTRO PARA LA PRIMERA LINEA
            # LOS DATOS FUERON OBTENIDOS EN BASE AL MANEJO DE CADENAS [X:Y] EN EL CUAL SE DEFINE DESDE QUE POSICION Y HASTA CUAL DESEA CAPTURAR LA INFORMACION
            primera_linea = file.readline()
            control_registro = ControlRegistro()
            control_registro.tipo_registro = primera_linea[0:1].replace(' ', '')
            control_registro.nit_entidad_recaudador = primera_linea[1:14].replace(' ', '')
            control_registro.nombre_entidad_recaudador = primera_linea[14:34].replace(' ', '')
            control_registro.codigo_convenio = primera_linea[34:49].replace(' ', '')
            control_registro.fecha_transmision = primera_linea[49:57].replace(' ', '')
            control_registro.secuencia_envio = primera_linea[57:58].replace(' ', '')
            control_registro.fecha_vencimiento = primera_linea[58:66].replace(' ', '')
            control_registro.numero_registros = primera_linea[66:74].replace(' ', '')
            control_registro.valor_total_transacciones = int(primera_linea[74:91].replace(' ', '')[:-2])
            control_registro.save()


            #SE RECORREN LAS DEMAS LINEAS
            for x in file.readlines()[1:]:
                #SE CREA EL REGISTRO SIGUIENDO EL PRINCIPIO DE MANEJO DE CADENAS EXPLICADO EN LA ANTERIOR LINEA
                registro_detalle = ControlDetalle()
                registro_detalle.control = control_registro
                registro_detalle.tipo_registro = x[0:1].replace(' ','')
                registro_detalle.nit_entidad_pagador = x[1:14].replace(' ','')
                registro_detalle.nombre_entidad_pagador = x[14:34].replace(' ','')
                registro_detalle.cuenta_bancaria_pagador = x[34:43].replace(' ','')
                registro_detalle.numero_cuenta = x[43:60].replace(' ','')
                registro_detalle.tipo_transaccion = x[60:62].replace(' ','')
                registro_detalle.valor_transaccion = int(x[62:79].replace(' ','')[:-2])
                registro_detalle.indicador_validacion = x[79:80].replace(' ','')
                registro_detalle.referencia_1 = x[80:110].replace(' ','')
                registro_detalle.referencia_2 = x[110:140].replace(' ','')
                registro_detalle.fecha_vencimiento = x[140:148].replace(' ','')
                registro_detalle.periodos_facturados = x[148:150].replace(' ','')
                registro_detalle.ciclo = x[150:153].replace(' ','')
                registro_detalle.save()
                print(registro_detalle)

        except Exception as err:
            #EN CASO DE ERROR SE MUESTRA EN CONSOLA
            print('ERROR: ',err)
            #SE CIERRA EL ARCHIVO ABIERTO
            file.close()
        finally:
            #FINALIZANDO EXITOSAMENTO O CON ERROR IGUAL SE CERRARA EL ARHIVO TXT ABIERTO
            file.close()