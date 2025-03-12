#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import Callable

def decorador(funcion: Callable[[],None]) -> Callable[[],None]:
    def funcion_modificada() -> None:
        print("Antes de ejecutar la funcion", end = "\n", file = stdout)
        funcion()
        print("Despues de ejecutar la funcion", end = "\n", file = stdout)
        return None
    return funcion_modificada


def saludo() -> None:
    print("Hola Daniel", end = "\n", file = stdout)
    return None

saludoModificado: Callable[[],None] = decorador(funcion=saludo)
saludoModificado()

# Manera mas facil de entender los decoradores pero no es la mas optima
