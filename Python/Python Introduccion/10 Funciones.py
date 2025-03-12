"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Funciones
"""
Paradigma: funcional es un paradigma de programación que se basa en funciones y en la programación declarativa
"""
# Definición
"""
Para definir una función se utiliza la palabra reservada def
seguido del nombre de la función y los paréntesis de apertura y cierre

la estructura de una función es la siguiente

>>> def es una palabra reservada de python que se utiliza para definir una función
>>> my_funcion es el nombre de la función puede tener cualquier nombre que no sea una palabra reservada de python
>>> () son los paréntesis de apertura y cierre de la función y dentro de ellos se pueden poner los parámetros de entrada de la función

>>> -> es el operador de retorno que se utiliza para indicar el tipo de dato que retornará la función y se puede omitir si la función no retorna nada o podemos poner None si la función no retorna nada 

>>> None es un tipo de dato que se utiliza para indicar que una variable no tiene ningún valor podemos decir que es el equivalente a null en otros lenguajes de programación
"""


from sys import stdout
from typing import Any, Dict, Union, NoReturn


def my_funcion() -> None:
    print("Esto es una función", end = "\n", file = stdout)
    return None


my_funcion()
my_funcion()
my_funcion()

# Función con parámetros de entrada/argumentos

# Union es un tipo especial en Python utilizado para indicar que una variable puede tener uno de varios tipos diferentes. Se importa del módulo typing, y se utiliza para definir una variable que puede contener valores de diferentes tipos especificados.

def sumar_dos_valores(*, primerValor: Union[int, str, float], segundoValor: Union[int, str, float]) -> Union[None, NoReturn]:
    resultado: Union[str, int, float, None] = None
    if isinstance(primerValor, (int, float)) and isinstance(segundoValor, (int, float)): resultado = primerValor + segundoValor
    elif isinstance(primerValor, str) and isinstance(segundoValor, str): resultado = primerValor + segundoValor
    else: raise TypeError("Los tipos de los operandos no son compatibles para la suma.")
    return None

sumar_dos_valores(primerValor = 5, segundoValor = 7)
sumar_dos_valores(primerValor = 54754, segundoValor = 71231)
sumar_dos_valores(primerValor = "5", segundoValor = "7")
sumar_dos_valores(primerValor = 1.4, segundoValor = 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sumar_dos_valores_con_retorno(*, primerValor: Union[int, str, float], segundoValor: Union[int, str, float]) -> Union[int, str, float, None, NoReturn]:

    suma: Union[str, int, float, None] = None
    if isinstance(primerValor, (int, float)) and isinstance(segundoValor, (int, float)): suma = primerValor + segundoValor
    elif isinstance(primerValor, str) and isinstance(segundoValor, str): suma = primerValor + segundoValor
    else: raise TypeError("Los tipos de los operandos no son compatibles para la suma.")

    return suma


# Podemos asignar el valor que retorna una función a una variable para utilizarlo más tarde Si la función no retorna nada la variable tendrá el valor None
resultado: Union[int, str, float, None] = sumar_dos_valores(primerValor = 1.4, segundoValor = 5.2)
print(resultado, end = "\n", file = stdout)

resultado = sumar_dos_valores_con_retorno(primerValor = 10, segundoValor = 5)
print(resultado, end = "\n", file = stdout)

# Función con parámetros de entrada/argumentos por clave


def imprimir_nombre(*, nombre: str, segundoNombre: str) -> None:
    print(f"{nombre} {segundoNombre}", end = "\n", file = stdout)
    return None


imprimir_nombre(segundoNombre="Benjamin", nombre="Perez")

# Función con parámetros de entrada/argumentos por defecto


# Podemos indicarle a un parámetro que tenga un valor por defecto si no se le pasa ningún valor al llamar la función y si se le pasa un valor al llamar la función se sobreescribirá el valor por defecto del parámetro por el valor que se le pasó al llamar la función


def imprimir_con_valores_por_defecto(
    *, nombre: str, segundoNombre: str , alias: Union[int, str, float, bool] = "Sin alias"
) -> None:
    print(f"{nombre} {segundoNombre} {alias}", end = "\n", file = stdout)
    return None


imprimir_con_valores_por_defecto(nombre = "Daniel", segundoNombre = "Benjamin")
imprimir_con_valores_por_defecto(nombre = "Daniel", segundoNombre = "Benjamin", alias = "BenjaminDev")

# Función con parámetros de entrada/argumentos arbitrarios

"""
* Es el operador de parámetros de entrada/argumentos arbitrarios que se utiliza para indicar que la función puede recibir un número indeterminado de parámetros de entrada/argumentos y se pueden utilizar en la función como una tupla de datos y se puede utilizar cualquier nombre para el parámetro de entrada/argumento arbitrario
"""


def imprimir_texto_en_mayuscula(*args: str) -> None:
    print(type(args), end = "\n", file = stdout)
    for texto in args: print(texto.upper(), end = "\n", file = stdout)
    return None


imprimir_texto_en_mayuscula("Hola", "Python", "BenjaminDev")
imprimir_texto_en_mayuscula("Hola")

"""
Función con parámetros de entrada/argumentos arbitrarios por clave
"""


def imprimir_texto_en_mayuscula_por_clave(**kwargs: Any) -> None:
    print(type(kwargs), end = "\n", file = stdout)
    for texto in kwargs: print(texto.upper(), end = "\n", file = stdout)
    return None


# Podemos pasar los parámetros de entrada/argumentos arbitrarios por clave de la siguiente manera clave=valor

"""
Otra manera es crear un diccionario y pasarle el diccionario a la función de la siguiente manera **diccionario o el nombre que le hayamos puesto al parámetro de entrada/argumento arbitrario por clave
"""

diccionario: Dict[str, str] = {
    "Texto1": "Hola",
    "Texto2": "Rust",
    "Texto3": "DanielDev",
}
imprimir_texto_en_mayuscula_por_clave(**diccionario)

imprimir_texto_en_mayuscula_por_clave(clave1 = "Hola", clave2 = "Python", clave3 = "BenjaminDev")


"""
>>> Con el operador * que se llama operador de desempaquetado podemos pasar una lista o una tupla a una funcion.

>>> Con el operador ** que se llama operador de desempaquetado podemos pasar un diccionario a una funcion.

Podemos tener ambos operadores en una misma función
"""


def imprimir_texto_en_mayuscula_con_desempaquetado(*args: str, **kwargs: Any) -> None:
    print(type(args), end = "\n", file = stdout)
    print(type(kwargs), end = "\n", file = stdout)
    for texto in args: print(texto.upper(), end = "\n", file = stdout)
    for texto in kwargs: print(texto.upper(), end = "\n", file = stdout)
    return None


imprimir_texto_en_mayuscula_con_desempaquetado(
    "Hola", "Python", "BenjaminDev", **diccionario
)


imprimir_texto_en_mayuscula_con_desempaquetado(
    "Hola",
    "Python",
    "BenjaminDev",
    clave1 = "Hola",
    clave2 = "Python",
    clave3 = "BenjaminDev",
)

"""
function asynchroneas  funciones asincronas

>>> Es una función que se ejecuta de manera asincrona lo que significa que se ejecuta en un hilo diferente al hilo principal y se puede ejecutar al mismo tiempo que otras funciones asincronas o funciones sincronas es decir que no se bloquea el hilo principal, esto es muy util para hacer peticiones a una API o a una base de datos sin bloquear el hilo principal

>>> Para definir una función asincrona se utiliza la palabra reservada async seguido de la palabra reservada def y el nombre de la función y los paréntesis de apertura y cierre

>>> para ejecutar una función asincrona se utiliza la palabra reservada await seguido del nombre de la función y los paréntesis de apertura y cierre

Para usar funciones asiincronas se debe de usar el modulo asyncio
"""

import asyncio


async def my_funcion_asincrona(nombre: str) -> str:
    return "Esto es una función asincrónica {}".format(nombre)


# Ejecutar la función asincrona
resultado_de_funcion_asincrona: str = asyncio.run(
    main = my_funcion_asincrona(nombre = "BenjaminDev")
)
print(resultado_de_funcion_asincrona, end = "\n", file = stdout)
print(asyncio.run(main = my_funcion_asincrona(nombre = "DanielDev")), end = "\n", file = stdout)
