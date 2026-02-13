<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***La librería `argparse` en Python es una herramienta poderosa para manejar argumentos de línea de comandos en programas. Te permite definir qué argumentos acepta tu programa, proporcionar descripciones y mensajes de ayuda, y manejar los valores de los argumentos de manera eficiente. A continuación, te explico cómo funciona `argparse` y sus parámetros y métodos más comunes.***

## ***Introducción a `argparse`***

*`argparse` es una librería estándar en Python que facilita la creación de interfaces de línea de comandos. Permite definir qué argumentos acepta el programa y cómo deben ser interpretados.*

### ***Clases y Métodos Principales***

#### ***1. `ArgumentParser`***

**La clase `ArgumentParser` es el punto de entrada para definir y manejar los argumentos de línea de comandos.**

**Parámetros de `ArgumentParser`:**

- **`prog`:** *Nombre del programa que se usará en los mensajes de ayuda. Por defecto, es el nombre del script.*
- **`description`:** *Descripción del programa que se mostrará en la ayuda.*
- **`add_help`:** *Un booleano que indica si se debe añadir la opción `-h/--help` automáticamente a la ayuda. Por defecto, es `True`.*
- **`epilog`:** *Texto adicional que se muestra después de la ayuda.*
- **`exit_on_error`:** *Un booleano que determina si el programa debe salir con un error en caso de argumentos incorrectos. Por defecto, es `True`.*

**Ejemplo:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import exit
from argparse import ArgumentParser

parser: ArgumentParser = ArgumentParser(
    prog = "Mi_Programa",
    description = "Este es un programa de ejemplo.",
    epilog = "Texto adicional al final de la ayuda.",
    exit_on_error = True,
    add_help = True
)

exit(0)
```

#### ***2. `.add_argument()`***

*Este método se usa para agregar un argumento que el programa puede aceptar. Acepta varios parámetros para configurar el comportamiento del argumento.*

**Parámetros de `.add_argument()`:**

- **`name_or_flags`:** *El nombre o nombres del argumento (como `--input` o `-i`).*
- **`dest`:** *Nombre del atributo del `Namespace` que almacenará el valor del argumento.*
- **`nargs`:** *Número de argumentos que se deben consumir. Puede ser:*
  - *Un número entero que indica cuántos argumentos se deben consumir.*
  - *`'?'` para indicar un argumento opcional.*
  - *`'*'` para consumir cualquier número de argumentos.*
  - *`'+'` para consumir uno o más argumentos.*
- **`type`:** *Tipo de dato que el argumento debe ser convertido. Por ejemplo, `int`, `float`, `str`.*
- **`required`:** *Booleano que indica si el argumento es obligatorio. Por defecto, es `False`.*
- **`help`:** *Descripción del argumento que se muestra en la ayuda.*
- **`metavar`:** *Nombre que se mostrará en la ayuda en lugar del nombre real del argumento.*
- **`action`:** *Define cómo se debe manejar el argumento. Por ejemplo:*
  - *`'store'`: Almacena el valor del argumento (por defecto).*
  - *`'store_true'`: Almacena `True` si el argumento está presente.*
  - *`'store_false'`: Almacena `False` si el argumento está presente.*
  - *`'append'`: Añade el valor al final de una lista.*

**Ejemplo:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from argparse import ArgumentParser
from sys import exit
parser: ArgumentParser = ArgumentParser(description = "Programa de ejemplo")

parser.add_argument(
    "-i", "--input",            # Nombres del argumento
    dest = "input_file",          # Nombre del atributo en el Namespace
    nargs = 1,                    # Número de argumentos esperados
    type = str,                   # Tipo de dato del argumento
    required = True,              # Argumento obligatorio
    help = "Fichero de entrada",  # Descripción del argumento
    metavar = "FICHERO"           # Nombre en la ayuda
)

parser.add_argument(
    "--verbose",                # Nombres del argumento
    action = "store_true",        # Almacena True si el argumento está presente
    help = "Mostrar salida detallada"  # Descripción del argumento
)
exit(0)
```

#### ***3. `.print_help()`***

*Este método imprime el mensaje de ayuda en el fichero especificado o en `stderr` por defecto.*

**Ejemplo:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from argparse import ArgumentParser
from sys import stderr, exit

parser: ArgumentParser = ArgumentParser(description = "Programa de ejemplo")
parser.add_argument("-i", "--input", required = True, help = "Fichero de entrada")
parser.print_help(file = stderr)
exit(1)
```

#### ***4. `.parse_args()`***

Este método analiza los argumentos de línea de comandos y devuelve un objeto `Namespace` con los argumentos como atributos.

**Ejemplo:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from argparse import ArgumentParser, Namespace
from sys import stdout, exit

parser: ArgumentParser = ArgumentParser(description = "Programa de ejemplo")
parser.add_argument("-i", "--input", required = True, help = "Fichero de entrada")
args: Namespace = parser.parse_args()

print(args.input, end = "\n", file = stdout)  # Imprime el valor del argumento --input
exit(0)
```

### ***Resumen de Opciones***

- **`name_or_flags`:** *Nombres de los argumentos (e.g., `--input`, `-i`).*
- **`dest`:** *Nombre del atributo en el objeto `Namespace`.*
- **`nargs`:** *Número de argumentos que se deben consumir.*
- **`type`:** *Tipo de dato del argumento.*
- **`required`:** *Indica si el argumento es obligatorio.*
- **`help`:** *Descripción del argumento.*
- **`metavar`:** *Nombre en la ayuda.*
- **`action`:** *Define cómo se maneja el argumento.*

### ***Documentación y Recursos***

- **[Documentación Oficial de `argparse`](https://docs.python.org/3/library/argparse.html "https://docs.python.org/3/library/argparse.html"):** *Información detallada sobre `argparse` y sus opciones.*

**En resumen, `argparse` es una herramienta flexible y potente para gestionar argumentos de línea de comandos en Python, permitiendo una configuración detallada y personalizada de los argumentos que tu programa acepta.**
