# Decisiones de diseño

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