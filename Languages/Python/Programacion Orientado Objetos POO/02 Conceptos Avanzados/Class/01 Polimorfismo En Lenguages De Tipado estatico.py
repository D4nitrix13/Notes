#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# El polimorfismo en python o en lenguages de tipado dinamico suele aplicarse de distinta manera que en lenguages de tipado estatico como Java o C# o C++.

# Asi se haria en lenguages de tipado estatico como Java o C# o C++ ya que no se puede tener dos clases con el mismo metodo por eso se usa la herencia para que ambas clases tengan el mismo metodo pero cada una lo ejecuta de manera diferente

# A esto se le llama polimorfismo de herencia o Polimorfirmo de subtipos o Polimorfismo de subclases


"""
Otro tipo de polimorfismo polimorfismo de sobrecarga

En Python, no existe el polimorfismo de sobrecarga en el sentido tradicional que se encuentra en otros lenguajes de programación como Java o C++. La sobrecarga de métodos se refiere a la capacidad de una clase para tener múltiples métodos con el mismo nombre pero con diferentes tipos o número de argumentos.

Python no soporta la sobrecarga de métodos de esta manera. Si defines un método con el mismo nombre más de una vez, el último método definido sobrescribirá los anteriores.

Sin embargo, Python tiene formas de lograr un comportamiento similar a la sobrecarga de métodos. Una forma común es usar argumentos con valores predeterminados o argumentos variables.
"""

from typing import Optional
from sys import stdout

class Animal:
    def __init__(self: 'Animal') -> None:
        return None

    def sonido(self: 'Animal') -> Optional[str]: return None
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

gatito: Gato = Gato()
perrito: Perro = Perro()

print(gatito.sonido(), end = "\n", file = stdout)
print(perrito.sonido(), end = "\n", file = stdout)
