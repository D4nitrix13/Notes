#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
SRP": "Single Responsability Principle" Significa en español Principio de responsabilidad unica. 

>>> Este principio dice que una clase debe tener una sola responsabilidad y no muchas responsabilidades.

>>> Este principio evita que los desarrolladores creen clases con muchas responsabilidades y que sean dificiles de mantener y de entender.
"""


from sys import stdout


class TanqueCombustible:
    def __init__(self: 'TanqueCombustible') -> None:
        self.combustible: int = 100
        return None

    def agregarCombustible(self: 'TanqueCombustible', cantidad: int) -> None:
        self.combustible += cantidad
        return None

    def obtenerCombustible(self: 'TanqueCombustible') -> int:
        return self.combustible

    def usarCombustible(self: 'TanqueCombustible', cantidad: int) -> None:
        self.combustible -= cantidad
        return None

class Auto:
    def __init__(self: 'Auto', tanque: 'TanqueCombustible') -> None:
        self.posicion: int = 0
        self.tanque: 'TanqueCombustible' = tanque
        return None

    def mover(self: 'Auto', distancia: int) -> str:
        if not self.tanque.obtenerCombustible() >= distancia / 2:
            return "No hay suficiente combustible"
        
        self.posicion += distancia
        self.tanque.usarCombustible(cantidad = distancia // 2)
        return "Has movido el auto exitosamente"
        

    def obtener_posicion(self: 'Auto') -> int: return self.posicion


tanque: TanqueCombustible = TanqueCombustible()
miAuto: Auto = Auto(tanque = tanque)
print(miAuto.obtener_posicion(),end="\n", file = stdout)

print(miAuto.mover(distancia = 10),end="\n", file = stdout)

print(miAuto.obtener_posicion(),end="\n", file = stdout)

print(miAuto.mover(distancia = 20),end="\n", file = stdout)

print(miAuto.obtener_posicion(),end="\n", file = stdout)

print(miAuto.mover(distancia = 60),end="\n", file = stdout)

print(miAuto.obtener_posicion(),end="\n", file = stdout)

print(miAuto.mover(distancia = 100),end="\n", file = stdout)

print(miAuto.obtener_posicion(),end="\n", file = stdout)

print(miAuto.mover(distancia = 100),end="\n", file = stdout)

print(miAuto.obtener_posicion(),end="\n", file = stdout)
