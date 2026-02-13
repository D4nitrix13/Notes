"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Temas: Condicionales, if, elif, else, ispección de valor, match case

"""
if es una palabra reservada de python que se utiliza para hacer condicionales
"""

from sys import stdout
from typing import List, Union


condicion: Union[bool, int] = False

"""
Este tipo de if se llama "if sin condición" o "if sin expresión". En Python, es válido escribir un if sin una condición explícita. En este caso, el bloque de código dentro del if se ejecutará si la condición es evaluada como verdadera. Sin embargo, ten en cuenta que si no se proporciona una condición, el if siempre se considerará verdadero y el bloque de código se ejecutará en cada iteración o llamada.

En la mayoría de los casos, es mejor evitar este tipo de if. Siempre que sea posible, es mejor proporcionar una condición explícita para que el código sea más legible y menos propenso a errores.

En Python, los valores que se evalúan como verdaderos se denominan valores truthy, mientras que los valores que se evalúan como falsos se denominan valores falsy. Los valores truthy y falsy son una característica de Python que se utiliza para evaluar los valores booleanos de los objetos. Por ejemplo, los valores truthy y falsy se utilizan en las declaraciones if para evaluar si una condición es verdadera o falsa.

Los siguientes valores se evalúan como falsos en Python:    
>>> False

>>> None

>>> Cualquier número igual a cero (0, 0.0, 0j). int, float, complex
Cualquier secuencia vacía (cadena vacía, lista vacía, tupla vacía). "",'',[],()
es un set el ultimo

>>> Cualquier conjunto vacío (conjunto vacío, diccionario vacío) set(), {}
>>> Cualquier objeto cuya implementación de __bool__ devuelva False o __len__ devuelva 0
"""
if condicion:  # Es lo mismo que if condicion == True:
    print("Se ejecuta la condición del if", end = "\n", file = stdout)

condicion = 5 * 5

"""
Esto es un if con condición o if con expresión
if condicion == 10:
"""
if condicion == 10:
    print("Se ejecuta la condición del segundo if", end = "\n", file = stdout)

# if, elif, else
"""
>>> if es una palabra reservada de python que se utiliza para hacer condicionales y se ejecuta cuando se cumple la condición del if

>>> elif es una palabra reservada de python que se utiliza para hacer condicionales y se ejecuta cuando no se cumple la condición del if

>>> else es una palabra reservada de python que se utiliza para hacer condicionales y se ejecuta cuando no se cumple ninguna condición

"""
if condicion > 10 and condicion < 20:
    print("Es mayor que 10 y menor que 20", end = "\n", file = stdout)
elif condicion == 25:
    print("Es igual a 25", end = "\n", file = stdout)
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25", end = "\n", file = stdout)

print("La ejecución continúa", end = "\n", file = stdout)

# Condicional con ispección de valor

string: str = ""
"""
Al poner not antes de una condición se niega la condición 
>>> si la condición es True se vuelve False
>>> si la condición es False se vuelve True
"""
if not string:
    print("Mi cadena de texto es vacía", end = "\n", file = stdout)

if string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden", end = "\n", file = stdout)


"""
El match es una nueva palabra reservada de python que se utiliza para hacer condicionales y se ejecuta cuando se cumple la condición del match y se puede utilizar para hacer condicionales con valores de una variable o de una expresión. También se puede utilizar para hacer condicionales con valores de una lista, tupla, set, diccionario o cualquier otro tipo de colección de datos o estructura de datos 
"""

edad: int = 18

match edad:
    case 18:
        print("Eres mayor de edad", end = "\n", file = stdout)
    case 17:
        print("Eres menor de edad", end = "\n", file = stdout)
    case 5:
        print("Eres un niño", end = "\n", file = stdout)

"""
Dentro de case se puede poner una condición para hacer match con un valor
"""
match edad:
    case edad if edad >= 18:
        print("Eres mayor de edad", end = "\n", file = stdout)
    case edad if edad < 18 and edad >= 5:
        print("Eres menor de edad", end = "\n", file = stdout)
    case edad if edad <= 5 and edad >= 1:
        print("Eres un niño", end = "\n", file = stdout)

nombre: str = "Daniel"

match nombre:
    case "Daniel":
        print("Tu nombre es Daniel", end = "\n", file = stdout)
    case "Danna":
        print("Tu nombre es Danna", end = "\n", file = stdout)
    case "Matias":
        print("Tu nombre es Pedro", end = "\n", file = stdout)

listaFrutas: List[str] = ["manzana", "pera", "uva"]

"""
Se puede hacer match con una lista, tupla, set, diccionario o cualquier otro tipo de colección de datos o estructura de datos
"""
match listaFrutas:
    case ["manzana", "pera", "uva"]:
        print("La lista contiene manzana, pera y uva", end = "\n", file = stdout)
    case ["manzana", "pera"]:
        print("La lista tiene manzana y pera", end = "\n", file = stdout)
    case ["manzana"]:
        print("La lista contiene una manzana", end = "\n", file = stdout)
    case []:
        print("La lista esta vacía", end = "\n", file = stdout)

letra: str = "a"

match letra:
    case "a":
        print("La letra es a", end = "\n", file = stdout)
    case "b":
        print("La letra es b", end = "\n", file = stdout)
    case _:
        print("La letra no es a ni b", end = "\n", file = stdout)
"""
el _ es un comodín que se utiliza para hacer match con cualquier valor
"""
