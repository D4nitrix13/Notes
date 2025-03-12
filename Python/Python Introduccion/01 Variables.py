"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Variables

from sys import stdout
from typing import Union


string: str = "My String variable"
print(string)

integer: int = 5
print(integer, end = "\n", file = stdout)

convercionDeIntegerAString: str = str(integer)
print(
    convercionDeIntegerAString,
    end = "\n", file = stdout,
)
print(
    type(convercionDeIntegerAString),
    end = "\n", file = stdout,
)

booleano: bool = False
print(
    booleano,
    end = "\n", file = stdout
)

flotante: float = 1.2
# Concatenación de variables en un print
print(string, convercionDeIntegerAString, booleano, flotante, end = "\n", file = stdout)
print("Este es el valor de:", booleano, end = "\n", file = stdout)

# Algunas funciones del sistema

"""
len() es una función que nos permite saber la longitud de una cadena de texto
"""
print(len(string), end = "\n", file = stdout)

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!

nombre: Union[str, int, None] = None
segundoNombre: Union[str, None] = None
alias: Union[str, None] = None
edad: Union[int, str, None] = None

nombre, segundoNombre, alias, edad = "Daniel", "Perez", "DaniDev", 18
print(
    "Me llamo:",
    nombre,
    segundoNombre,
    ". Mi edad es:",
    edad,
    ". Y mi alias es:",
    alias,
    end = "\n", file = stdout
)

# Inputs
nombre = str(input("¿Cuál es tu nombre? "))
edad = int(input("¿Cuántos años tienes? "))
print(nombre, end="\n", file=stdout)
print(edad, end="\n", file=stdout)

# Cambiamos su tipo
nombre = 35
# ! Esto es un error de tipo de dato en python
# ! pero no da error en tiempo de ejecución por que es un lenguaje interpretado y no compilado
edad = "Daniel"

print(nombre, end="\n", file=stdout)
print(edad, end="\n", file=stdout)

"""
Cambiamos su tipo en python las variables son dinámicas
Lo que quiere decir que podemos cambiar el tipo de dato de una variable en cualquier momento

En otros lenguajes de programación, las variables son estáticas
Lo que quiere decir que una vez que le asignamos un tipo de dato a una variable, no podemos cambiarlo
"""
direccion: Union[str, bool, int , float] = "Mi dirección"
direccion = True
direccion = 5
direccion = 1.2
print(type(direccion), end = "\n", file = stdout)


# Constantes
""" 
En python no existen las constantes, pero se pueden simular con mayúsculas y guiones bajos. Se usa para indicar que una variable no debe ser modificada en el futuro

Las constantes se suelen definir al principio del fichero o al principio de una clase Y puden tener cualquier tipo de dato
"""
FLOTANTE: float = 1.2
CADENA: str = "Mi cadena"
BOOLEANO: bool = True
ENTERO: int = 5
print(ENTERO, end = "\n", file = stdout)
