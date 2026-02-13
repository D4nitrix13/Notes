<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Aquí tienes algunas buenas prácticas en Git que pueden ayudarte a mantener tu flujo de trabajo ordenado y eficiente***

1. **Commits atómicos:** *Realiza commits que representen cambios coherentes y atómicos. Cada commit debe abordar una única funcionalidad, corrección de errores o cambio lógico.*

2. **Mensajes de commit descriptivos:** *Escribe mensajes de commit claros y descriptivos que expliquen qué cambios introduces y por qué. Utiliza un formato consistente, como el estilo imperativo ("Agrega", "Corrige", "Actualiza") y limita la longitud de las líneas a 50-72 caracteres.*

3. **Ramas significativas:** *Utiliza ramas para trabajar en nuevas funcionalidades o correcciones de errores. Mantén nombres de ramas descriptivos y coherentes con el trabajo que contienen.*

4. **Fusiones regulares:** *Fusiona con frecuencia los cambios de la rama principal en tu rama de trabajo para mantenerla actualizada y prevenir conflictos mayores más adelante.*

5. **Resolución de conflictos oportuna:** *Resuelve los conflictos de fusión tan pronto como aparezcan para evitar complicaciones posteriores y mantener un flujo de trabajo fluido.*

6. **Uso de `.gitignore`:** *Utiliza el fichero `.gitignore` para ignorar ficheros y directorios que no deben ser versionados, como ficheros generados automáticamente, dependencias de paquetes y ficheros de configuración local.*

7. ***Revisión de cambios antes de confirmar:** Revisa tus cambios utilizando `git diff` antes de confirmarlos para asegurarte de que estás incluyendo todos los cambios deseados y no estás introduciendo cambios no deseados.*

8. **Pruebas unitarias y de integración:** *Implementa pruebas unitarias y de integración para validar tus cambios antes de confirmarlos, garantizando que tu código funcione correctamente y no cause regressions en el código existente.*

9. **Uso de tags:** *Utiliza tags para marcar versiones importantes de tu proyecto, como versiones estables o lanzamientos de producción.*

10. **Documentación:** *Documenta tu código y tus decisiones de diseño para que otros miembros del equipo puedan entender fácilmente tu trabajo y colaborar eficientemente.*

*Al seguir estas buenas prácticas, puedes mejorar la calidad de tu trabajo, facilitar la colaboración con otros desarrolladores y mantener un historial de cambios limpio y comprensible en tu repositorio de Git.*

---

## ***Submódulos en Git***

> *Los submódulos en Git permiten incluir un repositorio dentro de otro repositorio. Esto es útil cuando deseas incluir un proyecto dentro de otro como una dependencia, pero mantenerlos separados para facilitar el desarrollo y la colaboración.*

---

### ***Cómo agregar un submódulo:***

1. ***Clonar el repositorio padre:***

   ```bash
   git clone <url_repositorio_padre>
   ```

2. ***Agregar el submódulo:***

   ```bash
   git submodule add <url_repositorio_submodulo> <ruta_destino>
   ```

   *Esto agregará el submódulo al repositorio padre en la ruta especificada.*

3. ***Confirmar los cambios:***

   ```bash
   git commit -m "Agrega submódulo"
   ```

4. ***Actualizar submódulo:***

   ```bash
   git submodule update --init --recursive
   ```

   *Esto descarga el contenido del submódulo y lo coloca en la ubicación especificada.*

---

### ***Git Hooks***

- *Los ganchos de Git son scripts personalizados que se ejecutan automáticamente en ciertos eventos, como antes o después de realizar un commit, push, merge, etc.*

---

#### ***Ejemplo de un gancho pre-commit:***

```bash
#!/bin/sh
echo "Ejecutando pre-commit hook..."
# Agregar aquí tus comprobaciones y acciones
```

*Este script se ejecutaría automáticamente antes de realizar un commit.*

---

### ***Git Bisect:***

- *Git Bisect es una herramienta que te ayuda a encontrar el commit que introdujo un determinado problema en tu código. Funciona realizando una búsqueda binaria en el historial de commits para identificar el commit responsable.*

---

#### ***Uso de Git Bisect:***

1. ***Inicializar la búsqueda:***

   ```bash
   git bisect start
   ```

2. ***Indicar un commit bueno y malo:***

   ```bash
   git bisect good <commit_bueno>
   git bisect bad <commit_malo>
   ```

3. ***Marcar los commits restantes como buenos o malos:***

   - *Git te indicará automáticamente un commit y debes indicar si es bueno o malo. Repite este paso hasta que Git identifique el commit responsable.*

   - *Para continuar con el proceso de bisect después de que Git haya seleccionado una revisión intermedia para que la pruebes, sigue estos pasos:*

    1. **Si la revisión seleccionada es buena (no contiene el problema que estás buscando), ejecuta el siguiente comando para informar a Git que la revisión es buena:**

         ```bash
         git bisect good
         ```

    2. **Si la revisión seleccionada es mala (contiene el problema que estás buscando), ejecuta el siguiente comando para informar a Git que la revisión es mala:**

         ```bash
         git bisect bad
         ```

    3. **Git seleccionará automáticamente la próxima revisión intermedia para que la pruebes y te proporcionará el hash de esa revisión junto con su mensaje de confirmación. Repite el proceso probando esa revisión y marcándola como buena o mala según corresponda.**

    4. **Continúa repitiendo los pasos 1-3 hasta que Git encuentre la revisión exacta que introdujo el problema.**

4. ***Finalizar la búsqueda:***

   ```bash
   git bisect reset
   ```

   *Este comando restablecerá tu repositorio a su estado original antes de comenzar el proceso de bisect, dejándote en la revisión en la que - estabas antes de iniciar la bisect.*

---

### ***Documentación:***

> *Es importante documentar estos procesos en el fichero README.md de tu repositorio para que los miembros del equipo puedan entender cómo funcionan y cómo utilizarlos. Puedes proporcionar ejemplos de código y capturas de pantalla para una mejor comprensión. Además, puedes crear directorios adicionales dentro del repositorio para almacenar scripts de ganchos y submódulos, y documentar su propósito y uso en ficheros README.md dentro de esas directorios.*

---

### ***Submódulos en Git:***

> *Supongamos que estás desarrollando un proyecto principal llamado "Proyecto A" y necesitas incluir una biblioteca externa llamada "BibliotecaX" en tu proyecto. En lugar de copiar y pegar la biblioteca en tu repositorio, puedes usar submódulos.*

1. ***Agregar el submódulo:***

   ```bash
   git submodule add https://github.com/usuario/BibliotecaX biblioteca_x
   ```

    ```bash
   git submodule add https://github.com/usuario/BibliotecaX.git biblioteca_x
   ```

   *Esto agregará la biblioteca como un submódulo en tu repositorio en la directorio `biblioteca_x`.*

   - *En Git, la extensión .git al final de la URL del repositorio es opcional y no afecta al funcionamiento del comando git submodule add. Ambas formas de la URL funcionarán igualmente bien y agregarán el repositorio como un submódulo en tu proyecto.*

   - *Para listar los submódulos en un repositorio de Git y para realizar otras operaciones relacionadas con submódulos, puedes utilizar una serie de comandos. Aquí tienes algunos de los comandos más comunes:*

    1. ***Listar submódulos:***

         ```bash
         git submodule
         ```

         - *Este comando lista todos los submódulos presentes en el repositorio, junto con la ruta y el hash de confirmación del submódulo.*

    2. ***Inicializar submódulos después de la clonación:***

         ```bash
         git submodule update --init
         ```

         - *Este comando inicializa todos los submódulos presentes en el repositorio después de la clonación.*

    3. ***Clonar un repositorio con sus submódulos:***

         ```bash
         git clone --recursive <URL_Repository>
         ```

       - *Este comando clona un repositorio y automáticamente inicializa y actualiza todos los submódulos contenidos en él.*

    4. ***Actualizar submódulos:***

      ```bash
      git submodule update --remote
      ```

    - *Este comando actualiza todos los submódulos a las versiones más recientes.*

    1. ***Agregar un submódulo:***

         ```bash
         git submodule add <URL_del_submódulo> <ruta_de_destino>
         ```

         - *Este comando agrega un nuevo submódulo al repositorio en la ruta especificada.*

    2. ***Eliminar un submódulo:***

         ```bash
         git submodule deinit -f <ruta_del_submódulo>
         git rm -f <ruta_del_submódulo>
         rm -rf .git/modules/<ruta_del_submódulo>
         ```

         ```bash
         git submodule deinit -f <ruta_del_submódulo>
         ```

         ```bash
         git rm -f <ruta_del_submódulo>
         ```

         ```bash
         rm -rf .git/modules/<ruta_del_submódulo>
         ```

         **Claro, aquí tienes una explicación detallada de cada comando relacionado con la eliminación de submódulos en Git:**

    3. ***`git submodule deinit -f <ruta_del_submódulo>`:***

    - *Este comando se utiliza para desinicializar un submódulo en el repositorio.*

    - *La opción `-f` o `--force` se utiliza para forzar la desinicialización del submódulo, incluso si hay cambios pendientes o no se puede
    desinicializar de forma limpia.*

    - *`<ruta_del_submódulo>` especifica la ruta del submódulo que se desea desinicializar.*

    1. **`*git rm -f <ruta_del_submódulo>`:***

    - *Este comando se utiliza para eliminar un submódulo del árbol de trabajo y del índice del repositorio.*

    - *La opción `-f` o `--force` se utiliza para forzar la eliminación del submódulo, incluso si hay cambios pendientes o no se puede eliminar de forma limpia.*

    - *`<ruta_del_submódulo>` especifica la ruta del submódulo que se desea eliminar.*

    1. **`rm *-rf .git/modules/<ruta_del_submódulo>`:***

    - *Este comando se utiliza para eliminar el directorio del submódulo dentro del directorio `.git/modules` del repositorio.*

    - *Eliminar este directorio es necesario para limpiar completamente el repositorio de cualquier referencia al submódulo eliminado.*

    - *`<ruta_del_submódulo>` especifica la ruta del submódulo para la cual se eliminará el directorio dentro de `.git/modules`.*

    - *En resumen, estos comandos se utilizan juntos para eliminar completamente un submódulo de un repositorio Git. Primero, `git submodule deinit -f` desinicializa el submódulo, luego `git rm -f` lo elimina del árbol de trabajo y del índice, y finalmente `rm -rf` elimina el directorio del submódulo dentro de `.git/modules`.*

    - *Estos comandos eliminan un submódulo del repositorio.*

    1. ***Clonar o actualizar un submódulo de forma recursiva:***

    ```bash
    git submodule update --init --recursive
    ```

    - *Este comando inicializa y actualiza de forma recursiva todos los submódulos presentes en el repositorio.*

    1. ***Obtener el estado de un submódulo:***

        ```bash
        git submodule status
        ```

        - *Este comando muestra el estado de todos los submódulos, incluyendo el hash de confirmación actual.*

        - *Estos son solo algunos de los comandos más utilizados para trabajar con submódulos en Git. Hay más comandos y opciones disponibles para realizar operaciones más avanzadas. Puedes consultar la documentación oficial de Git para obtener más detalles y opciones sobre el manejo de submódulos.*

2. ***Confirmar los cambios:***

   ```bash
   git commit -m "Agrega BibliotecaX como submódulo"
   ```

3. ***Actualizar submódulo:***

   ```bash
   git submodule update --init --recursive
   ```

---

### ***Git Hooks:***

**Supongamos que quieres asegurarte de que ningún fichero `.txt` se incluya en los commits. Puedes usar un gancho pre-commit para verificar esto.**

1. ***Crear un gancho pre-commit:***

   **Creas un fichero llamado `pre-commit` en la directorio `.git/hooks` dentro de tu repositorio con el siguiente contenido:**

   ```bash
   #!/bin/sh
   if git diff --cached --name-only | grep '\.txt$' > /dev/null; then
       echo "Error: No se permiten ficheros .txt en los commits."
       exit 1
   fi
   ```

   *Esto evitará que se realice un commit si hay ficheros `.txt` en la etapa de preparación.*

---

### ***Git Bisect***

- *Supongamos que tienes un bug en tu proyecto y sabes que estaba funcionando bien hace unos días, pero no estás seguro de cuál commit lo introdujo.*

1. ***Inicializar la búsqueda:***

   ```bash
   git bisect start
   ```

2. ***Indicar un commit bueno y malo:***

   ```bash
   git bisect good 2b6a7e1  # Commit bueno
   git bisect bad 4c74b3f   # Commit malo
   ```

3. ***Marcar los commits restantes:***

   - *Git te proporcionará automáticamente un commit y debes decirle si es bueno o malo. Repite esto hasta que Git identifique el commit responsable.*

4. ***Finalizar la búsqueda:***

   ```bash
   git bisect reset
   ```

---

### ***`.gitmodules`***

- *El fichero `.gitmodules` es un fichero de configuración utilizado por Git para almacenar información sobre los submódulos dentro de un repositorio. Cada entrada en este fichero representa un submódulo en el repositorio principal e incluye información como la ruta del submódulo dentro del repositorio, su URL remota y cualquier configuración adicional relevante.*

**En tu ejemplo específico:**

```bash
[submodule "prueba"]
    path = prueba
    url = https://github.com/user/repository
```

- *`[submodule "prueba"]`: Esta línea indica el inicio de la configuración para un submódulo llamado "prueba". Especifica que las siguientes líneas de configuración se aplicarán a este submódulo en particular.*

- *`path = prueba`: Esta línea especifica la ruta dentro del repositorio principal donde se encuentra el submódulo. En este caso, el submódulo se encontrará en un directorio llamado "prueba" dentro del repositorio principal.*

- *`url = https://github.com/user/repository`: Esta línea especifica la URL remota del repositorio del submódulo. Indica la ubicación desde la cual el submódulo será clonado cuando se inicialice en el repositorio principal.*

- *En resumen, el fichero `.gitmodules` es esencial para mantener la información necesaria sobre los submódulos en un repositorio Git. Permite que Git gestione los submódulos de manera adecuada y automática, facilitando su clonación y actualización dentro del repositorio principal.*

*Estos son ejemplos de cómo usar submódulos, ganchos de Git y Git Bisect en situaciones reales para mejorar tu flujo de trabajo y mantener la calidad de tu código.*
