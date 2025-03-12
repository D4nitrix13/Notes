<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Subida de un proyecto a GitHub"***

> *Para subir un proyecto a GitHub, sigue estos pasos:*

---

## ***1. Crea un repositorio en GitHub:***

1. *Inicia sesión en tu cuenta de GitHub.*

2. *Haz clic en el botón "New" en la esquina superior derecha de la página.*

3. *Completa la información del repositorio (nombre, descripción, público/privado).*

4. *Haz clic en "Create repository" para crear el repositorio.*

---

### ***2. Inicializa un repositorio local en tu proyecto:***

> *Si aún no tienes un repositorio Git en tu proyecto, inicialízalo ejecutando el siguiente comando en el directorio raíz de tu proyecto:*

```bash
git init
```

---

### ***3. Agrega los ficheros al repositorio:***

> *Agrega los ficheros de tu proyecto al área de preparación utilizando el comando `git add`. Por ejemplo, para agregar todos los ficheros, puedes usar:*

```bash
git add .
```

---

### ***4. Realiza un commit de tus cambios:***

> *Crea un commit con los ficheros que has agregado al área de preparación utilizando el comando `git commit`. Incluye un mensaje descriptivo que explique los cambios que has realizado. Por ejemplo:*

```bash
git commit -m "Initial commit"
```

---

### ***5. Conecta tu repositorio local con el repositorio remoto en GitHub:***

- *Usa el siguiente comando para agregar la URL del repositorio remoto de GitHub como "origin" (esto es comúnmente lo que se hace por defecto al clonar un repositorio, pero si has inicializado tu repositorio localmente sin clonar, necesitarás hacer esto manualmente):*

```bash
git remote add origin <URL_Repository>
```

- *Reemplaza `<URL_Repository>` con la URL del repositorio que creaste en GitHub.*

---

### ***6. Sube tu proyecto a GitHub:***

- *Finalmente, utiliza el comando `git push` para enviar tus cambios al repositorio remoto en GitHub:*

```bash
git push -u origin main
```

- *Si estás trabajando en una rama diferente, reemplaza `main` con el nombre de tu rama.*

---

### ***7. Verifica tu repositorio en GitHub:***

> *Después de subir tus cambios, visita tu repositorio en GitHub para verificar que los ficheros se hayan cargado correctamente.*

- *¡Listo! Tu proyecto ahora está en GitHub y puedes compartirlo con otros colaboradores, seguir su progreso y realizar un seguimiento de las versiones utilizando Git y GitHub.*
