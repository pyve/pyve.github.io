# Decisiones de diseño

## Nuevos modelos: page-html y page-md

La página de contactos era muy sencilla y podía escribirse en markdown.

Este es su contenido en markdown:

```markdown
### Lista de correo

[python-venezuela](https://groups.google.com/forum/#!forum/python-venezuela)

### Redes Sociales

[Twitter](https://twitter.com/PyConVe)

[Facebook](https://www.facebook.com/python.ve/)

[G+](https://plus.google.com/communities/113174766589037119283)

[LinkedIn](https://www.linkedin.com/company/fundaci%C3%B3n-python-de-venezuela?)
```

Daba lástima dejarlo en Html, y fue la oportunidad para incluir markdown entre
los posibles lenguajes de marcado a utilizar.

El modelo page-md lo basé en page-html. La única diferencia es el tipo del
campo body, que en este caso es markdown.

La plantilla page-md.html fue casi idéntica a page-html.html, pero tuve que
envolver lo que tenía anteriormente el bloque body dentro de unas etiquetas que
tenían las páginas originales.

El bloque body dentro de la nueva plantilla quedó así:

```markdown
{% block body %}
    <div class="themewrap">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
  {% if this.title %}<h2>{{ this.title }}</h2>{% endif %}
  {{ this.body }}
          </div>
        </div>
      </div>
    </div>
{% endblock %}
```

Ahora tenemos dos modelos: page-html y page-md, para elegir al momento de hacer
una página.

## Nuevo modelo: page-html-end-addon

Este modelo tuve que definirlo para poder incluir un script arbitrario al final
de una página.

El caso específico fue lapágina de la comunidad, que incluye un script al final
de la página, lo cuál no cumplía con el patrón de (cabecera, cuerpo, pie) de
todas las demás, donde sólo el cuerpo varía. En esta página, el pie era
diferente.

Añadía un bloque llamado "addon" al final del layout principal, que todos pueden
definir. El nuevo modelo page-html-end-addon incluye un campo addon que su layout
coloca en el bloque mencionado.

De esta manera, pude agregar el script que llena la lista de los pythonistas de
Venezuela.

## Enlace a otros sitios

He dejado los enoaces a sitios que están dentro de pyve pero son autónomos con
dirección absoluta y no relativa. Ejemplo, http://pyve.github.io/empleos/ y
las páginas propias de los eventos listados.

## Github y Travis [Borrador]

El funcionamiento de la compilación de la página es el descrito en la
[documentación oficial de lektor.](https://www.getlektor.com/docs/deployment/travisci/)

Consideraciones específicas de éste proyecto:

El usuario con el que el push a master se está haciendo es `pyvebot`, para éste
usuario se ha creado una cuenta de correo no supervisada `pyvebot@gmail.com`,
dicha cuenta está configurada con un token en github como es recomendado en la
documentación de lektor para mayor seguridad, en caso de requerir las credenciales
 para administrarla para futuros automatismos nhomar en gmail.com
 te puede ayudar.

Se activó el caché y se instala lektor con requirements.txt para poder en dado
caso automatizar algún otro proceso a través de git hooks.

La Configuración de travis quedó como se muestr en la imagen.

![Travis Config](https://www.evernote.com/l/AJ5glPUCbRVCQJz0uT4M_3nBaiIDIz6EOFMB/image.png)

Si tienes alguna pregunta levanta un issue en éste mismo proyecto.

Ahora en términos de seguridad para el repositorio algunas opciones se
habilitaron, debido a que todos estamos en proceso de aprendizaje y debemos
evitar errores al menos en code per review.

En el README colocaré dichos elementos de seguridad.

A partir de ahora deberás clonar nuevamente tus repositorios para continuar
contribuyendo como lo has hecho hasta ahora solo que no editarás sobre el
branch master (éste se generará automáticamente) deberás hacerlo siguiendo las
estrategias de lektor en el branch generator.

### Generación automática de contenido a partir de los md en el home del proyecto.

Cuando agregamos datos importantes al home, cómo la licencia, los
contribuidores y el tema de los README y los HOWTO se hizo un script
.pre-build.py que los convierte en contenido lektor para ser renderizados
correctamente en la página también.
