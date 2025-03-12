<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion Ejemplo 01***

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from typing import Callable, Union
from sys import stdout

def apply(number: Union[int, float], f: Callable[[Union[int, float]], Union[int, float]]) -> Union[int, float]:
    """
    Igual en Python3 se le puede pasar una funcion como argumento
    """
    return f(number)

if __name__ == "__main__":
    """
    funciones anonimas en python solo se pueden de una linea eso tengo entendido no se puede de multiple linea eso tengo entendido
    """
    print(apply(number = 15, f = lambda num: 2 * num),end="\n", file = stdout)
```

---

## ***Conceptos Clave***

1. **Funciones Lambda:** *En Python, las funciones lambda son funciones anónimas de una sola línea.*

2. **Sintaxis Compacta:** *Las funciones lambda permiten una sintaxis más compacta y pueden ser útiles cuando la función es simple y no requiere múltiples líneas de código.*

---

### ***Características***

- **Limitaciones:** *Las funciones lambda en Python están restringidas a una única expresión y no permiten múltiples líneas de código.*

---

### ***Ejemplo Práctico***

```python
if __name__ == "__main__":
    # Ejemplo de uso: Aplicar una función lambda que duplica el número 15.
    print(apply(number=15, f=lambda num: 2 * num), end="\n", file = stdout)
```

- *Este ejemplo muestra cómo utilizar una función lambda de una línea como argumento de la función `apply` en Python, aplicando la operación de duplicar el número 15 de manera concisa y directa.*
