#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import Callable

def decorador_one(funcion: Callable[[], None]) -> Callable[[], None]:
    def funcion_interna() -> None:
        print("Decorador 1 antes de la ejecución de la función", end="\n", file = stdout)
        funcion()
        print("Decorador 1 después de la ejecución de la función", end="\n", file = stdout)
        return None
    return funcion_interna


def decorador_two(funcion: Callable[[], None]) -> Callable[[], None]:
    def funcion_interna() -> None:
        print("Decorador 2 antes de la ejecución de la función", end="\n", file = stdout)
        funcion()
        print("Decorador 2 después de la ejecución de la función", end="\n", file = stdout)
        return None

    return funcion_interna


@decorador_one
@decorador_two
def saludo() -> None:
    print("¡Hola!", end="\n", file = stdout)
    return None

saludo()

"""
saludo está decorado con @decorador_one y @decorador_two, la salida completa será:

>>> Decorador 1 antes de la ejecución de la función
>>> Decorador 2 antes de la ejecución de la función
>>> ¡Hola!
>>> Decorador 2 después de la ejecución de la función
>>> Decorador 1 después de la ejecución de la función

La salida que ves es el resultado de aplicar dos decoradores, decorador_one y decorador_two, a la función saludo. Los decoradores en Python se aplican de abajo hacia arriba. Por lo tanto, primero se aplica decorador_two, luego decorador_one.

Cuando llamas a la función saludo(), esto es lo que sucede:

Debido al decorador decorador_one, se imprime "Decorador 1 antes de la ejecución de la función".

Luego, se llama a la función saludo. Pero saludo ha sido decorada con decorador_two, por lo que en lugar de ejecutar saludo directamente, se ejecuta el código del decorador decorador_two.

Dentro de decorador_two, se imprime "Decorador 2 antes de la ejecución de la función", luego se ejecuta la función original saludo (que imprime "¡Hola!"), y finalmente se imprime "Decorador 2 después de la ejecución de la función".

Después de que se completa la ejecución de decorador_two y saludo, se vuelve al decorador decorador_one, donde se imprime "Decorador 1 después de la ejecución de la función".


Se puedes aplicar tantos decoradores como desees a una función en Python.
"""
