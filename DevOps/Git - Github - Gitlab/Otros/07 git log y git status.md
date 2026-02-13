<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git log" y "git status"***

---

## ***`git status`***

> *El comando `git status` muestra el estado del repositorio actual. Te informa sobre los cambios que se han realizado pero aún no se han confirmado (commit), así como los cambios que se han confirmado pero aún no se han enviado (push) al repositorio remoto.*

```bash
git status
```

---

## ***`git log`***

> *El comando `git log` muestra un historial de todos los commits que se han realizado en el repositorio. Cada commit se muestra con su hash de commit, el autor, la fecha y el mensaje de commit.*

```bash
git log
```

### **`git log --oneline -n 1`**

> *Esta es una variante del comando `git log` que muestra cada commit en una sola línea, lo que puede hacer que el historial sea más fácil de leer. La opción `-n 1` limita la salida a solo el último commit.*

```bash
git log --oneline -n 1
```

```bash
git log --all -n 1
```

```bash
git log --all --oneline
```

```bash
git log --all
```

```bash
git log --full-history
```

```bash
git log
```

```bash
git ls-tree -r --name-only <commit>
```

```bash
git ls-tree -r --name-only <rama>
```

---

### ***`git ls-tree -r --name-only <commit>` o `git ls-tree -r --name-only <rama>`***

- *Este comando lista el contenido de los árboles de objetos en el formato especificado ya sea mostrar los ficheros y directorios agregados en una rama especifica la opcion `--name-only` sirve para ver solo el nombre del fichero.*

---

## ***`git reflog`***

> *El comando `git reflog` muestra un historial de todas las acciones que han cambiado la HEAD. Es útil si necesitas rastrear cambios que no están asociados con commits, como los merges o los resets.*

```bash
git reflog
```

> [!IMPORTANT]
> *El comando `git log` muestra el historial de commits en tu repositorio, permitiendo revisar los cambios realizados a lo largo del tiempo. Puedes usar diversas opciones para personalizar cómo se presenta esta información.*

---

## ***Opciones de `git log`***

1. **`--oneline`**
   - **Función:** *Muestra cada commit en una sola línea.*
   - **Uso:** *Para obtener una vista compacta del historial de commits.*
   - **Ejemplo:**

     ```bash
     git log --oneline
     ```

2. **`--graph`**
   - **Función:** *Dibuja un gráfico ASCII que representa el historial de ramas y merges.*
   - **Uso:** *Para visualizar la estructura de ramas y merges de forma gráfica.*
   - **Ejemplo:**

     ```bash
     git log --graph
     ```

3. **`--decorate`**
   - **Función:** *Muestra las referencias (tags, ramas) junto con los commits.*
   - **Uso:** *Para ver en qué rama o etiqueta se encuentra cada commit.*
   - **Ejemplo:**

     ```bash
     git log --decorate
     ```

4. **`--stat`**
   - **Función:** *Muestra un resumen de los cambios en cada commit, incluyendo el número de ficheros modificados y las líneas añadidas/eliminadas.*
   - **Uso:** *Para ver un resumen estadístico de los cambios en el historial.*
   - **Ejemplo:**

     ```bash
     git log --stat
     ```

5. **`--patch` o `-p`**
   - **Función:** *Muestra el contenido de los cambios realizados en cada commit.*
   - **Uso:** *Para ver las diferencias completas (diffs) introducidas por cada commit.*
   - **Ejemplo:**

     ```bash
     git log --patch
     ```

6. **`--author=<autor>`**
   - **Función:** *Filtra los commits por autor específico.*
   - **Uso:** *Para ver los commits realizados por un autor determinado.*
   - **Ejemplo:**

     ```bash
     git log --author="Daniel Perez"
     ```

7. **`--since=<fecha>` y `--until=<fecha>`**
   - **Función:** *Filtra los commits realizados después de una fecha (`--since`) o antes de una fecha (`--until`).*
   - **Uso:** *Para limitar los commits a un rango de fechas específico.*
   - **Ejemplo:**

     ```bash
     git log --since="2024-01-01" --until="2024-01-31"
     ```

8. **`--grep=<texto>`**
   - **Función:** *Busca commits que contengan un texto específico en el mensaje del commit.*
   - **Uso:** *Para encontrar commits relacionados con un término específico.*
   - **Ejemplo:**

     ```bash
     git log --grep="fix bug"
     ```

9. **`--pretty=<formato>`**
   - **Función:** *Controla el formato de salida del log.*
   - **Uso:** *Para personalizar cómo se muestra la información de los commits. Puedes usar formatos predefinidos o crear uno personalizado.*
   - **Ejemplo:**

     ```bash
     git log --pretty=format:"%h - %an, %ar : %s"
     ```

10. **`--reverse`**
    - **Función:** *Muestra los commits en el orden inverso, comenzando con el commit más antiguo.*
    - **Uso:** *Para ver el historial desde el inicio hasta el final.*
    - **Ejemplo:**

      ```bash
      git log --reverse
      ```

11. **`--abbrev-commit`**
    - **Función:** *Muestra los identificadores de commits de forma abreviada.*
    - **Uso:** *Para ver identificadores de commits más cortos y manejables.*
    - **Ejemplo:**

      ```bash
      git log --abbrev-commit
      ```

12. **`--relative-date`**
    - **Función:** *Muestra las fechas de los commits en formato relativo (ej. "2 weeks ago").*
    - **Uso:** *Para ver fechas en términos relativos en lugar de fechas absolutas.*
    - **Ejemplo:**

      ```bash
      git log --relative-date
      ```

*Estas opciones te permiten ajustar cómo visualizas y filtras el historial de commits en tu repositorio, ayudándote a obtener la información que necesitas de manera más eficiente.*

---

> [!IMPORTANT]
> *El comando `git status` muestra el estado actual del directorio de trabajo y del área de preparación (staging area) en un repositorio Git. Te permite ver qué cambios han sido añadidos al área de preparación, cuáles están pendientes de ser confirmados y otros detalles importantes.*

---

## ***Opciones de `git status`***

1. **`--short` o `-s`**
   - **Función:** *Muestra el estado en un formato resumido, con una representación concisa de los cambios.*
   - **Uso:** *Para obtener una vista rápida del estado de los ficheros en el repositorio.*
   - **Ejemplo:**

     ```bash
     git status --short
     ```

2. **`--branch`**
   - **Función:** *Muestra información adicional sobre la rama actual, como la relación con la rama remota y el estado de los commits.*
   - **Uso:** *Para obtener detalles sobre la rama activa y su sincronización con el repositorio remoto.*
   - **Ejemplo:**

     ```bash
     git status --branch
     ```

3. **`--untracked-files`**
   - **Función:** *Controla la visibilidad de los ficheros no rastreados. Puede ser `no`, `normal`, o `all` para ajustar la cantidad de información mostrada sobre ficheros no rastreados.*
   - **Uso:** *Para ajustar cómo se muestran los ficheros no rastreados en el estado.*
   - **Ejemplo:**

     ```bash
     git status --untracked-files=all
     ```

4. **`--ignored`**
   - **Función:** *Muestra ficheros ignorados por `.gitignore` junto con el estado.*
   - **Uso:** *Para ver también los ficheros que están siendo ignorados en el directorio de trabajo.*
   - **Ejemplo:**

     ```bash
     git status --ignored
     ```

5. **`--verbose`**
   - **Función:** *Muestra información más detallada sobre el estado del repositorio.*
   - **Uso:** *Para obtener más detalles sobre los cambios y el estado de los ficheros.*
   - **Ejemplo:**

     ```bash
     git status --verbose
     ```

6. **`--porcelain`**
   - **Función:** *Muestra la salida en un formato estable y fácil de analizar por scripts.*
   - **Uso:** *Para obtener una salida que sea consistente y fácil de procesar por herramientas automáticas.*
   - **Ejemplo:**

     ```bash
     git status --porcelain
     ```

7. **`--show-stash`**
   - **Función:** *Muestra la información de los stashes en el estado del repositorio.*
   - **Uso:** *Para ver si hay stashes pendientes en el repositorio.*
   - **Ejemplo:**

     ```bash
     git status --show-stash
     ```

8. **`--no-optional-locks`**
   - **Función:** *Evita el uso de bloqueos opcionales en el proceso de estado.*
   - **Uso:** *Para mejorar el rendimiento o evitar conflictos con otros procesos que puedan estar accediendo al repositorio.*
   - **Ejemplo:**

     ```bash
     git status --no-optional-locks
     ```

*Estas opciones te permiten personalizar cómo se muestra el estado del repositorio, adaptándolo a tus necesidades y preferencias. Puedes combinar diferentes opciones para obtener la vista más útil para ti.*
