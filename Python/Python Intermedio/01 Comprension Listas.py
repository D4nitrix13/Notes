"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""

# Tema: List Comprehension o Comprensión de listas


"""
List Comprehension o Comprensión de listas
>>> La comprensión de listas es una forma concisa de crear listas. Además, es más rápida que la creación de listas con un bucle for. Y tambien se puede utilizar para crear conjuntos, tuplas y diccionarios.

>>> Las listas son una de las estructuras de datos más utilizadas en Python y la comprensión de listas es una forma de crear listas de forma concisa.

Estructura:
[expresión for elemento in iterable]
"""

from sys import stdout
from typing import Dict, List, Set, Tuple, Union

# Ejemplo 1 con datos int
lista: List[Union[int, str]] = [0, 1, 2, 3, 4, 5, 6, 7]
print(f"{lista}", end ="\n", file = stdout)

rango: range = range(8)
print(f"list(rango) -> {list(rango)}", end ="\n", file = stdout)
print(f"type(rango) -> {type(rango)}", end ="\n", file = stdout)

# Definición

listaComprimida: List[Union[int, str, List[Union[int, str]]]] = [int(iterable) + 1 for iterable in range(0, 8, 1)]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

listaComprimida = [int(iterable) * 2 for iterable in range(0, 8, 1)]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

listaComprimida = [int(iterable) * iterable for iterable in range(0, 8, 1)]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

def sumar_cinco(*, numero: int) -> int:
    return numero + 5


# Tambien se pueden utilizar funciones en la comprensión de listas

listaComprimida = [
    sumar_cinco(numero = int(iterable)) for iterable in range(0, 8, 1)
]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

conjuntosComprimidos: Set[Union[int, str]] = set({int(iterable) for iterable in range(0, 8, 1)})
# conjuntosComprimidos: Set[int] = {int(iterable) for iterable in range(0, 8, 1)}

print(f"conjuntos comprimidos = {conjuntosComprimidos}", end ="\n", file = stdout)

tuplasComprimidas: Tuple[Union[Tuple[int, ...], int, str], ...] = tuple(int(iterable) for iterable in range(0, 8, 1))
print(f"tuplas comprimidas = {tuplasComprimidas}", end ="\n", file = stdout)

diccionarioComprimido: Dict[Union[int, str], Union[int, str]] = {
    int(iterable): int(iterable) for iterable in range(0, 8, 1)
}
print(f"diccionario comprimido = {diccionarioComprimido}", end ="\n", file = stdout)


# Ejemplo 2 con datos str

lista = ["hola", "mundo", "como", "estas"]
print(f"{lista}", end ="\n", file = stdout)

listaComprimida = [str(iterable) for iterable in lista]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

tuplasComprimidas = tuple(str(iterable) for iterable in lista)

print(f"tuplas comprimidas = {tuplasComprimidas}", end ="\n", file = stdout)

conjuntosComprimidos = set({str(iterable) for iterable in lista})
# conjuntosComprimidos = {str(iterable) for iterable in lista}

print(f"conjuntos comprimidos = {conjuntosComprimidos}", end ="\n", file = stdout)

diccionarioComprimido = {
    str(iterable): str(iterable) for iterable in lista
}
print(f"diccionario comprimido = {diccionarioComprimido}", end ="\n", file = stdout)


"""
tambien se pueden utilizar condicionales en la comprensión de listas
"""

listaComprimida = [
    int(iterable) for iterable in range(0, 8, 1) if iterable % 2 == 0
]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

tuplasComprimidas = tuple(
    int(iterable) for iterable in range(0, 8, 1) if iterable % 3 == 0
)

print(f"tuplas comprimidas = {tuplasComprimidas}", end ="\n", file = stdout)

conjuntosComprimidos = {
    int(iterable) for iterable in range(0, 8, 1) if iterable % 4 == 0
}

print(f"conjuntos comprimidos = {conjuntosComprimidos}", end ="\n", file = stdout)

diccionarioComprimido = {
    int(iterable): int(iterable) for iterable in range(0, 8, 1) if iterable % 5 == 0
}

listaBuena: List[str] = ["b", "c", "d", "a", "i"]
listaMala: List[str] = ["a", "e", "i", "o", "u"]
"""
Lo que estas haciendo es recorrer la listaMala y si el elemento esta en la listaBuena lo agregas a la listaComprimida
"""
listaComprimida = [
    str(iterable) for iterable in listaMala if iterable in listaBuena
]

print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

tuplasComprimidas = tuple(
    str(iterable) for iterable in listaMala if iterable in listaBuena
)

print(f"tuplas comprimidas = {tuplasComprimidas}", end ="\n", file = stdout)

conjuntosComprimidos = {
    str(iterable) for iterable in listaMala if iterable in listaBuena
}

print(f"conjuntos comprimidos = {conjuntosComprimidos}", end ="\n", file = stdout)

diccionarioComprimido = {
    str(iterable): str(iterable) for iterable in listaMala if iterable in listaBuena
}

"""
Tambien se pueden pasar estructuras anidadas en la comprensión de listas aunque no es tan común
"""

"""
En este caso estamos creando una lista de listas de enteros
En la primera iteración se crea una lista de enteros del 0 al 7 y se agrega a la listaComprimida
En la segunda iteración se dice que se repita la primera iteración 3 veces creando una lista de listas de enteros

Se puede crear otra variable o utilizar la misma variable para la comprensión de listas si una variable no se utiliza se puede utilizar el guion bajo
"""
listaComprimida = [
    [int(iterable) for iterable in range(0, 8, 1)] for _ in range(0, 3, 1)
]
print(f"lista comprimida = {listaComprimida}", end ="\n", file = stdout)

tuplasComprimidas = tuple(
    tuple(
        int(iterable) for iterable in range(0, 8, 1)
    ) for _ in range(0, 3, 1)
)

print(f"tuplas comprimidas = {tuplasComprimidas}", end ="\n", file = stdout)
