#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Articulo https://www.johndcook.com/blog/2021/04/12/spaceship-operator/
# Foro https://stackoverflow.com/questions/68535022/universal-comparison-operator-in-python

from sys import stdout
from typing import Optional

x: Optional[int] = None
y: Optional[int] = None

# x <=> y
# 1, 2 | 1, 0

x, y = 1, 0
result: int = (x > y) - (x < y)
print(result, end = "\n", file = stdout)

"""
En Python, el operador nave espacial (`<=>`) se introduce en la versión 3.12 y es una forma de simplificar la comparación entre dos valores, retornando un valor que indica la relación entre ellos:

- `-1` si el primer valor es menor que el segundo,
- `0` si son iguales,
- `1` si el primer valor es mayor que el segundo.

Para recrear esta funcionalidad en versiones anteriores a Python 3.12, puedes usar la expresión matemática que has proporcionado:

```python
(x > y) - (x < y)
```

### Explicación del Código

1. **Inicialización:**
   ```python
   from sys import stdout
   from typing import Optional

   x: Optional[int] = None
   y: Optional[int] = None
   ```
   Aquí se importan `stdout` para la salida estándar y `Optional` para permitir que `x` y `y` puedan ser `int` o `None`.

2. **Asignación de Valores:**
   ```python
   x, y = 1, 0
   ```
   Se asignan los valores `1` a `x` y `0` a `y`.

3. **Comparación y Cálculo del Resultado:**
   ```python
   result: int = (x > y) - (x < y)
   ```
   - `(x > y)` evalúa a `True` o `False`, que son `1` y `0` en una evaluación numérica.
   - `(x < y)` también evalúa a `True` o `False`.
   - La resta `(x > y) - (x < y)` produce el resultado del operador nave espacial:
     - Si `x` es mayor que `y`, el resultado será `1 - 0 = 1`.
     - Si `x` es menor que `y`, el resultado será `0 - 1 = -1`.
     - Si `x` es igual a `y`, el resultado será `0 - 0 = 0`.

4. **Impresión del Resultado:**
   ```python
   print(result, end="\n", file=stdout)
   ```
   Imprime el resultado en la salida estándar.

### Código Completo

Aquí está el código completo con explicaciones:

```python
from sys import stdout
from typing import Optional

# Declaración de variables que pueden ser enteros o None
x: Optional[int] = None
y: Optional[int] = None

# Asignación de valores a las variables
x, y = 1, 0

# Cálculo del resultado del operador nave espacial
# (x > y) devuelve 1 si x es mayor que y, de lo contrario 0
# (x < y) devuelve 1 si x es menor que y, de lo contrario 0
# La resta de estas dos evaluaciones da el mismo resultado que el operador nave espacial
result: int = (x > y) - (x < y)

# Imprimir el resultado
print(result, end="\n", file=stdout)
```

### Comparación con el Operador Nave Espacial en Python 3.12

En Python 3.12, puedes usar directamente el operador nave espacial:

```python
result = x <=> y
```

Esto simplifica el código y es más explícito en su propósito, pero la expresión matemática `(x > y) - (x < y)` logra el mismo resultado en versiones anteriores a Python 3.12.
"""