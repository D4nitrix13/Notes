<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***El fichero `MANIFEST.in` es utilizado en proyectos de Python para especificar qué Ficheros adicionales deben ser incluidos en el paquete distribuible cuando se crea una distribución del proyecto. Este fichero se usa junto con `setup.py` y se encuentra en el directorio raíz del proyecto***

## *¿Por Qué Usar Rutas **Relativas** En `MANIFEST.in`?*

> [!NOTE]
> *El archivo `MANIFEST.in` es utilizado por `setuptools` para **incluir o excluir archivos en el paquete fuente** (`sdist`, o `source distribution`). Cuando escribes rutas en él, **se interpretan en relación al directorio raíz del proyecto**, es decir, el mismo directorio donde está ubicado tu `setup.py` o `pyproject.toml`.*

---

### *¿Qué pasa si usas rutas **con `./` o absolutas**?*

- *Escribir rutas como `README.md` o `/home/usuario/proyecto/README.md` **puede hacer que `setuptools` no encuentre los archivos**, porque:*
  - *`` no siempre se interpreta correctamente en todos los contextos (especialmente al construir desde otras rutas o dentro de entornos virtuales).*
  - *Las rutas **absolutas** son **ignoradas o consideradas inválidas**, ya que `MANIFEST.in` solo permite rutas relativas al proyecto.*

---

### **Cómo Deben Escribirse Las Rutas**

| **Incorrecto**                 | **Correcto**                   |
| ------------------------------ | ------------------------------ |
| *`include README.md`*          | *`include README.md`*          |
| *`recursive-include src *`*    | *`recursive-include src *`*    |
| *`recursive-exclude Themes *`* | *`recursive-exclude Themes *`* |

**Estas rutas funcionan correctamente porque:**

- *`README.md`, `src/`, `Themes/`, etc., están **dentro del árbol del proyecto**.*
- *No se necesita (ni se debe) anteponer ``.*

---

## **Recordatorio Clave**

> [!NOTE]
> **Todas las rutas en `MANIFEST.in` deben ser relativas al directorio raíz del proyecto.**

**Esto garantiza:**

- *Compatibilidad multiplataforma.*
- *Correcta inclusión de archivos durante el empaquetado con `python3 setup.py sdist` o `python3 -m build`.*
- *Ausencia de errores por rutas mal interpretadas.*

## ***Propósito del `MANIFEST.in`***

1. **Incluir Ficheros Adicionales:**
  *Permite incluir Ficheros que no están directamente en el árbol de directorios del proyecto pero que deben formar parte del paquete distribuible. Por ejemplo, Ficheros de documentación, Ficheros de configuración, o Ficheros de datos.*

2. **Excluir Ficheros:**
  *También se puede usar para excluir Ficheros específicos del paquete distribuible. Esto es útil para evitar incluir Ficheros temporales o no relevantes.*

### ***Sintaxis Básica***

**El fichero `MANIFEST.in` usa una sintaxis simple para definir qué Ficheros incluir o excluir. Aquí están algunos comandos comunes:**

- **`include`:** *Incluye Ficheros específicos en la distribución.*

  ```bash
  include README.*
  include setup.cfg
  ```

- **`exclude`:** *Excluye Ficheros específicos de la distribución.*

  ```bash
  exclude *.pyc
  ```

- **`recursive-include`:** *Incluye todos los Ficheros en un directorio específico, incluyendo subdirectorios.*
  - **Exclusiones específicas:** *Al usar recursive-exclude, se deben proporcionar tanto el directorio como un patrón de fichero (puede ser * para todos los ficheros).*

  ```bash
  recursive-include Package *.txt
  ```

- **`recursive-exclude`:** *Excluye todos los Ficheros en un directorio específico, incluyendo subdirectorios.*
  - **Exclusiones específicas:** *Al usar recursive-exclude, se deben proporcionar tanto el directorio como un patrón de fichero (puede ser * para todos los ficheros).*

  ```bash
  recursive-exclude Package *.pyc
  ```

- **`global-include`:** *Incluye todos los Ficheros que coincidan con el patrón especificado en todos los directorios.*

  ```bash
  global-include *.txt
  ```

- **`global-exclude`:** *Excluye todos los Ficheros que coincidan con el patrón especificado en todos los directorios.*

  ```bash
  global-exclude *.pyc
  ```

- **`prune`:** *Excluye directorios enteros de la distribución.*

  ```bash
  prune tests
  ```

### ***Ejemplo de `MANIFEST.in`***

**Aquí hay un ejemplo de un Fichero `MANIFEST.in`:**

```bash
include README.*
include LICENSE.*
recursive-include Package/data *
exclude Package/data/temp*
prune Package/tests
```

**En este ejemplo:**

- *Se incluyen `README.*` y `LICENSE.*` en el paquete distribuible.*
- *Se incluyen todos los Ficheros en el directorio `Package/data`.*
- *Se excluyen los Ficheros en `Package/data` que comienzan con `temp`.*
- *Se excluye el directorio `Package/tests` y todo su contenido.*

### ***En el fichero `MANIFEST.in`, los comentarios se realizan utilizando el símbolo `#`. Todo el texto que sigue a `#` en una línea es considerado un comentario y será ignorado por el procesador del Fichero. Los comentarios son útiles para añadir descripciones o anotaciones sobre las inclusiones y exclusiones que estás configurando.***

### ***Ejemplos de Comentarios en `MANIFEST.in`***

**Aquí tienes algunos ejemplos que muestran cómo usar comentarios en un Fichero `MANIFEST.in`:**

```bash
# Incluir el Fichero de documentación principal
include README.*

# Incluir la licencia del proyecto
include LICENSE.*

# Incluir todos los Ficheros de datos en el directorio 'data'
recursive-include Package/data *

# Excluir los Ficheros temporales del directorio 'data'
exclude Package/data/temp*

# Excluir el directorio de pruebas
prune Package/tests
```

### ***Uso de Comentarios***

1. **Explicaciones Generales:**
  *Puedes usar comentarios para proporcionar explicaciones generales sobre qué hace cada línea o bloque de configuraciones en el Fichero.*

   ```bash
   # Incluir Ficheros de configuración
   include *.cfg
   ```

2. **Notas sobre Excepciones:**
  *Los comentarios pueden ser útiles para documentar excepciones o condiciones especiales que se aplican a ciertas reglas de inclusión o exclusión.*

   ```bash
   # Excluir Ficheros temporales que podrían ser generados por el editor
   exclude *.tmp
   ```

3. **Desactivación Temporal de Líneas:**
  *Puedes comentar líneas temporales para desactivar su efecto sin eliminarlas del Fichero.*

   ```bash
   # Incluye ejemplos de scripts, pero está comentado temporalmente
   # recursive-include Examples *.py
   ```

*Recuerda que los comentarios no afectan la funcionalidad del Fichero `MANIFEST.in` y solo sirven para documentación y organización dentro del Fichero mismo.*

---

### **Comparación Entre Las Dos Formas**

1. **`*/.mypy_cache/*` y `*/__pycache__/*`**

   - **Significado:**
     - *El patrón `*/.mypy_cache/*` significa "excluir todos los directorios llamados `.mypy_cache` que se encuentren en **cualquier nivel** del árbol de directorios, pero solo a un nivel de profundidad".*
     - *Similarmente, `*/__pycache__/*` excluye los directorios `__pycache__` en cualquier nivel de profundidad, pero solo un nivel de subdirectorios.*

   - **Limitación:**
     - *Solo tiene en cuenta un nivel de subdirectorios, lo que significa que si tienes directorios con más de un nivel de subdirectorios (por ejemplo, `foo/bar/.mypy_cache`), **no los excluirá**.*

2. **`**/__pycache__/*` y `**/.mypy_cache/*`**

   - **Significado:**
     - *El patrón `**/__pycache__/*` significa "excluir todos los directorios llamados `__pycache__` que se encuentren **en cualquier nivel** de subdirectorios, sin importar cuántos niveles de profundidad haya".*
     - *De igual forma, `**/.mypy_cache/*` se aplica a cualquier directorio `.mypy_cache`, sin importar cuán profundo esté en el árbol.*

   - **Ventaja:**
     - **Recursión profunda:** *El uso de `**` permite excluir estos directorios **en todos los niveles del árbol de directorios** (independientemente de cuántos subdirectorios haya). Esto es útil para proyectos más grandes o complejos que podrían tener directorios anidados con estos nombres en niveles profundos.*

---

## **¿Cuál es mejor?**

- **Uso de `**`:**
  - **Más completo y preciso.** *Es **más robusto**, ya que cubre todos los niveles del árbol de directorios, garantizando que no queden archivos o directorios de caché en niveles más profundos.*
  - **Recomendado** *cuando estás trabajando en proyectos con estructuras de directorios complejas o si no estás seguro de cuántos niveles de directorios pueden existir en tu proyecto.*

- **Uso de `*/`:**
  - **Más limitado**. *Aunque puede funcionar en muchos proyectos simples, **no cubre todos los casos** posibles en estructuras complejas, donde los directorios `__pycache__` o `.mypy_cache` están en niveles más profundos.*

---

## **¿Qué significa el `**`?**

*El `**` es un **comodín recursivo** en las herramientas de `setuptools` que coincide con **todos los directorios** y **subdirectorios** en cualquier nivel. Es similar a cómo funciona en los sistemas de archivos o en los globbing de shells, pero en el contexto de `MANIFEST.in` se usa para hacer que la coincidencia sea **más profunda y extensa**.*

- **`**/__pycache__/*`:**
  - *Coincide con cualquier directorio `__pycache__`, independientemente de cuántos niveles de directorios haya antes de él.*
  - *Ejemplo de coincidencias: `./foo/__pycache__/`, `./bar/baz/__pycache__/`, `./a/b/c/d/__pycache__/`.*

- **Conclusión**

- **Si tu proyecto es simple** *y no tiene muchas subcarpetas anidadas, `*/__pycache__/*` puede ser suficiente.*
- **Si tu proyecto es más complejo** *y quieres asegurarte de excluir todos los directorios `__pycache__` o `.mypy_cache` en cualquier nivel del árbol de directorios, **usa `**/__pycache__/*`**. Es la opción **más robusta y flexible**.*

*En resumen, el uso de `**` es generalmente preferible, ya que te garantiza que **se excluyen todos los directorios** en cualquier nivel del árbol de directorios, lo cual es más seguro a largo plazo.*

---

### ***Uso***

*Cuando se ejecuta un comando como `python setup.py sdist` o `python setup.py sdist`, el contenido del `MANIFEST.in` es utilizado para construir el paquete distribuible (tarball o zip), asegurando que todos los Ficheros necesarios estén incluidos y que los Ficheros no deseados sean excluidos.*
