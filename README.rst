====================
Sitio PyVe en Github
====================

Este proyecto tiene la intención de manejar el control de versiones del sitio
http://python.org.ve/ que nos tener un pequeño tablero de control de la comunidad python en
Venezuela. Técnicamente sólo contiene un conjunto de archivos **js**, **css** y **html**.

Las tecnologías que usan están basadas en bootstrap_

.. _bootstrap: http://twitter.github.io/bootstrap/

¿Cómo colaborar?
================

Es muy sencillo. Con un tanto de conocimiento en **Javascript** y **HTML** y un manejo básico
de control de versiones puedes enviar tu primer cambio al sitio.

Como requisito, debes tener una cuenta en github y seguir los pasos que enumeraremos a continuación
desde tu cuenta. Si no tienes una cuenta, puedes crear una cuenta muy facilmente en la página de
github_.

.. _github: http://www.github.com/

1. **Haz un fork**. Ingresar en el proyecto https://github.com/pyve/pyve.github.com y haz clic en
   el ícono "fork" que está en la esquina superior derecha. Ahora debe aparecer una copia del
   proyecto en tu cuenta.

2. **Descarga tu fork**. Abre el terminal y, en la carpeta donde tienes tus proyectos (si no la
   tienes créala, no seas desorganizado) ejecuta el comando.

.. code-block:: shell

   $ git clone https://github.com/[tu_cuenta_en_github]/pyve.github.com.git

3. **Haz los cambios**. Es decir, edita con las aplicaciones de tu preferencia los arcvhivos del
   repositorio. Esto requiere realizar el ciclo típico de git: ``git status``, ``git add``, ``git
   commit``.

4. **Sube los cambios a tu cuenta github**. Mediante el comando ``git push``.

5. **Haz un pull request**. Verifica que los cambios que realizaste se ven reflejados en tu cuenta
   y haz clic en el ícono "pull request" que se encuentra a la derecha. Luego selecciona "New pull
   request" y por finalmente haces clic donde dice "Click to create a pull request for this
   comparison".

Con este sencillo proceso, habrás enviado tus cambios al sitio de la comunidad de Python Venezuela.
Ahora sólo falta esperar que los administradores del sitio verifiquen y aprueben tus aportes.
