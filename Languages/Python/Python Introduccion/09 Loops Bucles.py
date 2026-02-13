"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Loops Bucles

# While

"""
El while es un bucle que se ejecuta mientras se cumpla una condición y se detiene cuando la condición no se cumple más 
"""
from sys import stdout
from typing import Any, Dict, List, Set, Tuple, Union


condicion: int = 0

while condicion < 10:
    print(condicion, end = "\n", file = stdout)
    condicion += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10", end = "\n", file = stdout)

print("La ejecución continúa", end = "\n", file = stdout)

"""
Si queremos detener la ejecución del bucle while podemos usar la palabra reservada break que se utiliza para detener la ejecución del bucle
"""

# Bucle infinito
while True:
    print("Esto es un bucle infinito que se detiene con break", end = "\n", file = stdout)
    break

while condicion < 20:
    condicion += 1
    if condicion == 15:
        print("Se detiene la ejecución", end = "\n", file = stdout)
        break
    print(condicion, end = "\n", file = stdout)

print("La ejecución continúa", end = "\n", file = stdout)

# For
"""
for es una palabra reservada de python que se utiliza para hacer bucles o loops que se ejecutan mientras haya elementoos en un iterable y se detienen cuando no hay más elementoos en el iterable. Un iterable es un objeto que se puede recorrer elementoo a elementoo. Los iterables pueden ser listas, tuplas, sets, diccionarios, etc.
"""
lista: List[int] = [35, 24, 62, 52, 30, 30, 17]

"""
la estructura de un for es la siguiente 
>>> for es una palabra reservada de python que se utiliza para hacer bucles o loops

>>> elemento es una variable que se utiliza para almacenar el elemento del iterable puede tener cualquier nombre que no sea una palabra reservada de python

>>> in es el operador de pertenencia que se utiliza para saber si un elemento pertenece a un iterable o no. Pero también se puede utilizar para recorrer un iterable asignando cada elemento a una variable que se puede utilizar dentro del bucle

>>> lista es el iterable que se va a recorrer
"""

# Esta variable puede almacenar cualquier tipo de valor
elemento: Any = None

for elemento in lista:
    print(elemento, end = "\n", file = stdout)

tupla: Tuple[Union[int, str, float], ...] = (35, 1.77, "Daniel", "Perez", "Daniel")

for elemento in tupla:
    print(elemento, end = "\n", file = stdout)

conjunto: Set[Union[str, int]] = {"Daniel", "Benjamin", 35}

for elemento in conjunto:
    print(elemento, end = "\n", file = stdout)

diccionario: Dict[Union[str, int], Union[str, int]] = {
    "Nombre": "Daniel",
    "Apellido": "Benjamin",
    "Edad": 35,
    1: "Python",
}

for elemento in diccionario:
    print(elemento, end = "\n", file = stdout)
    if elemento == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado", end = "\n", file = stdout)

print("La ejecución continúa", end = "\n", file = stdout)

for elemento in diccionario:
    print(elemento, end = "\n", file = stdout)
    if elemento == "Edad":
        continue
    print("Se ejecuta", end = "\n", file = stdout)
else:
    print("El bluce for para diccionario ha finalizado", end = "\n", file = stdout)
