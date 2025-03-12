#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
Los getters y setters son métodos que nos permiten acceder y modificar atributos privados de una clase.
"""


from sys import stdout


class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int) -> None:
        self.__nombre: str = nombre
        self.__edad: int = edad
        return None

    # Getters para obtener los valores de los atributos privados
    def get_nombre(self: 'Persona') -> str: return self.__nombre

    def get_edad(self: 'Persona') -> int: return self.__edad

    # Setters para modificar los valores de los atributos privados
    def set_nombre(self: 'Persona', nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre
        return None
    
    def set_edad(self: 'Persona', nueva_edad: int) -> None:
        self.__edad = nueva_edad
        return None

daniel: Persona = Persona(nombre="Daniel", edad=20)

# Getters para obtener los valores de los atributos privados
print(daniel.get_nombre(),end="\n", file = stdout)

# Setters para modificar los valores de los atributos privados

# Forma correcta para modificar los atributos privados
daniel.set_nombre(nuevo_nombre="Benjamin")

daniel.__nombre = "Benjamin" # No se puede modificar el atributo privado de esta forma
print(daniel.get_nombre(),end="\n", file = stdout)
