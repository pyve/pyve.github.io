====================
Sitio PyVe en Github
====================

Este proyecto tiene la intención de manejar el control de versiones del sitio
pyve.github.io, tecnicamente solo contiene un conjunto de archivos js, css y html
que permiten tener un pequeño tablero de control de la comunidad python en Venezuela.

Las tecnologías que usan están basadas en bootstrap_

.. _bootstrap: http://twitter.github.io/bootstrap/

¿Cómo colaborar?
================

Es muy sencillo, con un tanto de conocimiento en Javascript y HTML y un manejo básico
de control de versiones puedes enviar tu primer push cambio al sitio.

1. Haz un fork en el branch. Para hacerlo tienes que crear una cuenta en github, y una vez autenticado, ingresar en el
proyecto https://github.com/pyve/pyve.github.com y hacer clic en el ícono "fork" que está en la esquina superior
derecha. Ahora debe aparecer una copia del proyecto en tu cuenta.

2. Descarga tu fork. Abre el terminal y en la carpeta donde tienes tus proyectos (si no la tienes créala,
no seas desorganizado) ejecuta el comando

.. code-block:: shell

   $ git clone https://github.com/[tu_cuenta_en_github]/pyve.github.com.git

3. Haz los cambios. Es decir, edita con las aplicaciones de tu preferencia los arcvhivos del repositorio. Esto requiere
realizar el ciclo típico de git: ``git status``, ``git add`` (si añades archivos), ``git commit``.

4. Subelos a tu cuenta github. Mediante el comando ``git push`` a tu cuenta en github.

5. Haz un pull request. Para hacerlo tienes que verificar que los cambios que realizaste están actualizados en tu
cuenta de github, y hacer clic en el ícono "pull request" que se encuentra a la derecha. En la nueva ventana que
aparece seleccionar "New pull request" a continuación debe aparecer una interfaz que muestra las diferencias entre
los cambios que has realizado y el contenido actual del repositorio pyve. Finalmente haces clic donde dice "Click to
create a pull request for this comparison" para que los administradores del sitio pyve verifiquen y aprueben los cambios
que realizaste.

TODO: Sería cool contar con un video de estos 5 pasos en acción.
