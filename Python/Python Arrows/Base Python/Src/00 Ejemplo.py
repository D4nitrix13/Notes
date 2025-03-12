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
