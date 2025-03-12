<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git branch" y "git switch"***

> *`git branch` y `git switch` son dos comandos utilizados en Git para trabajar con ramas. Sin embargo, cumplen diferentes funciones.*

---

## ***`git branch`***

> *El comando `git branch` se utiliza para crear, listar, renombrar y eliminar ramas en tu repositorio. Aquí están algunas de sus funciones más comunes:*

- ***Crear una nueva rama:** `git branch <nombre_rama>`*

- ***Listar ramas:** `git branch`*

- ***Eliminar una rama:** `git branch -d <nombre_rama>`*

- ***Cambiar el nombre de una rama:** `git branch -m <nombre_actual> <nuevo_nombre>`*

**Por ejemplo, para crear una nueva rama llamada `feature`, usarías:**

```bash
git branch feature
```

**Para listar las ramas disponibles en un repositorio Git, puedes usar uno de los siguientes comandos:**

### ***1. Listar ramas locales***

**Para ver todas las ramas locales en tu repositorio:**

```bash
git branch
```

### ***2. Listar ramas remotas***

*Para ver todas las ramas remotas en tu repositorio:*

```bash
git branch -r
```

### ***3. Listar todas las ramas (locales y remotas)***

**Para ver todas las ramas, tanto locales como remotas:**

```bash
git branch -a
```

### ***4. Listar ramas con detalles***

**Para ver las ramas locales con detalles adicionales, como la última confirmación en cada rama:**

```bash
git branch -vv
```

- *Cada uno de estos comandos te proporciona diferentes niveles de detalle sobre las ramas en tu repositorio. Elige el que mejor se adapte a tus necesidades.*

### `git switch`

> *El comando `git switch`, introducido en Git 2.23, se utiliza para cambiar entre ramas o para crear y cambiar a una nueva rama en una sola operación. Algunas de sus funciones son:*

- **Cambiar a una rama existente:** `git switch <nombre_rama>`

- **Crear y cambiar a una nueva rama:** `git switch -c <nombre_nueva_rama>`

**Por ejemplo, para cambiar a la rama `feature`, usarías:**

```bash
git switch feature
```

**Para crear una nueva rama llamada `new-feature` y cambiar a ella, usarías:**

```bash
git switch -c new-feature
```

- *A partir de Git 2.23, `git switch` es preferido sobre `git checkout` para cambiar de rama, ya que `git switch` proporciona una interfaz más clara y segura para esta operación.*

- *En resumen, `git branch` se utiliza para operaciones relacionadas con ramas, como crear, listar, renombrar y eliminar, mientras que `git switch` se utiliza específicamente para cambiar entre ramas o para crear y cambiar a una nueva rama en una sola operación.*

### ***El gran Espacio en blanco que veas es típico en la visualización de la salida del comando `git branch -a` cuando usas paginación. Aquí está una explicación de las causas y cómo solucionarlo:***

### ***Causas del Espacio en Blanco***

1. **Paginación Automática:**
   - *Git, al igual que muchas herramientas de línea de comandos, usa un paginador (como `less` o `more`) para mostrar la salida de comandos que tienen muchas líneas. Este paginador agrega espacio en blanco cuando no hay más líneas que mostrar, o cuando la salida es más corta que la pantalla.*

2. **Configuración del Paginador:**
   - *El paginador por defecto puede estar configurado para mostrar espacios adicionales si no hay más contenido para mostrar.*

### ***Cómo Controlar o Eliminar el Espacio en Blanco***

1. **Deshabilitar el Paginador:**
   - *Puedes deshabilitar el paginador para que la salida se muestre directamente sin paginación. Utiliza el siguiente comando para ver la salida sin paginador:*

     ```bash
     git --no-pager branch -a
     ```

2. **Configuración del Paginador:**
   - *Puedes ajustar la configuración del paginador en Git. Para evitar la paginación, puedes cambiar la configuración global de Git para que no use el paginador para ciertos comandos:*

     ```bash
     git config --global core.pager cat
     ```

   - *Esto hará que Git utilice `cat` para mostrar la salida en lugar de un paginador, eliminando el espacio en blanco.*

3. **Uso de `less`:**
   - *Si `less` está configurado como tu paginador, puedes utilizar opciones como `-F` (para salir automáticamente si el contenido cabe en una pantalla) y `-X` (para desactivar el modo de visualización de pantalla completa):*

     ```bash
     git config --global core.pager "less -F -X"
     ```

4. **Salida Redirigida:**
   - *También puedes redirigir la salida a un fichero o usar otros comandos para procesarla sin paginación. Por ejemplo, para redirigir la salida a un fichero:*

     ```bash
     git branch -a > ramas.txt
     ```

   - *Luego puedes revisar el fichero `ramas.txt` para ver la salida sin paginación.*

**Las opciones `-F` y `-X` son parámetros que puedes usar con el paginador `less` para controlar su comportamiento. Aquí está lo que hacen:**

### ***Opciones de `less`***

1. **`-F` (o `--quit-if-one-screen`)**
   - **Función:** *Hace que `less` salga automáticamente si la salida cabe en una sola pantalla.*
   - **Uso:** *Si el contenido que estás visualizando no excede el tamaño de la pantalla, `less` terminará y devolverá el control a la línea de comandos sin esperar una entrada adicional del usuario.*

   **Ejemplo:**

   ```bash
   less -F fichero.txt
   ```

   *Si `fichero.txt` tiene menos líneas que la altura de la terminal, `less` cerrará automáticamente después de mostrar el fichero.*

2. **`-X` (o `--no-init`)**
   - **Función:** *Desactiva el modo de inicialización de la pantalla que `less` utiliza para borrar la pantalla al comenzar.*
   - **Uso:** *Evita que `less` limpie el contenido de la pantalla antes de mostrar la salida, lo que puede ser útil si prefieres mantener el contenido previo visible en la terminal.*

   **Ejemplo:**

   ```bash
   less -X fichero.txt
   ```

   *Al usar `-X`, `less` no borrará la pantalla cuando termine, lo que te permitirá ver el contenido previo.*

### ***Uso Combinado***

**Cuando usas `less` con ambos parámetros `-F` y `-X`, obtienes el siguiente comportamiento:**

- **`-F`:** *Si la salida cabe en una sola pantalla, `less` se cerrará automáticamente después de mostrar el contenido.*
- **`-X`:** *`less` no borrará la pantalla antes de mostrar el contenido y mantendrá el contenido visible después de salir.*

**Ejemplo de uso combinado:**

```bash
less -F -X fichero.txt
```

### ***Aplicación en Git***

**Cuando configuras Git para usar `less` con estos parámetros:**

```bash
git config --global core.pager "less -F -X"
```

**Esto hace que la salida de los comandos de Git que utilizan paginación se comporte de la siguiente manera:**

- **`-F`:** *Git saldrá automáticamente del paginador si la salida cabe en una sola pantalla.*
- **`-X`:** *Git no borrará la pantalla cuando termine de mostrar la salida, manteniendo el contenido visible en la terminal.*

*Esto puede ayudarte a evitar el gran espacio en blanco al visualizar salidas cortas, mejorando la experiencia de usuario en la terminal.*

### ***Resumen***

*El gran espacio en blanco es causado por la paginación automática de Git para manejar salidas largas. Puedes evitar este espacio en blanco deshabilitando el paginador, ajustando su configuración, o redirigiendo la salida a otro formato.*
