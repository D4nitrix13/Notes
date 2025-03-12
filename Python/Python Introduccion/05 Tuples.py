"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Tuplas

# Definición

"""
En python las tuplas son inmutables, es decir, no se pueden modificar, son una colección de elementos ordenados que no se pueden modificar ni eliminar

Ventajas de las tuplas:
- El acceso a los elementos es mas rápido que en las listas
- Ocupan menos espacio en memoria
- Formatean Strings
- Pueden utilizarse como claves en un diccionario
- Pueden utilizarse como elementos de una lista

Desventajas de las tuplas:
- No se pueden modificar
- No se pueden eliminar
- No se pueden ordenar
- No se pueden invertir
- No se pueden copiar
- No se pueden crear sublistas
- No se pueden concatenar
- No se pueden desempaquetar

Mutables: Son los objetos que se pueden modificar
Inmutables: Son los objetos que no se pueden modificar
"""

from sys import stdout
from typing import List, Tuple, Union

"""
>>> Para declarar una tupla con múltiples tipos, es necesario indicar el tipo de cada elemento en la tupla. Sin embargo, si no conoces el número exacto de elementos o sus tipos exactos, puedes usar Tuple[Union[int, str, float], ...] para indicar que la tupla puede tener un número variable de elementos, cada uno de los cuales puede ser de los tipos especificados.

>>> tupla: Tuple[Union[int, str, float], ...] = tuple()
"""

tupla: Union[Tuple[Union[int, str, float], ...], List[Union[int, float, str]]] = tuple()
otraTupla: Tuple[int, ...] = ()

tupla = (35, 1.77, "Daniel", "Perez", "Daniel")
otraTupla = (35, 60, 30)

print(tupla, end = "\n", file = stdout)
print(type(tupla), end = "\n", file = stdout)

# Acceso a elementos y búsqueda

print(tupla[0], end = "\n", file = stdout)
print(tupla[-1], end = "\n", file = stdout)
# print(tupla[4]) IndexError
# print(tupla[-6]) IndexError

print(tupla.count("Daniel"), end = "\n", file = stdout)
print(tupla.index("Perez"), end = "\n", file = stdout)
print(tupla.index("Daniel"), end = "\n", file = stdout)

# tupla[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

sumarTuplas: Tuple[Union[int, str, float], ...] = tupla + otraTupla
print(sumarTuplas, end = "\n", file = stdout)

"""
Tambien se pueden usar el slicing en las tuplas
"""

print("sumarTuplas[3:6] = ", sumarTuplas[3:6], end = "\n", file = stdout)

# Tupla mutable con conversión a lista

"""
Para convertir una tupla a lista se utiliza la función list()
Para convertir una lista a tupla se utiliza la función tuple()
"""

tupla = list(tupla)
print(type(tupla), end = "\n", file = stdout)

tupla[4] = "Daniel"
tupla.insert(1, "Azul")
tupla = tuple(tupla)
print(tupla, end = "\n", file = stdout)
print(type(tupla), end = "\n", file = stdout)

# Eliminación

# del tupla[2] TypeError: 'tuple' object doesn't support item deletion
# Que significa que no se puede eliminar un elemento en una tupla

del tupla
# print(tupla) NameError: name 'tupla' is not defined
# Que significa que no se puede imprimir una tupla que no existe
