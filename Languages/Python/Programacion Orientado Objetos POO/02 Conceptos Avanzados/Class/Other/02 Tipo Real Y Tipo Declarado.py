#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
En programación orientada a objetos, el tipo declarado de una variable es el tipo que se especifica en su declaración. El tipo real o actual de una variable es el tipo del objeto al que hace referencia en tiempo de ejecución.
"""

from sys import stdout

class Animal:
    def __init__(self: 'Animal') -> None: return None

    def sonido(self: 'Animal') -> str: return ""

class Gato(Animal):
    def __init__(self: 'Gato') -> None:
        super().__init__()
        return None

    def sonido(self: 'Gato') -> str: return "Miau"

class Perro(Animal):
    def __init__(self: 'Perro') -> None:
        super().__init__()
        return None

    def sonido(self: 'Perro') -> str: return "Guau"

# Tipo declarado: Animal
# Tipo real: Gato
animal1: Animal = Gato()

# Tipo declarado: Animal
# Tipo real: Perro
animal2: Animal = Perro()

print(animal1.sonido(),end="\n", file = stdout)  # Imprime "Miau"
print(animal2.sonido(),end="\n", file = stdout)  # Imprime "Guau"
