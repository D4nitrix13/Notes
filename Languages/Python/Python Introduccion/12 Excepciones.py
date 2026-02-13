"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Excepciones

from sys import stdout
from typing import Union


numeroUno: int = 5
numeroDos: int = 1
numeroTres: str = "1"

# Excepción base: try except

"""
Para manejar las excepciones se utiliza la palabra reservada try seguida de dos puntos y en la siguiente línea se escribe el código que se quiere ejecutar y que puede producir una excepción

Si se produce una excepción se ejecuta el código que está dentro del bloque except y si no se produce una excepción se ejecuta el código que está dentro del bloque else

El bloque finally se ejecuta siempre
"""
try:
    # Este código puede producir una excepción
    if isinstance(numeroUno, (int, float)) and isinstance(numeroTres, (int, float)): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)
    elif isinstance(numeroUno, str) and isinstance(numeroTres, str): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)
    
    print("No se ha producido un error", end = "\n", file = stdout)
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error", end = "\n", file = stdout)

# Flujo completo de una excepción: try except else finally

"""
>>> Primero se ejecuta el código que está dentro del bloque try 

>>> y si se produce una excepción se ejecuta el código que está dentro del bloque except 

>>> y si no se produce una excepción se ejecuta el código que está dentro del bloque else

>>> para finalizar se ejecuta el código que está dentro del bloque finally
"""
try:
    
    # Este código puede producir una excepción
    if isinstance(numeroUno, (int, float)) and isinstance(numeroTres, (int, float)): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)
    elif isinstance(numeroUno, str) and isinstance(numeroTres, str): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)

    print("No se ha producido un error", end = "\n", file = stdout)
except:
    print("Se ha producido un error", end = "\n", file = stdout)
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente", end = "\n", file = stdout)
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa", end = "\n", file = stdout)

# Excepciones por tipo

"""
Podemos capturar excepciones por tipo, para ello debemos indicar el tipo de excepción que queremos capturar después de la palabra reservada except
"""

try:
    # Este código puede producir una excepción
    if isinstance(numeroUno, (int, float)) and isinstance(numeroTres, (int, float)): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)
    elif isinstance(numeroUno, str) and isinstance(numeroTres, str): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)

    print("No se ha producido un error", end = "\n", file = stdout)
except ValueError:
    print("Se ha producido un ValueError", end = "\n", file = stdout)
except TypeError:
    print("Se ha producido un TypeError", end = "\n", file = stdout)

# Captura de la información de la excepción

"""
Podemos capturar la información de la excepción con la palabra reservada as que se utiliza después del tipo de excepción para asignar la información de la excepción a una variable y así poder utilizarla dentro del bloque except. la variable que se utiliza para capturar la información de la excepción puede tener cualquier nombre
"""

try:
    # Este código puede producir una excepción
    if isinstance(numeroUno, (int, float)) and isinstance(numeroTres, (int, float)): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)
    elif isinstance(numeroUno, str) and isinstance(numeroTres, str): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)

    print("No se ha producido un error", end = "\n", file = stdout)
except ValueError as error:
    # ValueError es una excepción que se produce cuando se intenta convertir un valor a un tipo de dato que no es compatible con el valor que se quiere convertir. Este error lo almacena la variable error
    print(error, end = "\n", file = stdout)
except Exception as errorRandom:
    # Exception es la clase base de todas las excepciones de Python y se utiliza para capturar cualquier excepción que no se haya capturado antes
    print(errorRandom, end = "\n", file = stdout)

# otra manera para capturar myltiples excepciones

try:
    # Este código puede producir una excepción
    if isinstance(numeroUno, (int, float)) and isinstance(numeroTres, (int, float)): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)
    elif isinstance(numeroUno, str) and isinstance(numeroTres, str): 
        print(numeroUno + numeroTres, end = "\n", file = stdout)

    print("No se ha producido un error", end = "\n", file = stdout)
except (ValueError,Exception) as error:
    # En este caso se capturan dos tipos de excepciones en un solo bloque except con una tupla de excepciones separadas por comas y se asigna la información de la excepción a la variable error
    print(error, end = "\n", file = stdout)

