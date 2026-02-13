<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Explicación detallada con comentarios en el código sobre cómo usar la librería `tomllib` en Python para manejar ficheros TOML. Primero, vamos a instalar la librería `tomllib` (que es parte del estándar en Python `3.11` y posteriores, por lo que no necesitas instalarla por separado en estas versiones). Para versiones anteriores a Python `3.11`, puedes usar `toml` o `pytoml` que son librerías de terceros***

> [!NOTE]
> **[Recurso](https://realpython.com/python311-tomllib/ "https://realpython.com/python311-tomllib/")**

## ***Instalación***

*Para Python `3.11` y versiones posteriores, no necesitas instalar nada adicional porque `tomllib` es parte de la biblioteca estándar.*

**Para versiones anteriores de Python, puedes instalar la librería `toml` usando pip:**

```bash
pip install toml
```

### ***Ejemplo de uso con `tomllib` (Python `3.11`+)***

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Importamos el módulo tomllib que está disponible en Python `3.11` y versiones posteriores
from io import BufferedReader
from sys import stdout
from tomllib import load # type: ignore
from typing import Any, Dict, Optional

# Ejemplo de cómo cargar un fichero TOML
# Supongamos que tenemos un fichero llamado 'config.toml' con el siguiente contenido:
# [settings]
# theme = "dark"
# version = 1.0

# Abrimos y leemos el fichero TOML
f: Optional[BufferedReader] = None

with open(file = r'config.toml', mode = 'rb') as f:
    # Usamos tomllib.load para cargar el contenido del fichero en un diccionario
    config: Dict[str, Any] = load(f)

# Imprimimos el contenido cargado
print(config, end = "\n", file = stdout)

# Ejemplo de cómo acceder a los datos cargados
print(config['settings']['theme'], end = "\n", file = stdout)  # Debería imprimir 'dark'

# Output
# {'settings': {'theme': 'dark', 'version': 1.0}}
exit(0)
```

### ***Ejemplo de uso con `toml` (versiones anteriores a Python `3.11`)***

**Si estás utilizando una versión de Python anterior a la `3.11`, usa la librería `toml`. Aquí están los ejemplos con esta librería.**

**Fichero: `config.toml`**

```toml
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Ejemplo de cómo cargar un fichero TOML
# Supongamos que tenemos un fichero llamado 'config.toml' con el siguiente contenido:
[settings]
theme = "dark"
version = 1.0
```

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Importamos el módulo toml
from sys import stdout, exit
from typing import Any, Dict
from toml import load

# Ejemplo de cómo cargar un fichero TOML
# Supongamos que tenemos un fichero llamado 'config.toml' con el siguiente contenido:
# [settings]
# theme = "dark"
# version = 1.0

# Abrimos y leemos el fichero TOML
config: Dict[str, Any] = load(f = r"config.toml")

# Imprimimos el contenido cargado
print(config, end = "\n", file = stdout)
# Output
# {'settings': {'theme': 'dark', 'version': 1.0}}

# Ejemplo de cómo acceder a los datos cargados
print(config['settings']['theme'], end = "\n", file = stdout)  # Debería imprimir 'dark'
exit(1)
```

### ***Métodos y Excepciones***

- **`load()`:** *Carga el contenido de un fichero objeto en formato TOML en un diccionario.*
- **`loads()`:** *Carga el contenido de una cadena en formato TOML en un diccionario.*
- **`dump()`:** *Escribe el diccionario en formato TOML en un fichero objeto.*
- **`dumps()`:** *Serializa el diccionario a una cadena en formato TOML.*

**Ejemplo de `dump` y `dumps` con `toml`:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from io import TextIOWrapper
from typing import Dict, Optional, Union
from toml import dump, dumps
from sys import stdout, exit
# Creamos un diccionario para ser guardado en formato TOML
data: Dict[str, Dict[str, Union[str, float]]] = {
    "settings": {
        "theme": "dark",
        "version": 1.0
    }
}

# Ejemplo de cómo escribir el diccionario en un fichero TOML
f: Optional[TextIOWrapper] = None
with open(file = r"new_config.toml", mode = "w") as f:
    dump(o = data, f = f)

# Ejemplo de cómo convertir el diccionario a una cadena TOML
tomlString: str = dumps(o = data)
print(tomlString, end="\n", file = stdout)  # Imprimirá el contenido TOML como una cadena
exit(1)
```

- **`TomlDecodeError`:** *Se lanza cuando hay un error al decodificar un fichero o cadena TOML.*

**Ejemplo de manejo de `TomlDecodeError`:**

**Fichero: `malformed_config.toml`**

```toml
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

[settings -> Malo]
theme = Mal formateado
version = 1.0 Numero Flotante
```

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stderr, exit, stdout
from typing import Any, Dict
from toml import load
from toml.decoder import TomlDecodeError

try:
    # Intentamos cargar un fichero TOML malformado
    config: Dict[str, Any] = load(f = r"malformed_config.toml")
except TomlDecodeError as e:
    # Capturamos y mostramos el error de decodificación
    print(f'Error al decodificar el fichero TOML: {e}', end = "\n", file = stderr)
    exit(1)

print(config, end = "\n", file = stdout)
exit(0)
```
