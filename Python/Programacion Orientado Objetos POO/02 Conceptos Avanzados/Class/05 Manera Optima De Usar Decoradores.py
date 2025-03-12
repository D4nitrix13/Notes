#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import Callable

# Este tipo de decorador se le conoce como decorador de funcion
def decorador(funcion: Callable[[],None]) -> Callable[[],None]:
    def funcion_modificada() -> None:
        print("Antes de ejecutar la funcion", end = "\n", file = stdout)
        funcion()
        print("Despues de ejecutar la funcion", end = "\n", file = stdout)
        return None

    return funcion_modificada


@decorador
def saludo() -> None:
    print("Hola Daniel", end = "\n", file = stdout)

# Mofiicamos la funcion saludo con el decorador
saludo()

# Manera mas optima de usar los decoradores
