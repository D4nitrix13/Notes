"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Listas

# Definición

"""
Las listas son una colección de elementos ordenados que se pueden modificar y eliminar y que pueden tener elementos de diferentes tipos

Ventajas de las listas:
- Se pueden modificar
- Se pueden eliminar
- Se pueden ordenar
- Se pueden invertir
- Se pueden copiar
- Se pueden crear sublistas
- Se pueden concatenar
- Se pueden desempaquetar
- Se pueden crear listas vacias
- Se pueden crear listas con elementos de diferentes tipos
- Se pueden crear listas con elementos repetidos

Desventajas de las listas:
- El acceso a los elementos es mas lento que en las tuplas
- Ocupan mas espacio en memoria que las tuplas
- No se pueden utilizar como claves en un diccionario porque son mutables
- No se pueden utilizar como elementos de una lista porque son mutables

Mutables: Son los objetos que se pueden modificar
Inmutables: Son los objetos que no se pueden modificar
"""

from sys import stdout
from typing import Any, List, Union


lista: list[int] = list()
otraLista: List[Union[int, float, str, None]] = []

print(len(lista), end = "\n", file = stdout)

lista = [35, 24, 62, 52, 30, 30, 17]

print(lista, end = "\n", file = stdout)
print(len(lista), end = "\n", file = stdout)

otraLista = [35, 1.77, "Daniel", "Perez"]

print(type(lista), end = "\n", file = stdout)
print(type(otraLista), end = "\n", file = stdout)

# Acceso a elementos y búsqueda de elementos mediante índices
"""
Los índices son la posición de un elemento dentro de una lista
Ejemplo:
lista = [35, 24, 62, 52, 30, 30, 17]
para acceder al elementos:
35 usamos el índice positivo 0 o el indice negativo -7
24 usamos el índice positivo 1 o el indice negativo -6
62 usamos el índice positivo 2 o el indice negativo -5
52 usamos el índice positivo 3 o el indice negativo -4
30 usamos el índice positivo 4 o el indice negativo -3
30 usamos el índice positivo 5 o el indice negativo -2
17 usamos el índice positivo 6 o el indice negativo -1

Los índices pueden ser positivos o negativos
Los índices positivos empiezan desde 0
Los índices negativos empiezan desde -1
"""

print(otraLista[0], end = "\n", file = stdout)
print(otraLista[1], end = "\n", file = stdout)
print(otraLista[-1], end = "\n", file = stdout)
print(otraLista[-4], end = "\n", file = stdout)
# .count() devuelve el número de veces que aparece un elemento en una lista puede ser un número o una cadena
print(lista.count(30), end = "\n", file = stdout)
# print(otraLista[4]) Si el índice no existe en la lista IndexError
# print(otraLista[-5]) Si el índice no existe en la lista genera un error IndexError

print(otraLista.index("Daniel"), end = "\n", file = stdout)

# Desempaquetado de listas
"""
otraLista = [35, 1.77, "Daniel", "Perez"]
edad: int = 35
ancho: float = 1.77
nombre: str = "Daniel"
segundoNombre: str = "Perez"
"""
edad: Union[int, float, str, None] = None
ancho: Union[int, float, str, None] = None
nombre: Union[int, float, str, None] = None
segundoNombre: Union[int, float, str, None] = None

edad, ancho, nombre, segundoNombre = otraLista
print(nombre, end = "\n", file = stdout)

# Otra forma de desempaquetar listas es:
nombre, ancho, edad, segundoNombre = (
    otraLista[2],
    otraLista[1],
    otraLista[0],
    otraLista[3],
)
print(edad, end = "\n", file = stdout)

# Concatenación de listas

# Al hacer una suma de listas se concatenan
# [35, 24, 62, 52, 30, 30, 17] + [35, 1.77, "Daniel", "Perez"]
# [35, 24, 62, 52, 30, 30, 17, 35, 1.77, "Daniel", "Perez"]
print(lista + otraLista, end = "\n", file = stdout)
# print(lista - otraLista) No se puede restar listas SyntaxError

# Creación, inserción, actualización y eliminación

# El metodo append() agrega un elemento al final de la lista
otraLista.append("Daniel")
print(otraLista, end = "\n", file = stdout)

# El metodo insert() agrega un elemento en la posición que se le indique
# insert(posición, elemento)
"""
otraLista = [35, 1.77, "Daniel", "Perez"]

otraLista.insert(1, "Rojo")
otraLista = [35, "Rojo", 1.77, "Daniel", "Perez"]
"""
otraLista.insert(1, "Rojo")
print(otraLista, end = "\n", file = stdout)

# Cambiar un elemento de la lista mediante su índice
"""
otros_lista = [35, "Rojo", 1.77, "Daniel", "Perez"]

lista  35  "Rojo"  1.77  "Daniel"  "Perez"
indice  0     1      2       3         4

otraLista[1] = "Azul"
otraLista = [35, "Azul", 1.77, "Daniel", "Perez"]

"""
otraLista[1] = "Azul"
print(otraLista, end = "\n", file = stdout)


# El metodo remove() elimina un elemento de la lista mediante su valor si hay más de un elemento con el mismo valor elimina el primero que encuentre si no encuentra el elemento genera un error ValueError.
otraLista.remove("Azul")
print(otraLista, end = "\n", file = stdout)

lista.remove(30)
print(lista, end = "\n", file = stdout)

# El metodo pop() elimina un elemento de la lista mediante su índice si no se le indica un índice elimina el último elemento de la lista

# lista.pop(-1) es lo mismo que lista.pop() elimina el último elemento de la lista
# lista.pop(0) elimina el primer elemento de la lista
# lista.pop(2) elimina el elemento en la posición 2 de la lista
# lista.pop(3) elimina el elemento en la posición 3 de la lista
print(lista.pop(), end = "\n", file = stdout)
print(lista, end = "\n", file = stdout)

# Se puede guardar el elemento que se elimina en una variable de esta forma
pop_elemento = lista.pop(2)
print(pop_elemento, end = "\n", file = stdout)
print(lista, end = "\n", file = stdout)

# la palabra reservada del elimina una variable o un elemento de una lista mediante su índice
del lista[2]
print(lista, end = "\n", file = stdout)

# Operaciones con listas

nuevaLista: List[Any] = lista.copy()

# El metodo clear() elimina todos los elementos de una lista y la deja vacia
lista.clear()
print(lista, end = "\n", file = stdout)
print(nuevaLista, end = "\n", file = stdout)

# El metodo reverse() invierte el orden de los elementos de una lista
# El metodo sort() ordena los elementos de una lista de menor a mayor si la lista tiene elementos de diferentes tipos genera un error TypeError
# El metodo sort() no se puede usar con listas que tengan elementos de diferentes tipos
# Tener en cuenta que sort() ordena las strings basándose en el orden lexicográfico, que puede no coincidir con el orden alfabético si las strings contienen caracteres no alfabéticos.

# El metodo sort() no retorna nada y modifica la lista original. Tiene como parámetros reverse y key. reverse es un booleano que si es True ordena la lista de mayor a menor y si es False ordena la lista de menor a mayor. key es una función que se le pasa como argumento y que se usa para ordenar la lista.
nuevaLista.reverse()

print(nuevaLista, end = "\n", file = stdout)

nuevaLista.sort()
print(nuevaLista, end = "\n", file = stdout)

# Sublistas

print(nuevaLista[1:3])

# Cambio de tipo de dato
# No todos los lenguages de programación permiten cambiar el tipo de dato de una variable
lista: str = "Hola Python"
print(lista, end = "\n", file = stdout)
print(type(lista), end = "\n", file = stdout)

"""
[:] Devuelve una copia de la lista completa
[::] Devuelve una copia de la lista completa
[::1] Devuelve una copia de la lista completa
[0:len(nuevaLista):1] Devuelve una copia de la lista completa
"""
print(nuevaLista[:], end = "\n", file = stdout)
print(nuevaLista[::], end = "\n", file = stdout)
print(nuevaLista[::1], end = "\n", file = stdout)
print(nuevaLista[0:len(nuevaLista):1], end = "\n", file = stdout)
"""
Con los las listas pasa algo curioso y es que si asignamos una lista a otra lista y cambiamos un elemento de la lista original se cambia en la lista copia

ejemplo:
lista: list[int] = [1, 2, 3]
copia_lista: list[int] = lista

lista[0] = 4
print(lista) # [4, 2, 3]
print(copia_lista) # [4, 2, 3]

Esto pasa porque las listas son mutables y cuando se asigna una lista a otra lista se asigna la referencia de memoria de la lista original a la lista copia y cuando se cambia un elemento de la lista original se cambia en la lista copia porque ambas listas apuntan a la misma referencia de memoria
"""
