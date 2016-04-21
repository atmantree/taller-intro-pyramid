# Creando un paquete

La mayor parte del desarrollo Python moderno es hecho en forma de Paquetes
Python. Es por ello que el enfoque de Pyramid es continuar con esta buena
práctica.

## Pasos

1. Cambiese a la carpeta `02`
2. Proceda a crear un archivo llamado `setup.py` con la siguiente información:

   ```Python
   from setuptools import setup

   requires = [
       'pyramid',
   ]

   setup(name='app',
       install_requires=requires,
   )
   ```

3. Instale su nueva aplicación, `python setup.py develop`
4. A continuación proceda a crear un directorio llamado `app`, con la 
   comando `mkdir app`
5. dentro del directorio `app` cree un archivo vacío llamado `__init__.py`
6. copie el archivo `hola_pyramid.py` del ejercicio anterior dentro de `app`
7. valide que funcione el script 

   ```
   python app/hola_pyramid.py
   ```


## Pasos (2da parte) uso de archivo .ini

1. modifique el archivo `setup.py` y agregue 

   ```Python
   from setuptools import setup

   requires = [
       'pyramid',
   ]

   setup(name='app',
       install_requires=requires,
       entry_points="""\
       [paste.app_factory]
       main = app:main
       """,
   )
   ```

2. Cree un archivo llamado `development.ini`

   ```
   [app:main]
   use = egg:app

   [server:main]
   use = egg:pyramid#wsgiref
   host = 0.0.0.0
   port = 6543
   ```

3. Haga una refactorización del archivo `__init__` agregando el contenido del 
   archivo `hola_pyramid.py`.

   ```Python
   from wsgiref.simple_server import make_server
   from pyramid.config import Configurator
   from pyramid.response import Response


   def hello_pyramid(request):
       print('-> solicitud entrante')
       return Response('<body><h1>Hola Pyramid</h1></body>')


   def hello_you(request):
       print('-> solicitud entrante')
       return Response('<body><h1>Hola {}</h1></body>'.format(request.matchdict["name"]))


   def not_found(request):
       return Response('<body><h1>P&aacute;gina no encontrada</h1></body>')



   def main(global_config, **settings):
       config = Configurator(settings=settings)
       config.add_route('hello', '/')
       config.add_route('hello_you', '/nombre/{name}')
       config.add_view(hello_pyramid, route_name='hello')
       config.add_view(hello_you, route_name='hello_you')
       config.add_notfound_view(not_found)
       return config.make_wsgi_app()
   ```

4. Borre el archivo `hola_pyramid.py` 
5. Instale su nuevo módulo `python setup.py develop` 
6. Inicie su aplicación Pyramid con:

   ```
   pserve development.ini --reload
   ```
