"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Tipos de errores

# SyntaxError
# print "¡Hola python3!" # Descomentar para Error
import math
from math import pi
from sys import stdout
from typing import Dict, List, Union

print("¡Hola comunidad!", end ="\n", file = stdout)

# NameError
lenguage: str = "Español"  # Comentar para Error
print(lenguage, end ="\n", file = stdout)

# IndexError
lista: List[str] = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(lista[0], end ="\n", file = stdout)
print(lista[4], end ="\n", file = stdout)
print(lista[-1], end ="\n", file = stdout)
# print(lista[5]) # Descomentar para Erro,end="\n"r

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Erro,end="\n"r
print(math.pi, end ="\n", file = stdout)

# KeyError
diccionario: Dict[Union[str, int], Union[str, int]] = {
    "Nombre": "Daniel",
    "Apellido": "PErez",
    "Edad": 18,
    1: "Python",
}
print(diccionario["Edad"], end ="\n", file = stdout)
# print(diccionario["Apelido"]) # Descomentar para Erro,end="\n"r
print(diccionario["Apellido"], end ="\n", file = stdout)

# TypeError
# print(lista["0"]) # Descomentar para Erro,end="\n"r
print(lista[0], end ="\n", file = stdout)
print(lista[False], end ="\n", file = stdout)  # False = 0

# ImportError
# from math import PI # Descomentar para Error
print(pi, end ="\n", file = stdout)

# ValueError
# integer = int("10 Años")
integer: int = int("10")  # Descomentar para Error
print(type(integer), end ="\n", file = stdout)

# ZeroDivisionError
# print(4/0) # Descomentar para Erro,end="\n"r
print(4 / 2, end ="\n", file = stdout)
