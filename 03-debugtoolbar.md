# Debug Toolbar

Para poder revisar el comportamiento de la aplicación y corregir eventuales
errores se debe contar con una herramienta robusta. Esto es del __Debug Toolbar__.

## Pasos

1. Cambiese a la carpeta `03`
2. Copie los archivos fuentes del ejercicio anterior
3. En el archivo `setup.py` agregue `pyramid_debugtoolbar` a los paquetes requeridos

   ```Python
   from setuptools import setup

   requires = [
       'pyramid',
       'pyramid_debugtoolbar',
   ]

   setup(name='app',
         install_requires=requires,
         entry_points="""\
         [paste.app_factory]
          main = app:main
          """,
   )
   ```

4. En el archivo `development.ini` agregue igualmente esta herramienta:

   ```
   [app:main]
   use = egg:app
   pyramid.includes =
       pyramid_debugtoolbar

   [server:main]
   use = egg:pyramid#wsgiref
   host = 0.0.0.0
   port = 6543
   ```

5. Reinstale su aplicación
6. Inicie su aplicación Pyramid:

   ```
   pserve development.ini --reload
   ```


## Ejercicio:

Sustituya `Response` por `xResponse` en alguna de las vistas y visite luego la url.
