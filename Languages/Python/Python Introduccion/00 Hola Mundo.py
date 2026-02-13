"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Hola Mundo

# Nuestro hola mundo en Python
from sys import stdout


print("Hola Python", end = "\n", file = stdout)
print("Hola Python", end = "\n", file = stdout)

# Esto es un comentario

"""
Este es un
comentario
en varias líneas
"""

"""
Este también es un
comentario
en varias líneas
"""

# Cómo consultar el tipo de dato
"""
En los lenjuages de programación, es importante saber el tipo de dato que estamos utilizando
para poder realizar las operaciones adecuadas.
>>> 1. str: Cadena de texto
>>> 2. int: Número entero
>>> 3. float: Número decimal
>>> 4. complex: Número complejo
>>> 5. bool: Valor booleano
>>> 6. NoneType: Valor nulo
"""


"""
>>> print() es una función que nos permite imprimir en consola el valor que le pasemos como parámetro.

>>> type() es una función que nos permite saber el tipo de dato que estamos utilizando.
"""
print(type("Soy un dato str"), end = "\n", file = stdout)  # Tipo 'str'
print(type(5), end = "\n", file = stdout)  # Tipo 'int'
print(type(1.5), end = "\n", file = stdout)  # Tipo 'float'
print(type(3 + 1j), end = "\n", file = stdout)  # Tipo 'complex'
print(type(True), end = "\n", file = stdout)  # Tipo 'bool'
print(type(print("Mi cadena de texto")), end = "\n", file = stdout)  # Tipo 'NoneType'
