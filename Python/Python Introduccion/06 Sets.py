"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Sets


# Definición

"""
Los sets son una colección de elementos desordenados que no se pueden modificar ni eliminar y que no pueden tener elementos de diferentes tipos

Ventajas de los sets:
- El acceso a los elementos es mas rápido que en las listas
- Ocupan menos espacio en memoria


Desventajas de los sets:
- Son desordenados
"""

from sys import stdout
from typing import Set, Union

"""
>>> En Python, un conjunto (set) se puede inicializar utilizando llaves {} o la función set(). Sin embargo, las llaves {} se utilizan para inicializar un conjunto vacío, ya que {} se interpreta como un diccionario vacío. Por lo tanto, para inicializar un conjunto vacío, se debe utilizar set().
"""
conjunto: Set[Union[str, int]] = set()
otroConjunto: Set[Union[str, int]] = set()

print(type(conjunto), end = "\n", file = stdout)

"""
Si se inicializa un set con {} se inicializa como un diccionario
"""
print(type(otroConjunto), end = "\n", file = stdout)  # Inicialmente es un diccionario

otroConjunto = {"Daniel", "Perez", 35}
print(type(otroConjunto), end = "\n", file = stdout)

print(len(otroConjunto), end = "\n", file = stdout)


"""
Para añadir elementos a un set se usa el método add
"""
otroConjunto.add("DaniDev")

print(otroConjunto, end = "\n", file = stdout)  # Un set no es una estructura ordenada

otroConjunto.add("DaniDev")  # Un set no admite repetidos

print(otroConjunto, end = "\n", file = stdout)

# Búsqueda
"""
Para buscar un elemento en un set se usa la palabra reservada in
Que in es un operador de pertenencia
"""
print("Daniel" in otroConjunto, end = "\n", file = stdout)
print("Dani" in otroConjunto, end = "\n", file = stdout)

# Eliminación

"""
Para eliminar un elemento de un set se usa el método remove() se le pasa como argumento el elemento a eliminar
"""
otroConjunto.remove("Daniel")
print(otroConjunto)

"""
Para eliminar todos los elementos de un set se usa el método clear()
"""
otroConjunto.clear()
print(len(otroConjunto), end = "\n", file = stdout)

# Eliminación del set completo con el operador del que es un operador de eliminación

del otroConjunto
# print(otroConjunto) NameError: name 'otroConjunto' is not defined

# Transformación
"""
Podemos convertir un set a una lista con la función list()
"""
conjunto = {"Daniel", "Perez", 35}
lista: list[Union[str, int]] = list(conjunto)
print(lista, end = "\n", file = stdout)
print(lista[0], end = "\n", file = stdout)

otroConjunto = {"Rust", "Typescript", "Python"}

# Otras operaciones

"""
El método union() une dos sets y retorna un nuevo set con los elementos de ambos sets sin repetir los elementos repetidos. Se toma como parámetro el set con el que se quiere unir
"""
nuevoSet: Set[Union[str, int]] = conjunto.union(otroConjunto)
print(nuevoSet.union(nuevoSet).union(conjunto).union({"JavaScript", "Java"}))

"""
El método difference() retorna un nuevo set con los elementos que no se repiten entre dos sets

En este caso los elementos que no se repiten entre nuevoSet y conjunto
"""
print(nuevoSet.difference(conjunto), end = "\n", file = stdout)
