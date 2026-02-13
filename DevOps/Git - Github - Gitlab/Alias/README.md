<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git alias"***

> *En Git, puedes definir alias para abreviar comandos comunes o incluso crear comandos personalizados. Estos alias pueden ser globales, locales o de sistema, y se configuran de diferentes maneras.*

1. **Alias Globales:** *Estos alias se aplican a todos los repositorios de Git en tu sistema.*

   *Para configurar alias globales, puedes usar el siguiente comando en tu terminal:*

   ```bash
   git config --global alias.<Name Alias> <Command Git>
   ```

   **Por ejemplo, para crear un alias global llamado `co` para `checkout`, usarías:**

   ```bash
   git config --global alias.co checkout
   ```

2. **Alias Locales:** *Estos alias se aplican solo al repositorio en el que se definen.*

   *Para configurar alias locales, puedes editar directamente el fichero `.git/config` dentro del repositorio y agregar secciones de alias, o puedes usar el siguiente comando en tu terminal dentro del repositorio:*

   ```bash
   git config alias.<Name Alias> <Command Git>
   ```

   ```bash
   git config --local alias.<Name Alias> <Command Git>
   ```

   **Por ejemplo:**

   ```bash
   git config alias.lg "log --oneline --decorate"
   ```

   ```bash
   git config --local alias.lg "log --oneline --decorate"
   ```

3. **Alias de Sistema:** *Estos alias se aplican a todos los repositorios en tu sistema y son definidos por el administrador del sistema.*

   **Los alias de sistema se definen editando el fichero de configuración de Git en el sistema, generalmente ubicado en `~/.gitconfig`.**

   **Por ejemplo, para agregar un alias de sistema llamado `ci` para `commit`, agregarías lo siguiente al fichero `/~/.gitconfig`:**

   ```toml
   [init]
        defaultBranch = master
   [core]
        editor = code --wait
   [user]
        name = Danielperezdev13
        email = 161483842+D4nitrix13@users.noreply.github.com
   ```

    **Aquí hay una breve explicación de las secciones y configuraciones:**

    1. *`[init]`*: *Esta sección contiene configuraciones relacionadas con la inicialización de nuevos repositorios. En este caso, has especificado que el nombre de la rama predeterminada para los nuevos repositorios será `master`.*

    2. *`[core]`*: *Esta sección contiene configuraciones globales para Git Core. Has especificado que tu editor predeterminado para los mensajes de confirmación será Visual Studio Code con la opción `--wait`, que espera a que se cierre la ventana de edición antes de continuar.*

    3. *`[user]`*: *Esta sección contiene información de identificación del usuario que será utilizada en los commits. Has configurado tu nombre de usuario como "Danielperezdev13" y tu dirección de correo electrónico asociada a tu cuenta de GitHub.*

    *Esta configuración es típica y comúnmente utilizada. Te permite personalizar tu entorno de Git de acuerdo a tus preferencias, como tu editor preferido y la información de identificación que quieres que se adjunte a tus commits.*

```bash
git log --oneline --all --graph --pretty=format:"%C(auto)%h%d %s %C(black)%C(bold)%cr"
```

`git log --oneline --all --graph --pretty=format:"%C(auto)%h%d %s %C(black)%C(bold)%cr"`:

- *Este comando muestra un historial de confirmaciones en una sola línea, incluyendo todos los ramas (`--all`) y representando gráficamente las relaciones entre las confirmaciones (`--graph`). La opción `--pretty=format` permite especificar un formato de salida personalizado. En este caso, `%C(auto)%h%d %s %C(black)%C(bold)%cr` formatea la salida para mostrar el hash de la confirmación (`%h`), los nombres de los ramas (`%d`), el mensaje de la confirmación (`%s`), y la fecha relativa (`%cr`) en negrita (`%C(black)%C(bold)`).*

---

## ***Para añadirle un alias***

```bash
git config alias.lg "log --oneline --all --graph --pretty=format:'%C(auto)%h%d %s %C(black)%C(bold)%cr'"
```

```bash
git config --local alias.lg "log --oneline --all --graph --pretty=format:'%C(auto)%h%d %s %C(black)%C(bold)%cr'"
```

```bash
git config --global alias.lg "log --oneline --all --graph --pretty=format:'%C(auto)%h%d %s %C(black)%C(bold)%cr'"
```

> *La opción `--pretty=format` en Git te permite personalizar el formato de salida de los resultados de varios comandos, como `git log`. Esta opción te da un control detallado sobre qué información mostrar y cómo formatearla.*

*Aquí están todas las opciones de formato que puedes utilizar dentro de `--pretty=format`:*

- **`%H`:** *Hash completo de la confirmación.*

- **`%h`:** *Hash corto de la confirmación.*

- **`%T`:** *Hash del árbol.*

- **`%t`:** *Hash corto del árbol.*

- **`%P`:** *Hashes de padres.*

- **`%p`:** *Hashes de padres abreviados.*

- **`%an`:** *Nombre del autor.*

- **`%aN`:** *Nombre del autor (nombre completo).*

- **`%ae`:** *Correo electrónico del autor.*

- **`%aE`:** *Correo electrónico del autor (nombre completo).*

- **`%ad`:** *Fecha de autoría (fecha).*

- **`%aD`:** *Fecha de autoría (formato de git blame).*

- **`%ar`:** *Fecha de autoría (relativa).*

- **`%at`:** *Fecha de autoría (formato UNIX timestamp).*

- **`%ai`:** *Fecha de autoría (formato ISO 8601).*

- **`%aI`:** *Fecha de autoría (formato ISO 8601, formato de git blame).*

- **`%cn`:** *Nombre del comisor.*

- **`%cN`:** *Nombre del comisor (nombre completo).*

- **`%ce`:** *Correo electrónico del comisor.*

- **`%cE`:** *Correo electrónico del comisor (nombre completo).*

- **`%cd`:** *Fecha de comisión (fecha).*

- **`%cD`:** *Fecha de comisión (formato de git blame).*

- **`%cr`:** *Fecha de comisión (relativa).*

- **`%ct`:** *Fecha de comisión (formato UNIX timestamp).*

- **`%ci`:** *Fecha de comisión (formato ISO 8601).*

- **`%cI`:** *Fecha de comisión (formato ISO 8601, formato de git blame).*

- **`%d`:** *Nombres de las ramas que contienen la confirmación.*

- **`%e`:** *Correo electrónico del autor (parecido a `%ae`).*

- **`%s`:** *Mensaje de la confirmación.*

- **`%f`:** *Referencia de nombres de confirmación.*

- **`%b`:** *Mensaje de la confirmación, excepto el título.*

- **`%B`:** *Mensaje de la confirmación, excepto el título, con comentario.*

- **`%N`:** *Nombre del campo en el formato de git notes.*

- **`%n`:** *Separador de línea.*

- **`%%`:** *Porcentaje literal.*

- *Puedes combinar estos marcadores de formato y otros caracteres para crear un formato personalizado que se adapte a tus necesidades. Por ejemplo, `%h` muestra el hash corto, `%an` muestra el nombre del autor, `%s` muestra el mensaje de la confirmación y `%cr` muestra la fecha relativa.*

- *Además, puedes aplicar formato a la salida utilizando códigos de color ANSI y otros atributos de texto. Esto te permite resaltar ciertas partes de la salida para mejorar la legibilidad o la visualización.*

- *Por ejemplo, puedes utilizar `%C(color)%s%C(reset)` para colorear el mensaje de la confirmación. `color` sería el nombre del color que deseas aplicar (por ejemplo, `red` para rojo, `green` para verde, etc.) y `reset` se utiliza para restablecer el color después del marcador de formato.*

- *La opción `auto` también es útil para permitir que Git elija automáticamente los colores dependiendo del contexto.*

- *En resumen, `--pretty=format` te da una gran flexibilidad para controlar cómo se muestra la salida de los comandos de Git, lo que puede ser útil para personalizar la visualización del historial de confirmaciones, por ejemplo, en `git log`.*

- *Recuerda que los alias son simplemente abreviaturas para comandos de Git y no crean nuevos comandos por sí mismos. Puedes usarlos como si fueran comandos Git estándar en tu terminal después de configurarlos.*
