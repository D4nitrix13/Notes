#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 

"""
Crear una clase estudiante con los siguientes atributos:
nombre, edad y grado

metodos:

estudiar: imprime f"el estudiante {} esta estudiando"
debemos preguntarle al usuario si quiere que el estudiante estudie, si la respuesta es si, entonces llamamos al metodo estudiar, si la respuesta es no, entonces no llamamos al metodo estudiar.
"""

import os
from sys import stdout
from typing import Optional

def borrar() -> None:
    os.system(command = "cls" if os.name == "nt" else "clear")
    return None


class Estudiante:
    def __init__(self: 'Estudiante', nombre: str, edad: int, grado: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.grado: str = grado
        return None


    def Estudiar(self: 'Estudiante') -> str: return f"El estudiante {self.nombre} esta estudiando"


nombre: str = str(input("Ingrese el nombre del estudiante: ")).capitalize()

while True:
    try:
        edad: int = int(input("Ingrese la edad del estudiante: "))
        break
    except ValueError: borrar()
grado: str = str(input("Ingrese el grado del estudiante: ")).lower()

estudiante: Estudiante = Estudiante(nombre = nombre, edad = edad, grado = grado)

borrar()
print(f"El Estudiante {estudiante.nombre}\nTiene {estudiante.edad} años\nY esta en el grado {estudiante.grado}",end = "\n", file = stdout)

preguntar: Optional[bool] = None

while True:
    if preguntar := str(input("Quieres estudiar (SI/NO)")) == "si":
        print(estudiante.Estudiar(),end = "\n", file = stdout)
        break
    elif preguntar == "no": break
    else: borrar()
