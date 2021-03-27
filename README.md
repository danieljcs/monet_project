# Monet Project

proyecto creaco para prueba tecnica solicitada por la empresa FINTECH.

## Instalacion

Aplicacion hecha en django cuenta con el archivo docker-compose el cual crea la imagen y contenedor para correr la aplicacion.
En caso de que no se vaya ejecutar con docker, se corre el comando para el entorno virtual

```bash
VIRTUALENV
> pip install -r requirements.txt
> python manage.py runserver
DOCKER
docker-compose up
```

## Uso
Una vez ejecutada la aplicacion cuenta con dos urls las cuales son:
```python
http://localhost:8000/admin/ #para acceder al admin proporcionado por django
http://localhost:8000/get_data_controles/ #url de la api para consultar los datos de las tablas
```

