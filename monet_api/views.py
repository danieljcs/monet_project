from rest_framework.decorators import api_view
from django.http import HttpResponse , HttpResponseRedirect,JsonResponse
from .models import *
import requests
from django.core.serializers import serialize

# API DE CONSULTA: TRAE TODOS LOS DATOS EXISTENTES Y RELACIONADOS EN LOS DOS MODELOS
@api_view(['GET']) # METODO GET
def get_data_controles(request):
    data = {} # SE CREA EL OBJETO DE RESPUESTA
    objeto_resp = {} # SE CREA EL OBJETO PARA LA DATA EN LA RESPUESTA
    objeto_resp['controles'] = [] #SE CREA LA LISTA DE CONTROLES
    try:
        controles = ControlRegistro.objects.all()
        for item in controles: #SE RECORREN LOS MODELOS EXISTENTES
            data_control = {} # SE CREA MODELO EL CUAL VA TENER LOS DATOS DEL CONTROL Y LOS DATOS DE LOS DETALLES DEL CONTROL RELACIONADOS AL MISMO
            control_detalle = ControlDetalle.objects.filter(control = item)
            data_control['control'] = serialize('json', [item], ensure_ascii=False)
            data_control['control_detalle'] = [serialize('json', [detalle], ensure_ascii=False) for detalle in control_detalle]
            objeto_resp['controles'].append(data_control) # SE AGREGA A LA LISTA

        data['ERROR'] = False
        data['mensaje'] = 'SUCCESS'
        data['data'] = objeto_resp
        return JsonResponse(data,safe=False)
    except Exception as err:
        print(err)
        data['ERROR'] = True
        data['mensaje'] = 'ERROR: '
        data['data'] = {}
        return JsonResponse(data,safe=False)