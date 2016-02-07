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