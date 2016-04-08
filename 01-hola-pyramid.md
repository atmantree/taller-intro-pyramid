# Hola Pyramid

Python posee un estándar llamado [WSGI](http://wsgi.readthedocs.org/) que
define como las aplicaciones web Python encajan en un los servidores web
estándar. Es así como define la recepción de solicitudes (requests) y la
entrega de respuestas (responses). Los _Microframeworks Web_ son herramientas
que le permiten encargarse de llevar su idea a la web sin lidiar con las
complejidades de un Framework Fullstack, usualmente agregando abstracciones para
simplificar las funcionalidades del estándar WSGI.

Pyramid permite construír su aplicación al estilo de un _Microframework_, pero
como se verá posteriormente, provée de herramientas para que su web escale a una
solución de mayor tamaño. 

En este paso construiremos un script que levante aplicación WSGI atienda
peticiones, envíe respuestas y haga uso de vistas (hablaremos un poco más del
patrón de diseño _MVC_ en pasos siguientes).


## Pasos

1. Cambiese de la carpeta `01`

   ```
   (env) $ cd 01
   (env) $
   ```
2. Agregue un archivo `hola_pyramid.py`

   ```Python
   from wsgiref.simple_server import make_server
   from pyramid.config import Configurator
   from pyramid.response import Response


   def hello_pyramid(request):
       print('-> solicitud entrante')
       return Response('<body><h1>Hola Pyramid</h1></body>')


   if __name__ == '__main__':
       config = Configurator()
       config.add_route('hello', '/')
       config.add_view(hello_pyramid, route_name='hello')
       app = config.make_wsgi_app()
       server = make_server('0.0.0.0', 6543, app)
       server.serve_forever()
   ```

3. Ejecute el script en la línea su terminal.

   ``` 
   (env) $ python hola_pyramid.py
   ```

5. En su navegador visite la dirección http://localhost:6543/
6. Para finalizar el script presione `Ctrl`+`c`

## Extras

1. Agregar tomar variables desde el request
2. Agregar not vista para not found


