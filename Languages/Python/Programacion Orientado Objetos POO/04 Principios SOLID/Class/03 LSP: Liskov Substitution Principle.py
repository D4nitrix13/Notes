#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
"LSP": "Liskov Substitution Principle" Significa en español Principio de sustitucion de Liskov. Se le llama asi por la matematica Barbara Liskov.

Este principio dice que una clase base debe poder ser sustituida por sus clases derivadas. Es decir que una clase derivada debe poder ser sustituida por su clase base sin afectar el funcionamiento del sistema.
"""

"""
Este codigo tiene un problema ya que la clase Pinguino no puede volar y la clase Ave si puede volar. Entonces la clase Pinguino no puede ser sustituida por la clase Ave sin afectar el funcionamiento del sistema.

class Ave:
    def __init__(self: 'Ave') -> None:
        return None

    def volar(self: 'Ave') -> str:
        return "Estoy volando"


class Pinguino(Ave):
    def __init__(self: 'Pinguino') -> None:
        super().__init__()
        return None

    # ave = Ave es una variable de parametro que es de tipo Ave

    def volar(self: 'Pinguino') -> str:
        return "No puedo volar"

def hacer_volar(ave: Ave = Ave) -> str:
    return ave.volar()

print(hacer_volar(ave = Pinguino()),end="\n", file = stdout)
"""

"""
En este codigo se soluciona el problema de la clase Pinguino que no puede volar. Se crea una clase AveVoladora que puede volar y una clase AveNoVoladora que no puede volar. Estas dos clases heredan de la clase Ave. Entonces la clase AveVoladora y la clase AveNoVoladora pueden ser sustituidas por la clase Ave sin afectar el funcionamiento del sistema.
"""


class Ave:
    def __init__(self: 'Ave') -> None:
        return None

    # Aqui podemos hacer todo lo que puede hacer un ave

class AveVoladora(Ave):
    def __init__(self: 'AveVoladora') -> None:
        super().__init__()
        return None

    def volar(self: 'AveVoladora') -> str:
        return "Estoy volando"

class AveNoVoladora(Ave):
    def __init__(self: 'AveNoVoladora') -> None:
        super().__init__()
        return None

    def volar(self: 'AveNoVoladora') -> str:
        return "No puedo volar"
