# Creando un proyecto Pyramid a partir de una plantilla

Normalmente usted podría crear su aplicación Pyramid manualmente, sin embargo
para su conveniencia Pyramid incluye unos esqueletos. Con ellos puede ir directo
a desarrollar su aplicación.

Pyramid incluye dentro de sus esqueletos una estructura lógica conveniente para
organizar su aplicación, en forma de un paquete, la cual usted podrá extender a
sus necesidades. Al estar organizada en forma de paquete le será más fácil de 
distribuir e instalar por los mecanismos estándar de Python.

Los esqueletos incluidos en Pyramid son:

* Simple: Sin mecanismo de persistencia de datos y con URL Dispatch para los routes
* ZODB: Con persistencia en la base de datos orientada a objetos ZODB y el mecanismo traversal para las urls
* SQL Alchemy: Con el ORM SQL Alchemy para conectar a un gran número de bases de datos y URL Dispatch para los routes.

## Pasos

1. Cámbiese a la carpeta `04`
2. Escriba `pcreate -l` y examine los esqueletos que ofrece Pyramid.
3. Proceda a crear 2 proyectos (uno starter y otro alchemy) examine las diferencias entre ellos 
   y las diferencias con el proyecto del paso anterior.
