<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git add" y "git commit"***

---

## ***Agregar cambios***

> [!NOTE]
> *Para agregar cambios a tu repositorio, primero necesitarás agregar los ficheros modificados al área de preparación con `git add`. Puedes agregar todos los ficheros modificados con `git add .`, o agregar ficheros específicos con `git add [nombre del fichero]`.*

```bash
git add .
```

```bash
git add ..
```

```bash
git add ./directory
```

```bash
git add fichero.py
```

**Para agregar todos los ficheros .py en el directorio actual y subdirectorios:**

```bash
git add *.py
```

## **`git commit`**

> *El comando `git commit` crea un nuevo commit con los cambios que has agregado al área de preparación. Un commit es como un "punto de control" en tu proyecto al que puedes volver más tarde si es necesario.*

```bash
git commit
```

### ***`git commit -m`***

> *La opción `-m` te permite especificar un mensaje de commit directamente en la línea de comandos. Esto es útil si tu cambio es lo suficientemente simple como para describirlo en una sola línea.*

```bash
git commit -m "Tu mensaje de commit aquí"
```

---

### ***`git commit --message=`***

> *La opción `--message=` es equivalente a `-m`. Te permite especificar un mensaje de commit directamente en la línea de comandos.*

```bash
git commit --message="Tu mensaje de commit aquí"
```

> [!IMPORTANT]
> *El comando `git add` se utiliza para agregar cambios al área de preparación antes de realizar un commit. Existen varias opciones interesantes que puedes usar con `git add` para personalizar cómo y qué cambios se añaden.*

---

## ***Opciones de `git add`***

1. **`<fichero>`**
   - **Función:** *Añade un fichero específico al área de preparación.*
   - **Uso:** *Ideal para agregar cambios de ficheros individuales.*
   - **Ejemplo:**

     ```bash
     git add fichero.txt
     ```

2. **`-A` o `--all`**
   - **Función:** *Añade todos los ficheros nuevos, modificados y eliminados al área de preparación.*
   - **Uso:** *Conveniente para asegurarte de que todos los cambios sean incluidos en el próximo commit.*
   - **Ejemplo:**

     ```bash
     git add -A
     ```

3. **`-u` o `--update`**
   - **Función:** *Añade solo los ficheros modificados y eliminados al área de preparación, pero no los ficheros nuevos.*
   - **Uso:** *Útil para preparar solo los cambios en ficheros existentes sin incluir nuevos ficheros.*
   - **Ejemplo:**

     ```bash
     git add -u
     ```

4. **`-p` o `--patch`**
   - **Función:** *Permite seleccionar interactivamente partes específicas de los cambios para agregar al área de preparación.*
   - **Uso:** *Ideal para hacer commits más detallados y específicos, eligiendo fragmentos de cambios.*
   - **Ejemplo:**

     ```bash
     git add -p
     ```

5. **`-i` o `--interactive`**
   - **Función:** *Inicia una sesión interactiva para agregar cambios.*
   - **Uso:** *Permite interactuar con Git para seleccionar cambios específicos o realizar otras operaciones en el área de preparación.*
   - **Ejemplo:**

     ```bash
     git add -i
     ```

6. **`-f` o `--force`**
   - **Función:** *Forza la adición de ficheros que están en `.gitignore`.*
   - **Uso:** *Útil si necesitas agregar ficheros que normalmente serían ignorados por las reglas de `.gitignore`.*
   - **Ejemplo:**

     ```bash
     git add -f fichero_ignorado.txt
     ```

7. **`--ignore-errors`**
   - **Función:** *Continúa agregando ficheros al área de preparación incluso si se encuentran errores.*
   - **Uso:** *Para evitar que errores detengan el proceso de adición de ficheros.*
   - **Ejemplo:**

     ```bash
     git add --ignore-errors .
     ```

8. **`-n` o `--dry-run`**
   - **Función:** *Muestra qué ficheros serían añadidos al área de preparación sin realmente agregarlos.*
   - **Uso:** *Permite verificar qué cambios se añadirán sin hacer cambios reales.*
   - **Ejemplo:**

     ```bash
     git add -n .
     ```

9. **`--verbose`**
   - **Función:** *Muestra información detallada sobre los ficheros que se están añadiendo al área de preparación.*
   - **Uso:** *Para obtener detalles adicionales durante el proceso de adición.*
   - **Ejemplo:**

     ```bash
     git add --verbose fichero.txt
     ```

10. **`<directorio>/`**
    - **Función:** *Añade todos los ficheros en un directorio específico al área de preparación.*
    - **Uso:** *Útil para agregar todos los ficheros de un directorio sin tener que listarlos individualmente.*
    - **Ejemplo:**

      ```bash
      git add directorio/
      ```

*Estas opciones te permiten personalizar la forma en que agregas cambios al área de preparación, facilitando un control más preciso sobre lo que se incluye en el próximo commit.*

---

### ***`Eliminar commits`***

*Hay varias formas de eliminar un commit en Git, dependiendo de tus necesidades y de si el commit que deseas eliminar ya ha sido compartido con otros o no. Aquí te muestro algunas formas comunes:*

1. **`git reset`:** *Puedes usar `git reset` para eliminar el commit y opcionalmente mover la rama hacia atrás en la historia. Ten en cuenta que esto puede eliminar el commit y deshacer los cambios locales, así que úsalo con precaución. Por ejemplo:*

   ```bash
   git reset --hard HEAD~1
   ```

   *Esto eliminará el último commit y todos los cambios asociados.*

2. **`git revert`:** *Esta opción crea un nuevo commit que revierte los cambios realizados en el commit que deseas eliminar. No modifica la historia existente, lo que la hace más segura si el commit ya ha sido compartido con otros. Por ejemplo:*

   ```bash
   git revert <ID_del_commit>
   ```

   *Esto creará un nuevo commit que deshace los cambios introducidos por el commit especificado.*

3. **`git rebase -i`:** *Puedes usar la opción interactiva de rebase para eliminar un commit. Esto te permite reescribir la historia de la rama. Por ejemplo:*

   ```bash
   git rebase -i HEAD~2
   ```

   *Esto abrirá un editor interactivo donde puedes elegir eliminar el commit.*

4. **`git cherry-pick`:** *Puedes usar `git cherry-pick` para seleccionar los cambios de otros commits y aplicarlos en una nueva rama, sin incluir el commit que deseas eliminar.*

5. **`git reset --soft`:** *Similar a `git reset --hard`, pero mantiene los cambios en el área de preparación (staging), lo que te permite modificar los ficheros y realizar un nuevo commit sin perder los cambios. Por ejemplo:*

   ```bash
   git reset --soft HEAD~1
   ```

   *Esto deshace el último commit pero mantiene los cambios en el área de preparación.*

6. **`git revert --no-commit`:** *Similar a `git revert`, pero no realiza un commit inmediato, lo que te permite realizar cambios adicionales antes de crear el commit de reversión. Por ejemplo:*

   ```bash
   git revert --no-commit <ID_del_commit>
   ```

   *Luego puedes hacer más cambios y luego hacer un commit cuando estés listo.*

- *Estas son algunas de las formas comunes de eliminar commits en Git. Cada método tiene sus propias implicaciones y es importante entender cómo afectarán a tu historial de commits y a cualquier colaborador que esté trabajando en el mismo repositorio.*

> [!NOTE]
> **Nota:** *Recuerda que los mensajes de commit deben ser descriptivos y significativos para ayudar a otros desarrolladores (o a ti mismo en el futuro) a entender qué cambios se realizaron en cada commit.*

Aquí tienes algunas opciones interesantes del comando `git commit`, que te permiten ajustar cómo registras cambios en tu repositorio:

---

<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git commit"***

> *El comando `git commit` se utiliza para guardar los cambios en el repositorio local. Existen varias opciones interesantes que puedes usar con `git commit` para personalizar el proceso de commit.*

---

## ***Opciones de `git commit`***

1. **`-m <mensaje>`**
   - **Función:** *Especifica el mensaje del commit en la línea de comandos, evitando abrir el editor de texto.*
   - **Uso:** *Útil para hacer commits rápidos con un mensaje corto.*
   - **Ejemplo:**

     ```bash
     git commit -m "Añadido nuevo fichero README"
     ```

2. **`-a` o `--all`**
   - **Función:** *Añade automáticamente todos los ficheros rastreados al commit.*
   - **Uso:** *Conveniente para hacer commits de todos los cambios en ficheros rastreados sin necesidad de hacer `git add` por separado.*
   - **Ejemplo:**

     ```bash
     git commit -a -m "Actualización de todos los ficheros rastreados"
     ```

3. **`-p` o `--patch`**
   - **Función:** *Permite hacer un commit interactivo para seleccionar partes específicas de los cambios para el commit.*
   - **Uso:** *Útil para hacer commits más granulares y detallados.*
   - **Ejemplo:**

     ```bash
     git commit -p
     ```

4. **`--amend`**
   - **Función:** *Modifica el último commit. Puedes agregar cambios adicionales al último commit o cambiar su mensaje.*
   - **Uso:** *Ideal para corregir errores o agregar cambios olvidados.*
   - **Ejemplo:**

     ```bash
     git commit --amend -m "Corrección del mensaje del commit"
     ```

5. **`--no-edit`**
   - **Función:** *Utiliza el mensaje del commit anterior cuando se usa `--amend`, sin abrir el editor de texto.*
   - **Uso:** *Práctico si solo quieres añadir cambios al último commit sin modificar su mensaje.*
   - **Ejemplo:**

     ```bash
     git commit --amend --no-edit
     ```

6. **`-v` o `--verbose`**
   - **Función:** *Muestra los cambios en el commit antes de confirmarlo.*
   - **Uso:** *Permite revisar los cambios que se van a incluir en el commit.*
   - **Ejemplo:**

     ```bash
     git commit -v
     ```

7. **`--signoff`**
   - **Función:** *Añade una línea `Signed-off-by` al mensaje del commit, indicando la aprobación del autor.*
   - **Uso:** *Requerido por algunas organizaciones para certificar que los cambios cumplen con las políticas de contribución.*
   - **Ejemplo:**

     ```bash
     git commit --signoff -m "Añadido soporte para nuevas funcionalidades"
     ```

8. **`--date <fecha>`**
   - **Función:** *Especifica una fecha para el commit.*
   - **Uso:** *Útil para establecer una fecha diferente en el commit, por ejemplo, al importar cambios históricos.*
   - **Ejemplo:**

     ```bash
     git commit --date="2024-07-01 12:00:00" -m "Commit con fecha específica"
     ```

9. **`--dry-run`**
   - **Función:** *Simula el commit sin realizarlo realmente.*
   - **Uso:** *Permite verificar qué cambios se incluirán en el commit sin efectuar el commit.*
   - **Ejemplo:**

     ```bash
     git commit --dry-run -m "Simulación de commit"
     ```

10. **`-n` o `--no-verify`**
    - **Función:** *Omite los hooks de pre-commit y pre-push.*
    - **Uso:** *Utilizado para hacer commits sin que se ejecuten los hooks que podrían prevenir el commit.*
    - **Ejemplo:**

      ```bash
      git commit -n -m "Commit sin ejecutar hooks"
      ```

*Estas opciones te permiten ajustar el comportamiento del comando `git commit` según tus necesidades y facilitar un flujo de trabajo más eficiente.*

### ***Ejemplo básico de `git rm`***

- **El comando `git rm` se utiliza para eliminar ficheros de tu índice de Git (staging area) y, opcionalmente, de tu directorio de trabajo. Aquí hay un ejemplo y una explicación de sus flags y para qué sirven:**

- **Supongamos que tienes un fichero llamado `fichero.txt` en tu repositorio y quieres eliminarlo:**

```bash
git rm fichero.txt
```

**Este comando hará lo siguiente:**

1. *Eliminará `fichero.txt` del índice de Git.*
2. *Eliminará `fichero.txt` del directorio de trabajo.*

### ***Flags comunes de `git rm`***

1. **`-f` o `--force`:**
   - *Si el fichero tiene cambios que no se han registrado (no commit), Git no permitirá eliminarlo sin esta opción. Usar `-f` o `--force` fuerza la eliminación.*

   ```bash
   git rm -f fichero.txt
   ```

2. **`--cached`:**
   - *Elimina el fichero del índice, pero lo deja en el directorio de trabajo. Esto es útil si deseas que el fichero ya no esté en seguimiento por Git pero quieres conservarlo en tu proyecto local.*

   ```bash
   git rm --cached fichero.txt
   ```

3. **`-r` o `--recursive`:**
   - *Permite eliminar directorios y sus contenidos recursivamente. Útil cuando necesitas eliminar varios ficheros o directorios a la vez.*

   ```bash
   git rm -r directorio/
   ```

4. **`-n` o `--dry-run`:**
   - *Muestra qué ficheros se eliminarían sin realizar ninguna acción. Útil para ver qué pasará sin hacer cambios reales.*

   ```bash
   git rm -n fichero.txt
   ```

### ***Ejemplo combinado***

**Si deseas eliminar un fichero del índice pero conservarlo en tu directorio de trabajo, forzar la eliminación y aplicar recursivamente:**

```bash
git rm --cached -f -r directorio/
```

### ***Resumen***

- **`git rm fichero.txt`:** *Elimina `fichero.txt` del índice y del directorio de trabajo.*
- **`git rm -f fichero.txt`:** *Fuerza la eliminación de `fichero.txt` incluso si tiene cambios no registrados.*
- **`git rm --cached fichero.txt`:** *Elimina `fichero.txt` del índice pero lo conserva en el directorio de trabajo.*
- **`git rm -r directorio/`:** *Elimina la directorio y su contenido recursivamente.*
- **`git rm -n fichero.txt`:** *Muestra qué ficheros se eliminarían sin realizar la acción.*

- *Con estos ejemplos y flags, puedes gestionar la eliminación de ficheros y directorios en tu repositorio de Git de manera efectiva.*
