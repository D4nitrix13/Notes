"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
from typing import Dict, Union, Set, List
from sys import stdout

# Definición

"""
Los diccionarios son una estructura de datos que nos permite almacenar valores de diferente tipo, a diferencia de las listas, en lugar de acceder a los valores por un índice, lo hacemos por una llave. Las llaves pueden ser de tipo string o numérico. Los diccionarios son estructuras de datos mutables. Los diccionarios se definen con llaves {}. O también con la función dict(). 

La clave de un diccionario puede ser de cualquier tipo inmutable, como los números, cadenas o tuplas. Si intentamos usar como clave un tipo mutable como las listas, obtendremos un error de tipo TypeError. La clave es un identificador único para cada elemento dentro de un diccionario. Si intentamos crear un diccionario con dos claves iguales, se sobrescribirá el valor de la primera clave.

>>> ventajas de los diccionarios:

- Los diccionarios son estructuras de datos muy eficientes para buscar y almacenar valores.

- Los diccionarios son estructuras de datos muy flexibles para representar información.

- Los diccionarios son estructuras de datos muy eficientes para representar información proveniente de bases de datos.

>>> desventajas de los diccionarios:

- Los diccionarios no tienen un orden definido, por lo que no podemos esperar que los elementos se mantengan en un orden específico.

- Los diccionarios no son estructuras de datos eficientes en el uso de memoria, debido a que almacenan la información en forma de clave:valor, por lo que cada elemento del diccionario almacena dos valores.

"""
# En Python, el operador | se utiliza como el operador de "or" a nivel de bits (bitwise OR). Este operador realiza una operación OR a nivel de bits entre los operandos en una representación binaria.
# Operación a nivel de bits: El operador | toma dos números y realiza una operación OR a nivel de bits en sus representaciones binarias.
dicccionario: Dict[Union[str, int], Union[str, int, Set[str], float]] = dict()
otroDicccionario: Dict[Union[str, int], Union[str, int, Set[str], float]] = {}
otraForma = dict(
    Nombre = "Daniel",
    Apellido = "Perez",
    Edad = 18,
    Lenguajes = {"Python", "Rust", "Typescript"},
    Altura = 1.77,
)


print(type(dicccionario), end = "\n", file = stdout)
print(type(otroDicccionario), end = "\n", file = stdout)

otroDicccionario = {
    "Nombre": "Daniel",
    "Apellido": "Perez",
    "Edad": 35,
    1: "Python"
}

dicccionario = {
    "Nombre": "Daniel",
    "Apellido": "Perez",
    "Edad": 35,
    "Lenguajes": {"Python", "Rust", "Typescript"},
    1: 1.77
}

print(otroDicccionario, end = "\n", file = stdout)
print(dicccionario, end = "\n", file = stdout)

print(
    len(otroDicccionario), end = "\n", file = stdout
)  # Cantidad de elementos en el diccionario en total serian 4. Nombre, Apellido, Edad, 1 no se cuentan los valores de los conjuntos
print(
    len(dicccionario), end = "\n", file = stdout
)  # Cantidad de elementos en el diccionario en total serian 5. Nombre, Apellido, Edad, Lenguajes, 1 no se cuentan los valores de los conjuntos

# Búsqueda
"""
Para buscar un valor en un diccionario, debemos usar la llave correspondiente. Si la llave no existe, obtendremos un error de tipo KeyError. Para evitar este error, podemos usar el método get, que recibe como parámetro la llave a buscar y un valor por defecto que se retornará en caso de que la llave no exista.

Usamos el [] para buscar un valor en un diccionario, pero también para insertar o actualizar un valor. Si la llave existe, se actualizará el valor, si la llave no existe, se insertará el valor.
"""
print(dicccionario[1], end = "\n", file = stdout)
print(dicccionario["Nombre"], end = "\n", file = stdout)


# El operador de pertenencia in nos permite saber si una llave existe en un diccionario. Nos retorna True si la llave existe y False si no existe. Si queremos saber si un valor existe en un diccionario, debemos usar el método values.
print("Perez" in dicccionario, end = "\n", file = stdout)
print("Apellido" in dicccionario, end = "\n", file = stdout)

# Inserción
"""
Para insertar un valor en un diccionario, debemos usar el [] y asignarle un valor. Si la llave existe, se actualizará el valor, si la llave no existe, se insertará el valor.
"""
dicccionario["Calle"] = "Calle DaniDev"
print(dicccionario, end = "\n", file = stdout)

# Actualización
"""
Para actualizar un valor en un diccionario, debemos usar el [] y asignarle un valor. Si la llave existe, se actualizará el valor, si la llave no existe, se insertará el valor.
"""
dicccionario["Nombre"] = "Benjamin"
print(dicccionario["Nombre"], end = "\n", file = stdout)

# Eliminación

"""
Para eliminar un valor en un diccionario, debemos usar el método pop, que recibe como parámetro la llave a eliminar y retorna el valor eliminado. Si la llave no existe, obtendremos un error de tipo KeyError. Para evitar este error, podemos usar el método pop, que recibe como parámetro la llave a eliminar y un valor por defecto que se retornará en caso de que la llave no exista. También podemos usar la palabra reservada del, que recibe como parámetro la llave a eliminar. Si la llave no existe, obtendremos un error de tipo KeyError. Para evitar este error, podemos usar el método pop, que recibe como parámetro la llave a eliminar y un valor por defecto que se retornará en caso de que la llave no exista.
"""
del dicccionario["Calle"]
print(dicccionario, end = "\n", file = stdout)

# Esta variable almacenara el valor eliminado de la llave "Nombre" en caso de que exista, en caso de que no exista almacenara None
valorEliminado: Union[str, int, Set[str], float, None] = dicccionario.pop("Nombre", None)

print(dicccionario, end = "\n", file = stdout)

print(valorEliminado, end = "\n", file = stdout)


# Otras operaciones
"""
el metodo items() nos permite obtener una lista de tuplas, donde cada tupla contiene la llave y el valor de cada elemento del diccionario. 
El método keys() nos permite obtener una lista con todas las llaves del diccionario. 

El método values() nos permite obtener una lista con todos los valores del diccionario.
"""
print(dicccionario.items(), end = "\n", file = stdout)
print(dicccionario.keys(), end = "\n", file = stdout)
print(dicccionario.values(), end = "\n", file = stdout)

lista: List[Union[str, int]] = ["Nombre", 1, "Piso"]

"""
El método fromkeys() nos permite crear un diccionario a partir de una lista de llaves. El método fromkeys() recibe como primer parámetro la lista de llaves y como segundo parámetro un valor por defecto para todas las llaves. Si no se especifica el segundo parámetro, el valor por defecto será None.

Poner entre parentesis la lista, tupla o conjunto, es para que el metodo fromkeys() reciba un iterable, y no una lista de argumentos.
"""

nuevoDiccionario: Dict[Union[str, int], Union[str, int, Set[str], float, None]] = dict.fromkeys(
    lista, "Valor por defecto"
)

print(nuevoDiccionario, end = "\n", file = stdout)

nuevoDiccionario = dict.fromkeys(
    ("Nombre", 1, "Piso"), None
)

print(nuevoDiccionario, end = "\n", file = stdout)

nuevoDiccionario = dict.fromkeys(
    (dicccionario), None
)
print(nuevoDiccionario, end = "\n", file = stdout)

nuevoDiccionario = dict.fromkeys(dicccionario, "DaniDev")
print(nuevoDiccionario, end = "\n", file = stdout)

valor = nuevoDiccionario.values()
print(type(valor), end = "\n", file = stdout)

print(nuevoDiccionario.values(), end = "\n", file = stdout)

"""
Esta linea de codigo nos permite obtener una lista de los valores del diccionario, sin repetir ninguno, es decir, si hay dos valores iguales, solo se mostrara uno.

>>> list() convierte el objeto en una lista
>>> dict.fromkeys() convierte el objeto en un diccionario
>>> .values() obtiene los valores del diccionario
>>> keys() obtiene las llaves del diccionario

"""
print(list(set(nuevoDiccionario.values())), end = "\n", file = stdout)
print(tuple(nuevoDiccionario), end = "\n", file = stdout)
print(set(nuevoDiccionario), end = "\n", file = stdout)

