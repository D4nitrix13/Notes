<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***La biblioteca `prettytable` en Python se utiliza para generar tablas visualmente atractivas en la terminal o en la salida estándar. Es especialmente útil para mostrar datos de manera organizada y legible.***

> [!NOTE]
> **[Recurso](https://zetcode.com/python/prettytable/ "https://zetcode.com/python/prettytable/")**

## ***Instalación***

**Primero, necesitas instalar `prettytable` si aún no lo has hecho. Puedes instalarlo usando pip:**

```bash
pip install prettytable
```

### ***Uso Básico***

**Aquí te muestro cómo usar `PrettyTable` con ejemplos comentados:**

#### ***Ejemplo 1: Crear una Tabla Básica***

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Importamos la clase PrettyTable del módulo prettytable
from prettytable import PrettyTable
from sys import stdout, exit

# Creamos una instancia de PrettyTable
table: PrettyTable = PrettyTable()

# Definimos los nombres de las columnas de la tabla
table.field_names = ["Nombre", "Edad", "Ciudad"]

# Agregamos filas a la tabla
table.add_row(row = ["Danna", 30, "Nueva York"])
table.add_row(row = ["Benjamin", 25, "San Francisco"])
table.add_row(row = ["Charlie", 35, "Los Ángeles"])

# Imprimimos la tabla
print(table, end = "\n", file = stdout)
exit(0)
```

*En este ejemplo, se crea una tabla con tres columnas: "Nombre", "Edad" y "Ciudad", y se agregan tres filas con datos correspondientes.*

#### ***Ejemplo 2: Configuración Avanzada***

**Puedes personalizar la apariencia de la tabla de varias maneras. Aquí hay algunos ejemplos:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout, exit
from prettytable import PrettyTable

# Creamos una instancia de PrettyTable
table: PrettyTable = PrettyTable()

# Definimos los nombres de las columnas
table.field_names = ["Producto", "Cantidad", "Precio Unitario"]

# Agregamos filas a la tabla
table.add_row(row = ["Manzanas", 10, "$1.00"])
table.add_row(row = ["Naranjas", 5, "$0.80"])
table.add_row(row = ["Plátanos", 7, "$1.20"])

# Configuramos el ancho de las columnas
table.max_width = 20

# Cambiamos el alineamiento de las columnas
table.align["Producto"] = "l"  # Alineación a la izquierda
table.align["Cantidad"] = "r"  # Alineación a la derecha
table.align["Precio Unitario"] = "c"  # Alineación al centro

# Establecemos un borde para la tabla
table.border = True

# Establecemos el borde de las filas
table.header = True
table.header_style = "title"

# Imprimimos la tabla
print(table, end = "\n", file = stdout)
exit(0)
```

#### ***Ejemplo 3: Mostrar la Tabla en Formato de deseado, agregando un título***

**Puedes exportar la tabla en formato deseado, agregando un título para usarla en ficheros README u otros documentos.**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout, exit
from prettytable import PrettyTable

# Creamos una instancia de PrettyTable
table: PrettyTable = PrettyTable()

# Definimos los nombres de las columnas
table.field_names = ["Nombre", "Edad", "Ciudad"]

# Agregamos filas a la tabla
table.add_row(row = ["Danna", 30, "Nueva York"])
table.add_row(row = ["Benjamin", 25, "San Francisco"])
table.add_row(row = ["Charlie", 35, "Los Ángeles"])

# Exportamos la tabla en formato deseado, agregando un título
# El formato por defecto es 'grid', que muestra la tabla con bordes
formatTable: str = table.get_string(title="Australian cities")

# Imprimimos la tabla formateada con el título en la salida estándar
# El parámetro end="\n" asegura que haya una nueva línea después de la tabla
print(formatTable, end="\n", file=stdout)

# Salimos del programa con código de estado 0 (éxito)
exit(0)
```

### ***Métodos Principales***

- **`PrettyTable()`:** *Crea una nueva instancia de `PrettyTable`.*
- **`field_names`:** *Define los nombres de las columnas de la tabla.*
- **`add_row(row)`:** *Agrega una fila a la tabla. La fila debe ser una lista con los valores de cada columna.*
- **`get_string()`:** *Devuelve una representación en cadena de la tabla en el formato especificado agregando un título", etc.*
- **`max_width`:** *Establece el ancho máximo de las columnas.*
- **`align`:** *Establece el alineamiento de las columnas. Puede ser "l" para izquierda, "r" para derecha, o "c" para centro.*
- **`border`:** *Habilita o deshabilita el borde de la tabla.*
- **`header`:** *Habilita o deshabilita el encabezado de la tabla.*
- **`header_style`:** *Define el estilo del encabezado.*

### **Ejemplo Completo**

**Aquí tienes un ejemplo completo que muestra cómo usar `PrettyTable` para crear una tabla con todas las opciones anteriores:**

```python
#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout, exit
from prettytable import PrettyTable

# Creamos una instancia de PrettyTable
table: PrettyTable = PrettyTable()

# Definimos los nombres de las columnas
table.field_names = ["Nombre", "Edad", "Ciudad"]

# Agregamos filas a la tabla
table.add_row(row = ["Danna", 30, "Nueva York"])
table.add_row(row = ["Benjamin", 25, "San Francisco"])
table.add_row(row = ["Charlie", 35, "Los Ángeles"])

# Configuramos el ancho máximo de las columnas
table.max_width = 20

# Cambiamos el alineamiento de las columnas
table.align["Nombre"] = "l"
table.align["Edad"] = "r"
table.align["Ciudad"] = "c"

# Habilitamos el borde y el encabezado
table.border = True
table.header = True

# Imprimimos la tabla
print(table, end="\n", file=stdout)

# Salimos del programa con código de estado 0 (éxito)
exit(0)
```
