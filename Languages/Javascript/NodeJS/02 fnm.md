<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Ejemplos de Uso de FNM***

**1. Listar versiones disponibles para instalación:**

*Para ver las versiones de Node.js que puedes instalar con `fnm`, puedes usar los comandos `list-remote`, `ls-remote`, `list` o `ls`. Aquí utilizaremos `list` como ejemplo:*

```bash
fnm list-remote
```

- *Esto mostrará una lista de todas las versiones de Node.js disponibles para su instalación desde los repositorios remotos.*

**2. Listar versiones instaladas localmente:**

- *Para ver las versiones de Node.js que ya tienes instaladas en tu sistema, puedes usar `fnm list` o `fnm ls`:*

```bash
fnm list
```

- *Esto te mostrará las versiones de Node.js que tienes instaladas localmente, marcando con un asterisco (`*`) la versión actualmente activa.*

- *Cuando ejecutas el comando `fnm list`, estás solicitando a FNM que te muestre todas las versiones de Node.js que están instaladas en tu sistema y cuál de ellas está marcada como la versión por defecto ("default"). Además, mostrará con un asterisco (`*`) la versión que está actualmente activa en tu entorno.*

**El resultado de `fnm list` puede verse así:**

```bash
* system
12.22.1
14.17.0
```

**En este ejemplo:**

- **`* system`:** *Esto indica que actualmente estás utilizando la versión de Node.js del sistema (la que se instaló sin utilizar FNM).*
- **`12.22.1` y `14.17.0`:** *Estas son versiones específicas de Node.js que has instalado usando FNM.*

- *El asterisco (`*`) indica cuál de estas versiones está activa en tu sesión actual de terminal. Si ves `* system`, significa que estás utilizando la versión de Node.js que no fue gestionada por FNM (posiblemente instalada a través del gestor de paquetes de tu sistema operativo).*

## ***Significado de "system"***

- *Cuando `fnm list` muestra "`* system`", se refiere a la versión de Node.js que está configurada como la predeterminada o la que se utiliza fuera del control de FNM. Esto puede ser la versión instalada globalmente en tu sistema operativo antes de que comenzaras a usar FNM para gestionar las versiones de Node.js.*

- *En resumen, "`* system`" en `fnm list` indica que estás utilizando la versión de Node.js del sistema operativo, no gestionada por FNM. Esto puede ser útil para saber qué versión de Node.js es la predeterminada si no has establecido una versión específica con FNM o si necesitas comparar con las versiones gestionadas por FNM.*

**3. Instalar una versión específica de Node.js:**

**Para instalar una versión específica de Node.js, utiliza el comando `install` seguido de la versión que deseas instalar:**

```bash
fnm install 14.17.0
```

**Esto instalará la versión `14.17.0 de Node.js` en tu sistema.**

**4. Usar una versión específica de Node.js:**

**Para cambiar la versión de Node.js que estás utilizando actualmente, usa el comando `use` seguido de la versión que deseas usar:**

```bash
fnm use 14.17.0
```

- *Esto cambiará la versión activa de Node.js a la 14.17.0.*

**5. Establecer una versión predeterminada de Node.js:**

**Puedes establecer una versión predeterminada de Node.js para que se utilice por defecto en nuevas sesiones de terminal con el comando `default`:**

```bash
fnm default 14.17.0
```

- *Esto establecerá la versión 14.17.0 como la versión predeterminada de Node.js.*

**6. Ver la versión actual de Node.js en uso:**

**Para ver la versión de Node.js que está actualmente activa y en uso, puedes usar `current`:**

```bash
fnm current
```

- *Este comando mostrará la versión de Node.js que está configurada como activa en tu sesión actual de terminal.*

**7. Desinstalar una versión de Node.js:**

**Para eliminar una versión específica de Node.js de tu sistema, utiliza el comando `uninstall` seguido de la versión que deseas eliminar:**

```bash
fnm uninstall 14.17.0
```

- *Esto eliminará la versión 14.17.0 de Node.js de tu sistema.*

**8. Obtener ayuda sobre los comandos disponibles:**

**Si necesitas más información sobre los comandos disponibles y sus opciones, puedes usar el comando `help`:**

```bash
fnm help
```

```bash
fnm --help
```

- *Esto te proporcionará información detallada sobre cómo usar `fnm` y sus diferentes subcomandos.*

- *Estos ejemplos te dan una idea de cómo puedes utilizar `fnm` para gestionar fácilmente las versiones de Node.js en tu sistema. Cada comando te proporciona flexibilidad para trabajar con múltiples versiones y administrarlas según las necesidades de tu proyecto.*

```bash
fnm install 20.15.0
Installing Node v20.15.0 (x64)
00:00:05 ███████████████████████████████████████████████████████████████████████████ 24.43 MiB/24.43 MiB (4.66 MiB/s, 0s)
```

```bash
fnm alias 20.15.0 default
```

```bash
fnm list
* v20.15.0 default
* system
```
