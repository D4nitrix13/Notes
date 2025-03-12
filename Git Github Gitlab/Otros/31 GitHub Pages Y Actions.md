<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"GitHub Pages Y Actions"***

> *GitHub Pages y GitHub Actions son dos características poderosas de GitHub que se pueden utilizar juntas para automatizar el proceso de publicación de un sitio web estático. Aquí hay una descripción general de cada una:*

---

## ***GitHub Pages:***

> *GitHub Pages es un servicio de alojamiento web estático proporcionado por GitHub de forma gratuita. Te permite crear sitios web estáticos directamente desde tus repositorios de GitHub y publicarlos en Internet.*

**Características principales:**

- *Alojamiento gratuito de sitios web estáticos.*

- *Integración directa con repositorios de GitHub.*

- *Admite la generación de sitios estáticos utilizando Jekyll o cualquier otro generador de sitios estáticos.*

---

### ***GitHub Actions:***

> *GitHub Actions es un sistema de automatización basado en flujos de trabajo que te permite automatizar tareas comunes y procesos dentro de tu repositorio de GitHub.*

**Características principales:**

- *Te permite automatizar tareas como pruebas, compilaciones, despliegues, entre otros.*

- *Utiliza ficheros de flujo de trabajo YAML para definir las acciones que deseas realizar.*

- *Se puede integrar con eventos de GitHub, como confirmaciones de código, creación de pull requests, entre otros.*

---

### ***Integración de GitHub Pages y Actions:***

- *Puedes utilizar GitHub Actions para automatizar el proceso de generación y despliegue de tu sitio web estático en GitHub Pages. Por ejemplo, puedes configurar un flujo de trabajo de GitHub Actions que se active cada vez que realices una confirmación en la rama `main`, genere el sitio web estático y lo publique en GitHub Pages.*

*Ejemplo de flujo de trabajo de GitHub Actions para desplegar un sitio web estático en GitHub Pages:*

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Build site
      run: |
        # Coloca aquí los comandos para generar el sitio web estático (por ejemplo, npm run build, hugo, jekyll, etc.)

    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./path/to/generated/site
```

- *Este flujo de trabajo se activará en cada confirmación en la rama `main`, generará el sitio web estático y lo publicará en GitHub Pages utilizando el token de acceso generado automáticamente por GitHub Actions (`secrets.GITHUB_TOKEN`). Asegúrate de ajustar los comandos de construcción (`run`) y la ubicación del directorio de publicación (`publish_dir`) según las necesidades de tu proyecto.*

- *En resumen, al combinar GitHub Pages y GitHub Actions, puedes automatizar el proceso de despliegue de tu sitio web estático, lo que te permite enfocarte más en el desarrollo de tu proyecto y menos en las tareas de implementación.*
