# Introducción

## Clonar repositorio

```
$ git clone https://github.com/atmantree/taller-intro-pyramid.git
$ cd taller-intro-pyramid
$
```

## Crear y activar el Virtualenv

```
$ pyvenv env
$ source env/bin/activate 
(env) $ python --version
Python 3.x.y
(env) $
```

## Instalar Requerimientos de Python

Debido a la corta duración del taller todos los modulos necesarios serán instalados en
este paso sin embargo en sus proyectos recuerde incluirlos al momento que los requiera.

```
(env) $ pip install -r requirements.txt
(env) $
```

## Probar la instalación

```
(env) $ python -c "import pyramid"
(env)$
```

Si no devuelve ningun mensaje de error entonces ha sido bien instalado.

## ¿Qué sigue?

>> [Hola Pyramid](01-hola-pyramid.md)

## Notas

* En caso de que necesite parar el taller, para retomarlo simplemente debe activar nuevamente el
  virtualenv y continuar con el punto en donde se quedó. 
