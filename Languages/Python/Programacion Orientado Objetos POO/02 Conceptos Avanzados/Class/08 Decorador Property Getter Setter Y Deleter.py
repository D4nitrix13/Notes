#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

""" 
@property es un decorador reservado en Python que nos permite definir métodos getter, setter y deleter para atributos de clase. Esto nos permite acceder a los atributos de una clase como si fueran públicos, pero sin perder la seguridad de que sean privados.

Ademas de que accedemos a el como si fuera un atributo, al llamarlo no es necesario poner los parentesis.
"""

from sys import stdout


class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int) -> None:
        self.__nombre: str = nombre
        self.__edad: int = edad
        return None

    @property
    # Getter
    # Estamos oculatando el nombre real del atributo y lo estamos reemplazando por el nombre del decorador ademas obtenemos el valor del atributo tambien de que no es necesario poner los parentesis al llamarlo
    def nombre(self: 'Persona') -> str:
        return self.__nombre

    @nombre.setter
    # Setter
    # Ponemos nombre.setter para que sepa que es el setter del atributo nombre lo que hace es cambiar el valor del atributo ademas de que no es necesario poner los parentesis al llamarlo
    def nombre(self: 'Persona', nuevoNombre: str) -> None:
        self.__nombre = nuevoNombre
        return None

    @nombre.deleter
    # deleter
    # Ponemos nombre.deleter para que sepa que es el deleter del atributo nombre lo que hace es eliminar el atributo ademas de que no es necesario poner los parentesis al llamarlo
    def nombre(self: 'Persona') -> None:
        del self.__nombre
        return None


daniel: 'Persona' = Persona(nombre="Daniel", edad=20)
print(daniel.nombre,end="\n", file = stdout)
daniel.nombre = "Benjamin"
del daniel.nombre
try: print(daniel.nombre,end="\n", file = stdout)
except AttributeError: print("El atributo nombre ha sido eliminado",end="\n", file = stdout)
else: print("El atributo nombre no ha sido eliminado",end="\n", file = stdout)
finally: print("Fin del programa",end="\n", file = stdout)
