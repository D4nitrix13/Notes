#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from datetime import datetime
from sys import stdout, exit
from typing import Union

def primer_ejemplo() -> None:
    n: Union[int, float] = 1_000_000_000
    print(f"{n}", end = "\n", file = stdout)

    n = 1e9
    print(f"{n}", end = "\n", file = stdout)

    n = 1000000000
    print(f"{n:_}", end = "\n", file = stdout)
    print(f"{n:,}", end = "\n", file = stdout)

    return None



def segundo_ejemplo() -> None:
    var: str = "var"
    print(f"{var:>20}:", end = "\n", file = stdout)
    print(f"{var:<20}:", end = "\n", file = stdout)
    print(f"{var:^20}:", end = "\n", file = stdout)

    print(f"{var:_>20}:", end = "\n", file = stdout)
    print(f"{var:#<20}:", end = "\n", file = stdout)
    print(f"{var:|^20}:", end = "\n", file = stdout)

    return None



def tercer_ejemplo() -> None:
    now: datetime = datetime.now()
    print(f"{now:%d.%m.%y (%H:%M:%S)}", end = "\n", file = stdout)
    print(f"{now:%c}", end = "\n", file = stdout)
    print(f"{now:%I %p}", end = "\n", file = stdout)

    return None



def cuarto_ejemplo() -> None:
    n: float = 1234.5678
    print(n, end = "\n", file = stdout)
    print(round(number = n, ndigits = 2), end = "\n", file = stdout)
    print(f"{n:.2f}", end = "\n", file = stdout)
    print(f"{n:.0f}", end = "\n", file = stdout)
    print(f"{n:,.3f}", end = "\n", file = stdout)
    print(f"{n:_.3f}", end = "\n", file = stdout)

    return None

def quinto_ejemplo() -> None:
    a: int = 5
    b: int = 10
    var: str = "Daniel Says Hi"
    print(f"a + b = {a + b}", end = "\n", file = stdout)
    print(f"{a + b = }", end = "\n", file = stdout)
    print(f"{a + b =}", end = "\n", file = stdout)
    print(f"{a + b=}", end = "\n", file = stdout)
    print(f"{bool(a) = }", end = "\n", file = stdout)
    print(f"{var = }", end = "\n", file = stdout)

    return None


if __name__ == "__main__":
    primer_ejemplo()
    segundo_ejemplo()
    tercer_ejemplo()
    cuarto_ejemplo()
    quinto_ejemplo()
    exit(0)

"""
Aquí tienes una explicación detallada de cada función en el código proporcionado, que demuestra varias características y técnicas de formateo en Python.

### 1. **primer_ejemplo()**
Esta función muestra diferentes maneras de representar números en Python utilizando formateo de cadenas.

```python
def primer_ejemplo() -> None:
    n: Union[int, float] = 1_000_000_000
    print(f"{n}", end = "\n", file = stdout)

    n = 1e9
    print(f"{n}", end = "\n", file = stdout)

    n = 1000000000
    print(f"{n:_}", end = "\n", file = stdout)
    print(f"{n:,}", end = "\n", file = stdout)
```

- **`n: Union[int, float] = 1_000_000_000`:** Aquí se define una variable `n` que puede ser un entero o un flotante, inicializada con un valor grande.
  
- **`print(f"{n}", end = "\n", file = stdout)`:** Imprime el valor de `n` tal cual, sin ningún formato especial.

- **`n = 1e9`:** Asigna el valor de `n` en notación científica. `1e9` es igual a `1,000,000,000`.

- **`print(f"{n}", end = "\n", file = stdout)`:** Imprime el valor de `n` en notación científica.

- **`n = 1000000000`:** Asigna un valor de número entero sin formato especial.

- **`print(f"{n:_}", end = "\n", file = stdout)`:** Imprime el valor de `n` usando `_` como separador de miles (esto requiere Python 3.6 o superior).

- **`print(f"{n:,}", end = "\n", file = stdout)`:** Imprime el valor de `n` con comas como separador de miles.

### 2. **segundo_ejemplo()**
Esta función muestra cómo alinear y rellenar cadenas con varios caracteres.

```python
def segundo_ejemplo() -> None:
    var: str = "var"
    print(f"{var:>20}:", end = "\n", file = stdout)
    print(f"{var:<20}:", end = "\n", file = stdout)
    print(f"{var:^20}:", end = "\n", file = stdout)

    print(f"{var:_>20}:", end = "\n", file = stdout)
    print(f"{var:#<20}:", end = "\n", file = stdout)
    print(f"{var:|^20}:", end = "\n", file = stdout)
```

- **`var: str = "var"`:** Define una cadena `var` con el valor `"var"`.

- **`print(f"{var:>20}:", end = "\n", file = stdout)`:** Imprime `var` alineado a la derecha en un campo de 20 caracteres.

- **`print(f"{var:<20}:", end = "\n", file = stdout)`:** Imprime `var` alineado a la izquierda en un campo de 20 caracteres.

- **`print(f"{var:^20}:", end = "\n", file = stdout)`:** Imprime `var` centrado en un campo de 20 caracteres.

- **`print(f"{var:_>20}:", end = "\n", file = stdout)`:** Imprime `var` alineado a la derecha en un campo de 20 caracteres, rellenado con guiones bajos (`_`).

- **`print(f"{var:#<20}:", end = "\n", file = stdout)`:** Imprime `var` alineado a la izquierda en un campo de 20 caracteres, rellenado con signos de número (`#`).

- **`print(f"{var:|^20}:", end = "\n", file = stdout)`:** Imprime `var` centrado en un campo de 20 caracteres, rellenado con barras verticales (`|`).

### 3. **tercer_ejemplo()**
Esta función muestra cómo formatear fechas y horas.

```python
def tercer_ejemplo() -> None:
    now: datetime = datetime.now()
    print(f"{now:%d.%m.%y (%H:%M:%S)}", end = "\n", file = stdout)
    print(f"{now:%c}", end = "\n", file = stdout)
    print(f"{now:%I%p}", end = "\n", file = stdout)
```

- **`now: datetime = datetime.now()`:** Obtiene la fecha y hora actuales.

- **`print(f"{now:%d.%m.%y (%H:%M:%S)}", end = "\n", file = stdout)`:** Imprime la fecha y hora en el formato `día.mes.año (hora:minuto:segundo)`.

- **`print(f"{now:%c}", end = "\n", file = stdout)`:** Imprime la fecha y hora en formato completo, usando el formato de fecha y hora corto del sistema.

- **`print(f"{now:%I%p}", end = "\n", file = stdout)`:** Imprime la hora en formato de 12 horas seguido del AM/PM.

### 4. **cuarto_ejemplo()**
Esta función muestra cómo formatear números flotantes con diferentes precisiones y separadores.

```python
def cuarto_ejemplo() -> None:
    n: float = 1234.5678
    print(n, end = "\n", file = stdout)
    print(round(number = n, ndigits = 2), end = "\n", file = stdout)
    print(f"{n:.2f}", end = "\n", file = stdout)
    print(f"{n:.0f}", end = "\n", file = stdout)
    print(f"{n:,.3f}", end = "\n", file = stdout)
    print(f"{n:_.3f}", end = "\n", file = stdout)
```

- **`n: float = 1234.5678`:** Define un número flotante.

- **`print(n, end = "\n", file = stdout)`:** Imprime el número flotante tal cual.

- **`print(round(number = n, ndigits = 2), end = "\n", file = stdout)`:** Redondea el número a 2 decimales y lo imprime.

- **`print(f"{n:.2f}", end = "\n", file = stdout)`:** Imprime el número flotante redondeado a 2 decimales.

- **`print(f"{n:.0f}", end = "\n", file = stdout)`:** Imprime el número flotante redondeado a 0 decimales (entero).

- **`print(f"{n:,.3f}", end = "\n", file = stdout)`:** Imprime el número flotante con 3 decimales y comas como separadores de miles.

- **`print(f"{n:_.3f}", end = "\n", file = stdout)`:** Imprime el número flotante con 3 decimales y guiones bajos como separadores de miles (esto requiere Python 3.6 o superior).

### 5. **quinto_ejemplo()**
Esta función muestra cómo imprimir variables y expresiones en un formato de depuración.

```python
def quinto_ejemplo() -> None:
    a: int = 5
    b: int = 10
    var: str = "Daniel Says Hi"
    print(f"a + b = {a + b}", end = "\n", file = stdout)
    print(f"{a + b = }", end = "\n", file = stdout)
    print(f"{a + b =}", end = "\n", file = stdout)
    print(f"{a + b=}", end = "\n", file = stdout)
    print(f"{bool(a) = }", end = "\n", file = stdout)
    print(f"{var = }", end = "\n", file = stdout)
```

- **`a: int = 5`** y **`b: int = 10`:** Define dos enteros.

- **`var: str = "Daniel Says Hi"`:** Define una cadena.

- **`print(f"a + b = {a + b}", end = "\n", file = stdout)`:** Imprime el resultado de la suma de `a` y `b` con un texto explicativo.

- **`print(f"{a + b = }", end = "\n", file = stdout)`:** Usa el formato de cadena `f-string` para imprimir la expresión `a + b` junto con su resultado.

- **`print(f"{a + b =}", end = "\n", file = stdout)`** y **`print(f"{a + b=}", end = "\n", file = stdout)`:** También imprimen la expresión `a + b` con su resultado, pero el formato de impresión puede variar.

- **`print(f"{bool(a) = }", end = "\n", file = stdout)`:** Imprime el valor booleano de `a` con su nombre de expresión.

- **`print(f"{var = }", end = "\n", file = stdout)`:** Imprime el valor de `var` con su nombre de expresión.

Este código muestra cómo utilizar

 varias características avanzadas de formateo de cadenas en Python, que son útiles para la presentación y depuración de datos.
"""