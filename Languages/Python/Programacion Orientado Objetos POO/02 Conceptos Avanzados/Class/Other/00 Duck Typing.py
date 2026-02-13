#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me
"""
Duck Typing es un concepto en Python que se refiere a la idea de que no importa el tipo de objeto con el que estás trabajando, sino qué operaciones o comportamientos puedes hacer con él. Si un objeto se comporta como un pato (es decir, tiene los mismos métodos y propiedades), entonces puedes tratarlo como un pato.
"""


from sys import stdout
from typing import Union


class Pato:
    def __init__(self: 'Pato') -> None:
        return None

    def hablar(self: 'Pato') -> str:
        return "¡Cuac!"


class Perro:
    def __init__(self: 'Perro') -> None:
        return None

    def hablar(self: 'Perro') -> str: return "¡Guau!"

def hacer_hablar(Animal: Union[Pato, Perro]) -> None:
    # No importa el tipo de 'Animal' mientras tenga un método 'hablar'
    print(Animal.hablar(),end="\n", file = stdout)
    return None


pato: Pato = Pato()
perro: Perro = Perro()

# Aunque 'pato' y 'perro' son de diferentes tipos,
# ambos tienen un método 'hablar', por lo que podemos usarlos
# de manera intercambiable en la función 'hacer_hablar'

hacer_hablar(Animal = pato)  # Imprime: ¡Cuac!
hacer_hablar(Animal = perro)  # Imprime: ¡Guau!

# En este ejemplo, la función hacer_hablar puede tomar cualquier objeto que tenga un método hablar. No importa si el objeto es un Pato o un Perro, siempre que tenga un método hablar, se puede usar en hacer_hablar. Esto es Duck Typing.
