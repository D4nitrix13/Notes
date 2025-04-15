<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***El fichero `MANIFEST.in` es utilizado en proyectos de Python para especificar qué Ficheros adicionales deben ser incluidos en el paquete distribuible cuando se crea una distribución del proyecto. Este fichero se usa junto con `setup.py` y se encuentra en el directorio raíz del proyecto***

## ***Propósito del `MANIFEST.in`***

1. **Incluir Ficheros Adicionales:**
  *Permite incluir Ficheros que no están directamente en el árbol de directorios del proyecto pero que deben formar parte del paquete distribuible. Por ejemplo, Ficheros de documentación, Ficheros de configuración, o Ficheros de datos.*

2. **Excluir Ficheros:**
  *También se puede usar para excluir Ficheros específicos del paquete distribuible. Esto es útil para evitar incluir Ficheros temporales o no relevantes.*

### ***Sintaxis Básica***

**El fichero `MANIFEST.in` usa una sintaxis simple para definir qué Ficheros incluir o excluir. Aquí están algunos comandos comunes:**

- **`include`:** *Incluye Ficheros específicos en la distribución.*

  ```bash
  include ./README.*
  include ./setup.cfg
  ```

- **`exclude`:** *Excluye Ficheros específicos de la distribución.*

  ```bash
  exclude ./*.pyc
  ```

- **`recursive-include`:** *Incluye todos los Ficheros en un directorio específico, incluyendo subdirectorios.*
  - **Exclusiones específicas:** *Al usar recursive-exclude, se deben proporcionar tanto el directorio como un patrón de fichero (puede ser * para todos los ficheros).*

  ```bash
  recursive-include ./Package *.txt
  ```

- **`recursive-exclude`:** *Excluye todos los Ficheros en un directorio específico, incluyendo subdirectorios.*
  - **Exclusiones específicas:** *Al usar recursive-exclude, se deben proporcionar tanto el directorio como un patrón de fichero (puede ser * para todos los ficheros).*

  ```bash
  recursive-exclude ./Package *.pyc
  ```

- **`global-include`:** *Incluye todos los Ficheros que coincidan con el patrón especificado en todos los directorios.*

  ```bash
  global-include ./*.txt
  ```

- **`global-exclude`:** *Excluye todos los Ficheros que coincidan con el patrón especificado en todos los directorios.*

  ```bash
  global-exclude ./*.pyc
  ```

- **`prune`:** *Excluye directorios enteros de la distribución.*

  ```bash
  prune ./tests
  ```

### ***Ejemplo de `MANIFEST.in`***

**Aquí hay un ejemplo de un Fichero `MANIFEST.in`:**

```bash
include ./README.*
include ./LICENSE.*
recursive-include ./Package/data *
exclude ./Package/data/temp*
prune ./Package/tests
```

**En este ejemplo:**

- *Se incluyen `./README.*` y `./LICENSE.*` en el paquete distribuible.*
- *Se incluyen todos los Ficheros en el directorio `./Package/data`.*
- *Se excluyen los Ficheros en `./Package/data` que comienzan con `./temp`.*
- *Se excluye el directorio `./Package/tests` y todo su contenido.*

### ***En el fichero `MANIFEST.in`, los comentarios se realizan utilizando el símbolo `#`. Todo el texto que sigue a `#` en una línea es considerado un comentario y será ignorado por el procesador del Fichero. Los comentarios son útiles para añadir descripciones o anotaciones sobre las inclusiones y exclusiones que estás configurando.***

### ***Ejemplos de Comentarios en `MANIFEST.in`***

**Aquí tienes algunos ejemplos que muestran cómo usar comentarios en un Fichero `MANIFEST.in`:**

```bash
# Incluir el Fichero de documentación principal
include ./README.*

# Incluir la licencia del proyecto
include ./LICENSE.*

# Incluir todos los Ficheros de datos en el directorio 'data'
recursive-include ./Package/data *

# Excluir los Ficheros temporales del directorio 'data'
exclude ./Package/data/temp*

# Excluir el directorio de pruebas
prune ./Package/tests
```

### ***Uso de Comentarios***

1. **Explicaciones Generales:**
  *Puedes usar comentarios para proporcionar explicaciones generales sobre qué hace cada línea o bloque de configuraciones en el Fichero.*

   ```bash
   # Incluir Ficheros de configuración
   include ./*.cfg
   ```

2. **Notas sobre Excepciones:**
  *Los comentarios pueden ser útiles para documentar excepciones o condiciones especiales que se aplican a ciertas reglas de inclusión o exclusión.*

   ```bash
   # Excluir Ficheros temporales que podrían ser generados por el editor
   exclude ./*.tmp
   ```

3. **Desactivación Temporal de Líneas:**
  *Puedes comentar líneas temporales para desactivar su efecto sin eliminarlas del Fichero.*

   ```bash
   # Incluye ejemplos de scripts, pero está comentado temporalmente
   # recursive-include ./Examples *.py
   ```

*Recuerda que los comentarios no afectan la funcionalidad del Fichero `MANIFEST.in` y solo sirven para documentación y organización dentro del Fichero mismo.*

### ***Uso***

*Cuando se ejecuta un comando como `python setup.py sdist` o `python ./setup.py sdist`, el contenido del `MANIFEST.in` es utilizado para construir el paquete distribuible (tarball o zip), asegurando que todos los Ficheros necesarios estén incluidos y que los Ficheros no deseados sean excluidos.*
