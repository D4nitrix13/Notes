<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***`colored` es una librería de Python que permite añadir colores y estilos a la salida en la consola. Es útil para mejorar la visibilidad de la salida del programa, especialmente cuando se trata de logs, mensajes de error, o simplemente para hacer la interfaz más atractiva.***

> [!NOTE]
> **[Recurso](https://dslackw.gitlab.io/colored/user_guide/user_guide/ "https://dslackw.gitlab.io/colored/user_guide/user_guide/")**

## ***Instalación***

**Para usar `colored`, primero necesitas instalarlo. Puedes hacerlo usando `pip`:**

```bash
pip install colored
```

### ***Uso Básico***

**A continuación, te muestro cómo usar `colored` para aplicar colores y estilos a textos en la consola.**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout
from colored import Fore, Back, Style

# Definir colores y estilos
red: str  = Fore.RED
green: str  = Fore.GREEN
yellow: str  = Fore.YELLOW
blue: str  = Fore.BLUE
reset: str  = Style.reset

# Definir fondos
bgRed: str  = Back.RED
bgGreen: str  = Back.GREEN

# Estilos
bold: str = Style.bold
underline: str = Style.underline

# Crear mensajes con colores y estilos
message1: str = f"{red}Este texto es rojo{reset}"
message2: str = f"{green}{bold}Este texto es verde y negrita{reset}"
message3: str = f"{yellow}{underline}Este texto es amarillo y subrayado{reset}"
message4: str = f"{blue}{bgRed}Texto azul con fondo rojo{reset}"

# Imprimir los mensajes
print(message1, end = "\n", file = stdout)
print(message2, end = "\n", file = stdout)
print(message3, end = "\n", file = stdout)
print(message4, end = "\n", file = stdout)
exit(0)
```

### ***Explicación del Código***

1. **Importar la Librería:**
   - `from colored import Fore, Back, Style` *importa las funciones necesarias para definir colores de texto, fondos y estilos.*

2. **Definir Colores y Estilos:**
   - **Colores de Texto:** `Fore.RED`, `Fore.GREEN`, `Fore.YELLOW`, `Fore.BLUE` *definen colores para el texto.*
   - **Fondos:** `Back.RED`, `Back.GREEN` *definen colores para el fondo del texto.*
   - **Estilos:** `Style.bold`, `Style.underline` *definen estilos como negrita y subrayado.*
   - **Restablecer:** `Style.reset` *se usa para restablecer el estilo y color al valor predeterminado.*

3. **Crear Mensajes:**
   - *Se crean mensajes aplicando los colores y estilos definidos.*

4. **Imprimir Mensajes:**
   - *Se imprimen los mensajes con los estilos aplicados.*

### ***Ejemplo Avanzado***

**Aquí hay un ejemplo más avanzado que utiliza `colored` para imprimir una tabla estilizada:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import List, Union
from colored import Fore, Back, Style # type: ignore
from sys import stdout, exit
# Definir colores y estilos
headerColor: str = Fore.WHITE + Back.BLUE + Style.bold
dataColor: str = Fore.BLACK + Back.WHITE
reset: str = Style.reset

# Definir datos
headers: List[str] = ["Nombre", "Edad", "Ciudad"]
data: List[List[Union[str, int]]] = [
    ["Danna", 30, "Nueva York"],
    ["Benjamin", 25, "San Francisco"],
    ["Charlie", 35, "Los Ángeles"]
]

# Crear tabla estilizada
print(f"{headerColor}{' | '.join(headers)}{reset}", end = "\n", file = stdout)
print("-" * 40, end = "\n", file = stdout)  # Línea de separación
row: Union[List[Union[str, int]], None] = None
for row in data:
    print(f"{dataColor}{' | '.join(map(lambda i: str(i), row))}{reset}", end = "\n", file = stdout)
    # Sintax Sugar
    # print(f"{dataColor}{' | '.join(map(str, row))}{reset}", end = "\n", file = stdout)

"""
El error que ves se debe a que `mypy`, una herramienta de comprobación de tipos para Python, no puede encontrar información de tipos para el módulo `colored`. Cuando `mypy` analiza tu código, busca ficheros de tipo (`.pyi`) o marcadores (`py.typed`) que proporcionen información sobre los tipos en módulos externos. Si no puede encontrar estos ficheros o marcadores, emite un error como el que estás viendo.

### ¿Por qué añadir `# type: ignore`?

Añadir `# type: ignore` es una forma de decirle a `mypy` que ignore los errores de tipo en una línea específica de código. Esto es útil cuando sabes que el código es correcto y no deseas que `mypy` muestre errores sobre módulos que no tienen información de tipos disponible.

### Ejemplo de Problema

En nuestro caso, `mypy` se queja de que no puede analizar el módulo `colored` porque falta información de tipos. Esto es común con algunas bibliotecas que no proporcionan sus propios ficheros de tipo ni tienen una compatibilidad completa con `mypy`.

### Cómo Resolver el Problema

#### 1. **Ignorar el Error Específico**

Puedes añadir `# type: ignore` al final de la línea que está causando el error. Esto le dice a `mypy` que ignore los errores de tipo en esa línea.

from colored import fore, back, style  # type: ignore

#### 2. **Proporcionar Información de Tipos Manualmente**

Si quieres ser más específico, puedes crear un fichero de tipo personalizado para proporcionar información sobre los tipos de la biblioteca. Este es un enfoque más avanzado y generalmente se utiliza si el fichero de tipo existente no cubre todos los casos necesarios.

#### 3. **Agregar una Configuración en `mypy.ini`**

Puedes configurar `mypy` para ignorar los módulos sin tipo globalmente. Esto se hace en el fichero de configuración `mypy.ini`:

[mypy]
ignore_missing_imports = True

Esta configuración ignorará todos los módulos que no tienen información de tipos, lo cual puede ser útil si trabajas con muchos módulos de este tipo.

### Ejemplo Avanzado

Aquí tienes un ejemplo más completo del código con `# type: ignore` añadido:

#!/usr/bin/env python3

from sys import stdout, exit
from colored import fore, back, style  # type: ignore

# Definir colores y estilos
red: str = fore.RED
green: str = fore.GREEN
yellow: str = fore.YELLOW
blue: str = fore.BLUE
reset: str = style('reset')

# Definir fondos
bg_red: str = back.RED
bg_green: str = back.GREEN

# Estilos
bold: str = style('bold')
underline: str = style('underline')

# Crear mensajes con colores y estilos
message1: str = f"{red}Este texto es rojo{reset}"
message2: str = f"{green}{bold}Este texto es verde y negrita{reset}"
message3: str = f"{yellow}{underline}Este texto es amarillo y subrayado{reset}"
message4: str = f"{blue}{bg_red}Texto azul con fondo rojo{reset}"

# Imprimir los mensajes
print(message1, end="\n", file=stdout)
print(message2, end="\n", file=stdout)
print(message3, end="\n", file=stdout)
print(message4, end="\n", file=stdout)

# Salida del programa con código de estado 0 (éxito)
exit(0)

### Recursos Adicionales

- Consulta [la documentación de `mypy`](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports) para obtener más detalles sobre cómo manejar módulos sin información de tipos.
- Considera la posibilidad de contribuir con ficheros de tipo para las bibliotecas que utilizas, si es posible.

En resumen, `# type: ignore` se usa para suprimir errores de tipo en líneas específicas donde `mypy` no puede encontrar la información de tipos necesaria. Es una solución rápida cuando se trabaja con bibliotecas que no están totalmente compatibles con las herramientas de verificación de tipos.
"""
```

### ***Explicación del Ejemplo Avanzado***

1. **Definir Colores y Estilos para la Tabla:**
   - *`headerColor` define el estilo para los encabezados de la tabla.*
   - *`dataColor` define el estilo para los datos.*
   - *`reset` restablece el estilo y color al valor predeterminado.*

2. **Definir Datos:**
   - *`headers` y `data` contienen los datos de la tabla.*

3. **Imprimir la Tabla:**
   - *Se imprime la fila de encabezados con el color y estilo definido.*
   - *Se imprime una línea de separación.*
   - *Se imprimen las filas de datos con el color y estilo definido.*
