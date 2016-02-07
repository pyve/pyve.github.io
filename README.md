[![Build Status](https://travis-ci.org/pyve/pyve.github.com.svg?branch=master)](https://travis-ci.org/pyve/pyve.github.com)

# Propuesta de FrontEnd para el sitio web de la comunidad Python Venezuela

Este proyecto tiene la intención de manejar el control de versiones del sitio
http://python.org.ve/ que nos permite tener un pequeño tablero de control de la comunidad Python en
Venezuela.

Está basada en el generador de páginas estáticas
[lektor](https://github.com/lektor/lektor)

## ¿Cómo correr la página en tu local?

Clona el repo (o descarga los archivos) y dentro de la carpeta del proyecto ejecuta:

```
sudo pip install lektor
git clone git@github.com:pyve/pyve.github.com.git
git checkout generator
cd pyve.github.com
lektor server
```

Luego visita http://localhost:5000 en tu navegador y ¡voilá!

## Herramientas utilizadas

HTML+CSS+JS son las tecnologías empleadas en el diseño web de esta propuesta, el tema está basado en 
el framework de diseño web [Bootstrap](http://getbootstrap.com/) y puede ser detallado en el archivo 
`assets/css/style.css`.


## Consideraciones del proyecto

* Este repositorio git trata de cumplir con las reglas que propone el flujo de trabajo [git-flow](http://nvie.com/posts/a-successful-git-branching-model/).
* Esta propuesta trata de cumplir con las reglas que propone el [versionamiento semantico](http://semver.org/lang/es/).
* La organización del contenido está guiada por el sitio [python.org.ve](http://pyve.github.io/) actual y por lo escrito en la propuesta del [Rediseño del Sitio Web](https://github.com/pyve/pyve.github.com/wiki/Redise%C3%B1o-del-Sitio-Web).

¿Cómo colaborar?
================

Es muy sencillo. Con un tanto de conocimiento en *javascript* y *HTML* y un manejo básico
de control de versiones puedes enviar tu primer cambio al sitio.

¿Cómo agregar un nuevo contenido?
=================================

Como requisito, debes tener una cuenta en github y seguir los pasos que enumeramos en el archivo 
[CONTRIBUTING.md](https://github.com/pyve/pyve.github.com/blob/master/CONTRIBUTING.md)
desde tu cuenta. Si no tienes una cuenta, puedes crear una cuenta fácilmente en la página de
[github](http://github.com).
