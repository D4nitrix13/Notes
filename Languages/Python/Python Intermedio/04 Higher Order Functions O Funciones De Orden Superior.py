"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
from functools import reduce
from sys import stdout
from typing import Callable, List
from typing_extensions import Protocol

class Add(Protocol):
    def __call__(self: "Add", valor: int) -> int: return valor

# Tema: Higher Order Functions o Funciones de Orden Superior

"""
Funciones de orden superior son funciones que toman otras funciones como argumentos o devuelven otras funciones como resultado.
Las funciones de orden superior son una característica importante de los lenguajes de programación funcional.
"""


def sumar_uno(valor: int) -> int: return valor + 1

def sumar_cinco(valor: int) -> int: return valor + 5

def sumar_dos_valores_añadir_valor(
    primerValor: int, segundoValor: int, funcionSuma: Callable
) -> int:
    return funcionSuma(primerValor + segundoValor)


print(
    sumar_dos_valores_añadir_valor(primerValor = 5, segundoValor = 2, funcionSuma = sumar_uno),
    end="\n", file = stdout
)

print(
    sumar_dos_valores_añadir_valor(primerValor = 5, segundoValor = 2, funcionSuma = sumar_cinco),
    end="\n", file = stdout
)

def sumar_diez(valorOriginal: int) -> Add:
    def add(valor: int) -> int: return valor + 10 + valorOriginal
    return add

añadirFuncion: Add = sumar_diez(valorOriginal = 10)
print(añadirFuncion(5), end ="\n", file = stdout)
print((sumar_diez(valorOriginal = 5))(valor = 1), end ="\n", file = stdout)

# Built-in Higher Order Functions o Funciones de Orden Superior Integradas

listaNumeros: List[int] = [2, 5, 10, 21, 3, 30]

# Map
"""
map() es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia
La función map() toma una función y una secuencia y devuelve un iterador que produce los resultados de aplicar la función a cada elemento de la secuencia.
"""

def multiplicar_dos(numero: int) -> int: return numero * 2

print(list(map(multiplicar_dos, listaNumeros)), end ="\n", file = stdout)
print(list(map(lambda numero: numero * 2, listaNumeros)), end ="\n", file = stdout)

# Filter
"""
filter() es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia
La función filter() toma una función y una secuencia y devuelve un iterador que produce todos los elementos de la secuencia para los que la función devuelve True.
"""


def filtrar_mayor_que_diez(numero: int) -> bool:
    if numero > 10: return True
    return False


print(list(filter(filtrar_mayor_que_diez, listaNumeros)), end ="\n", file = stdout)
print(list(filter(lambda numero: numero > 10, listaNumeros)), end ="\n", file = stdout)


"""
reduce() es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia
La función reduce() toma una función y una secuencia y devuelve un solo valor calculado a partir de la secuencia.
La función reduce() se encuentra en el módulo functools.
"""

# Reduce

def sumar_dos_valores(primerValor: int, segundoValor: int) -> int: return primerValor + segundoValor

print(reduce(sumar_dos_valores, listaNumeros), end ="\n", file = stdout)
print(reduce(sumar_dos_valores, listaNumeros, 15), end ="\n", file = stdout)
print(sum(listaNumeros, start = 0), end ="\n", file = stdout)
