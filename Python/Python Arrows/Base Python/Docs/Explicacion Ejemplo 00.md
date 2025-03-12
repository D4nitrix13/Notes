<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import Callable, Union

def apply(number: Union[int, float], f: Callable[[Union[int, float]], Union[int, float]]) -> Union[int, float]:
    """
    Aplica una función dada a un número y devuelve el resultado.

    Args:
        number (Union[int, float]): El número al que se aplicará la función.
        f (Callable): La función que se aplicará al número.

    Returns:
        Union[int, float]: El resultado de aplicar la función al número.
    """
    return f(number)

def double(number: Union[int, float]) -> Union[int, float]:
    """
    Duplica un número.

    Args:
        number (Union[int, float]): El número a duplicar.

    Returns:
        Union[int, float]: El número duplicado.
    """
    return 2 * number

if __name__ == "__main__":
    # Ejemplo de uso: Aplicar la función double al número 15.
    print(apply(number = 15, f = double), end="\n", file = stdout)
```

---

## ***Conceptos Clave***

1. **Funciones como Argumentos:** *En Python, al igual que en JavaScript, puedes pasar funciones como argumentos a otras funciones.*

2. **Tipado de Datos:** *Usando `typing.Callable`, especificas que `f` es una función que puede aceptar un `int` o `float` y devolver un `int` o `float`.*

---

### ***Características***

- **Flexibilidad:** *Permite modularizar y reutilizar funciones de manera efectiva al pasarlas como argumentos.*
- **Documentación Explícita:** *Las docstrings claras y detalladas ayudan a entender rápidamente cómo utilizar las funciones.*

---

### ***Ejemplo Práctico***

```python
if __name__ == "__main__":
    # Ejemplo de uso: Aplicar la función double al número 15.
    print(apply(number=15, f=double), end="\n", file = stdout)
```

- *Este código Python muestra cómo definir y utilizar funciones que aceptan otras funciones como argumentos, facilitando la aplicación de operaciones específicas a diferentes datos de manera modular y eficiente.*
