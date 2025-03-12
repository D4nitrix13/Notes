<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git fetch" y "git pull"***

> *`git fetch` y `git pull` son dos comandos relacionados con la obtención de cambios desde un repositorio remoto, pero tienen algunas diferencias clave en cuanto a su funcionamiento.*

## ***`git fetch`:***

- *El comando `git fetch` descarga los últimos cambios del repositorio remoto a tu repositorio local, pero no los fusiona automáticamente con tu rama actual.*

- *Actualiza las referencias remotas (por ejemplo, `origin/main`) en tu repositorio local para que reflejen las referencias actuales del repositorio remoto.*

- *Los cambios descargados se almacenan en el repositorio local, pero no afectan tu trabajo actual.*

- *Te permite revisar los cambios antes de fusionarlos manualmente.*

---

### ***`git pull`:***

- *El comando `git pull` realiza dos acciones en una: primero, realiza un `git fetch` para obtener los últimos cambios del repositorio remoto, y luego realiza un `git merge` para fusionar automáticamente esos cambios en tu rama local.*

- *Es una forma rápida de obtener los últimos cambios del repositorio remoto y fusionarlos directamente en tu rama local.*

- *Si hay conflictos de fusión, Git intentará fusionar automáticamente los cambios si es posible. Si no es posible, te pedirá que resuelvas los conflictos manualmente.*

---

### ***Diferencias clave:***

- *`git fetch` solo descarga los cambios y actualiza las referencias remotas en tu repositorio local, sin fusionar automáticamente. Es útil si quieres revisar los cambios antes de fusionarlos.*

- *`git pull` realiza una fusión automática después de descargar los cambios, lo que puede ser conveniente si estás seguro de que quieres fusionar los cambios directamente en tu rama local.*

- **En resumen, si prefieres revisar los cambios antes de fusionarlos, utiliza `git fetch` seguido de un `git merge` o `git rebase`. Si estás seguro de que quieres fusionar los cambios directamente en tu rama local, puedes usar `git pull`.**

---

> [!IMPORTANT]
> *El comando `git fetch` se utiliza para obtener actualizaciones del repositorio remoto sin aplicarlas automáticamente a tu rama actual. Es una forma segura de ver los cambios en el remoto antes de decidir si integrarlos en tu trabajo local.*

---

## ***Opciones de `git fetch`***

1. **`<remoto>`**
   - **Función:** *Especifica el nombre del repositorio remoto del cual se deben obtener los cambios.*
   - **Uso:** *Para obtener actualizaciones de un repositorio remoto específico.*
   - **Ejemplo:**

     ```bash
     git fetch origin
     ```

2. **`<remoto> <rama>`**
   - **Función:** *Obtiene cambios para una rama específica del repositorio remoto.*
   - **Uso:** *Para obtener actualizaciones solo para una rama específica en lugar de todas las ramas.*
   - **Ejemplo:**

     ```bash
     git fetch origin main
     ```

3. **`--all`**
   - **Función:** *Obtiene cambios de todos los repositorios remotos configurados.*
   - **Uso:** *Para actualizar todas las referencias locales desde todos los remotos.*
   - **Ejemplo:**

     ```bash
     git fetch --all
     ```

4. **`--prune`**
   - **Función:** *Elimina las ramas remotas que han sido eliminadas en el repositorio remoto.*
   - **Uso:** *Para limpiar las referencias a ramas remotas que ya no existen.*
   - **Ejemplo:**

     ```bash
     git fetch --prune
     ```

5. **`--depth <n>`**
   - **Función:** *Obtiene solo los últimos `n` commits del repositorio remoto, creando una clonación superficial.*
   - **Uso:** *Para obtener una historia limitada y reducir el tamaño de la descarga.*
   - **Ejemplo:**

     ```bash
     git fetch --depth 1
     ```

6. **`--no-tags`**
   - **Función:** *No obtiene las etiquetas del repositorio remoto.*
   - **Uso:** *Para evitar la descarga de etiquetas si no son necesarias.*
   - **Ejemplo:**

     ```bash
     git fetch --no-tags
     ```

7. **`--tags`**
   - **Función:** *Obtiene todas las etiquetas del repositorio remoto.*
   - **Uso:** *Para actualizar todas las referencias de etiquetas desde el remoto.*
   - **Ejemplo:**

     ```bash
     git fetch --tags
     ```

8. **`--quiet` o `-q`**
   - **Función:** *Suprime la salida del comando para que solo se muestren los errores.*
   - **Uso:** *Para una salida menos detallada durante la actualización.*
   - **Ejemplo:**

     ```bash
     git fetch --quiet
     ```

9. **`--verbose` o `-v`**
   - **Función:** *Muestra información detallada sobre el proceso de obtención.*
   - **Uso:** *Para ver más detalles sobre qué cambios se están obteniendo.*
   - **Ejemplo:**

     ```bash
     git fetch --verbose
     ```

10. **`--no-recurse-submodules`**
    - **Función:** *No obtiene actualizaciones para submódulos.*
    - **Uso:** *Para evitar la actualización de submódulos si solo quieres obtener los cambios del repositorio principal.*
    - **Ejemplo:**

      ```bash
      git fetch --no-recurse-submodules
      ```

*Estas opciones te permiten personalizar la forma en que obtienes los cambios del repositorio remoto, proporcionando flexibilidad para manejar diferentes escenarios y necesidades.*
