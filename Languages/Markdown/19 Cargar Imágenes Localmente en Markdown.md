<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# Cargar Imágenes Localmente en Markdown

Para cargar imágenes en local utilizando Markdown, sigue los pasos a continuación:

1. **Ubicación de las Imágenes:**
   Asegúrate de tener tus imágenes almacenadas localmente en un directorio accesible desde tu fichero Markdown.

2. **Sintaxis de Markdown:**
   Usa la siguiente sintaxis para insertar una imagen en tu fichero Markdown:

   ```markdown
   ![Texto alternativo](ruta/a/la/imagen.png)
   ```

   - `Texto alternativo`: Es una descripción opcional de la imagen que aparece si la imagen no puede cargarse o para accesibilidad.
   - `ruta/a/la/imagen.png`: Es la ruta relativa desde la ubicación de tu fichero Markdown hasta la imagen.

3. **Manejo de Nombres de Ficheros con Espacios:**
   Si el nombre del fichero de imagen contiene espacios, debes escapar cada espacio con `%20`. Por ejemplo:

   ```markdown
   ![Texto alternativo](ruta/a/la/imagen%20con%20espacios.png)
   ```

4. **Ejemplo Práctico:**
   Supongamos que tienes una estructura de directorios como esta:

   ```txt
   ├── mi_proyecto
   │   ├── README.md
   │   └── imagenes
   │       ├── imagen1.png
   │       ├── imagen2 con espacios.png
   │       └── imagen3.png
   ```

   Para insertar `imagen1.png` en tu README, usarías:

   ```markdown
   ![Imagen 1](imagenes/imagen1.png)
   ```

   Para `imagen2 con espacios.png`, usarías:

   ```markdown
   ![Imagen 2](imagenes/imagen2%20con%20espacios.png)
   ```

5. **Visualización:**
   Al visualizar tu fichero Markdown renderizado, las imágenes deberían aparecer correctamente si la ruta es correcta y el nombre del fichero está escrito correctamente.
