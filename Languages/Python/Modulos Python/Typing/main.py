#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout
from typing import Callable, Dict, FrozenSet, List, Optional, Set, Tuple, Type, TypeVar, Union, NoReturn, Any, Protocol

# Variables

# Cadena de texto (string)
# Un conjunto de caracteres Unicode que representan texto.
# Ejemplo: "Daniel"
string: str = "Daniel"

# Entero (int)
# Un número entero, positivo o negativo, sin decimales.
# Ejemplo: 18
integer: int = 18

# Número de punto flotante (float)
# Un número que puede contener decimales.
# Ejemplo: 20.0
flotante: float = 20.0

# Número complejo (complex)
# Un número que tiene una parte real y una parte imaginaria.
# Ejemplo: 10j (donde la parte real es 0 y la imaginaria es 10)
numeroComplex: complex = 10j

# Valor booleano (bool)
# Un valor que puede ser True (verdadero) o False (falso).
# Ejemplo: True
booleano: bool = True

# Ningún valor (None)
# Representa la ausencia de un valor o un valor nulo.
# Ejemplo: None
nada: None = None

# Estructuras De Datos De Un Solo Tipo

# Lista de cadenas de texto (List[str])
# Una colección ordenada y mutable de elementos de tipo cadena.
# Ejemplo: ["Daniel", "Perez"]
listaString: List[str] = ["Daniel", "Perez"]

# Lista de enteros (List[int])
# Una colección ordenada y mutable de elementos de tipo entero.
# Ejemplo: [18, 20]
listaInteger: List[int] = [18, 20]

# Lista de números de punto flotante (List[float])
# Una colección ordenada y mutable de elementos de tipo flotante.
# Ejemplo: [100.5, 500.10]
listaFloat: List[float] = [100.5, 500.10]

# Lista de números complejos (List[complex])
# Una colección ordenada y mutable de elementos de tipo complejo.
# Ejemplo: [100j, 200j]
listaComplex: List[complex] = [100j, 200j]

# Lista de valores booleanos (List[bool])
# Una colección ordenada y mutable de elementos de tipo booleano.
# Ejemplo: [True, False]
listaBooleano: List[bool] = [True, False]

# Lista de valores None (List[None])
# Una colección ordenada y mutable de elementos de tipo None.
# Ejemplo: [None, None]
listaNone: List[None] = [None, None]

# Tupla de cadenas de texto (Tuple[str, str])
# Una colección ordenada e inmutable de un número fijo de elementos de tipo cadena.
# Ejemplo: ("Daniel", "Perez")
TuplaString: Tuple[str, str] = ("Daniel", "Perez")

# Tupla de enteros (Tuple[int, int])
# Una colección ordenada e inmutable de un número fijo de elementos de tipo entero.
# Ejemplo: (18, 20)
TuplaInteger: Tuple[int, int] = (18, 20)

# Tupla de números de punto flotante (Tuple[float, float])
# Una colección ordenada e inmutable de un número fijo de elementos de tipo flotante.
# Ejemplo: (100.5, 500.10)
TuplaFloat: Tuple[float, float] = (100.5, 500.10)

# Tupla de números complejos (Tuple[complex, complex])
# Una colección ordenada e inmutable de un número fijo de elementos de tipo complejo.
# Ejemplo: (100j, 200j)
TuplaComplex: Tuple[complex, complex] = (100j, 200j)

# Tupla de valores booleanos (Tuple[bool, bool])
# Una colección ordenada e inmutable de un número fijo de elementos de tipo booleano.
# Ejemplo: (True, False)
TuplaBooleano: Tuple[bool, bool] = (True, False)

# Tupla de valores None (Tuple[None, None])
# Una colección ordenada e inmutable de un número fijo de elementos de tipo None.
# Ejemplo: (None, None)
TuplaNone: Tuple[None, None] = (None, None)

# Conjunto de cadenas de texto (Set[str])
# Una colección desordenada y mutable de elementos únicos de tipo cadena.
# Ejemplo: {"Daniel", "Perez"}
SetString: Set[str] = {"Daniel", "Perez"}

# Conjunto de enteros (Set[int])
# Una colección desordenada y mutable de elementos únicos de tipo entero.
# Ejemplo: {18, 20}
SetInteger: Set[int] = {18, 20}

# Conjunto de números de punto flotante (Set[float])
# Una colección desordenada y mutable de elementos únicos de tipo flotante.
# Ejemplo: {100.5, 500.10}
SetFloat: Set[float] = {100.5, 500.10}

# Conjunto de números complejos (Set[complex])
# Una colección desordenada y mutable de elementos únicos de tipo complejo.
# Ejemplo: {100j, 200j}
SetComplex: Set[complex] = {100j, 200j}

# Conjunto de valores booleanos (Set[bool])
# Una colección desordenada y mutable de elementos únicos de tipo booleano.
# Ejemplo: {True, False}
SetBooleano: Set[bool] = {True, False}

# Conjunto de valores None (Set[None])
# Una colección desordenada y mutable de elementos únicos de tipo None.
# Ejemplo: {None, None}
SetNone: Set[None] = {None, None}

# Diccionario de cadenas de texto (Dict[str, str])
# Una colección desordenada y mutable de pares clave-valor, donde las claves y los valores son de tipo cadena.
# Ejemplo: {"Daniel": "Perez"}
DiccionarioString: Dict[str, str] = {"Daniel": "Perez"}

# Diccionario de enteros (Dict[int, int])
# Una colección desordenada y mutable de pares clave-valor, donde las claves y los valores son de tipo entero.
# Ejemplo: {18: 20}
DiccionarioInteger: Dict[int, int] = {18: 20}

# Diccionario de números de punto flotante (Dict[float, float])
# Una colección desordenada y mutable de pares clave-valor, donde las claves y los valores son de tipo flotante.
# Ejemplo: {100.5: 500.10}
DiccionarioFloat: Dict[float, float] = {100.5: 500.10}

# Diccionario de números complejos (Dict[complex, complex])
# Una colección desordenada y mutable de pares clave-valor, donde las claves y los valores son de tipo complejo.
# Ejemplo: {100j: 200j}
DiccionarioComplex: Dict[complex, complex] = {100j: 200j}

# Diccionario de valores booleanos (Dict[bool, bool])
# Una colección desordenada y mutable de pares clave-valor, donde las claves y los valores son de tipo booleano.
# Ejemplo: {True: False}
DiccionarioBooleano: Dict[bool, bool] = {True: False}

# Diccionario de valores None (Dict[None, None])
# Una colección desordenada y mutable de pares clave-valor, donde las claves y los valores son de tipo None.
# Ejemplo: {None: None}
DiccionarioNone: Dict[None, None] = {None: None}


# Datos Especiales

# Any (Cualquiera)
# Representa cualquier tipo de dato. Se puede reasignar a diferentes tipos sin restricciones.
# Ejemplo: Puede ser un string, un entero, un float, un complejo, un booleano, None, lista, tupla, conjunto o diccionario.

cualquiera: Any = "Daniel"  # Cadena de texto
cualquiera = 18  # Entero
cualquiera = 100.10  # Número de punto flotante
cualquiera = 20j  # Número complejo
cualquiera = True  # Valor booleano
cualquiera = None  # Ningún valor
cualquiera = ["Perez", 13, 18.13, 100j, True, None]  # Lista con varios tipos de datos
cualquiera = ("Perez", 13, 18.13, 100j, True, None)  # Tupla con varios tipos de datos
cualquiera = {"Perez", 13, 18.13, 100j, True, None}  # Conjunto con varios tipos de datos
cualquiera = {
   "String": "Perez", 
   ("Numero", True, 18.13, 108j, 10, None): 13, 
   True: None
}  # Diccionario con claves y valores de varios tipos de datos


# Estructura De Datos De Múltiples Tipos

# Union
# `Union` permite que una variable pueda ser de cualquiera de los tipos especificados.
# Aquí usamos `Union` para indicar que los elementos de las estructuras de datos pueden ser de varios tipos.

# Lista que puede contener elementos de varios tipos: str, int, float, complex, bool, None
listaMultiple: List[Union[str, int, float, complex, bool, None]] = [
   "Daniel",  # Cadena de texto
   100,       # Entero
   18.10,     # Número de punto flotante
   300j,      # Número complejo
   True,      # Valor booleano
   None       # Ningún valor
]

# Tupla que puede contener elementos de varios tipos: str, int, float, complex, bool, None
# Elipsis en Tuple:
# En la anotación de tipos, Tuple[Tipo, ...] indica que la tupla puede contener un número arbitrario de elementos del tipo especificado.
# El uso de ... (elipsis) después del tipo significa que la tupla puede tener cero o más elementos de ese tipo.
tuplaMultiple: Tuple[Union[str, int, float, complex, bool, None], ...] = (
   "Daniel",  # Cadena de texto
   100,       # Entero
   18.10,     # Número de punto flotante
   300j,      # Número complejo
   True,      # Valor booleano
   None       # Ningún valor
)

# Conjunto que puede contener elementos de varios tipos: str, int, float, complex, bool, None
setMultiple: Set[Union[str, int, float, complex, bool, None]] = {
   "Daniel",  # Cadena de texto
   100,       # Entero
   18.10,     # Número de punto flotante
   300j,      # Número complejo
   True,      # Valor booleano
   None       # Ningún valor
}

# Diccionario que puede contener claves y valores de varios tipos: str, int, float, complex, bool, None
diccionarioMultiple: Dict[Union[str, int, float, complex, bool, None], Union[str, int, float, complex, bool, None]] = {
   "Nombre": "Daniel",   # Clave y valor son cadenas de texto
   18: 100,              # Clave y valor son enteros
   100.13: 18.10,        # Clave y valor son números de punto flotante
   200j: 300j,           # Clave y valor son números complejos
   True: False,          # Clave y valor son valores booleanos
   None: None            # Clave y valor son None
}


# Ejemplo de Lista anidada
# Lista que puede contener Tuplas de enteros o Sets de cadenas de texto, o ser None
listaAnidada: Optional[List[Union[Tuple[int, ...], Set[str]]]] = [
   {"Daniel", "Perez"},  # Set de cadenas de texto
   (1, 2, 3, 4, 5)       # Tupla de enteros
]

# Ejemplo de Tupla anidada
# Definimos un set de tuplas y frozensets
# Nota: El uso de frozenset para diccionarios es solo una solución parcial y no siempre es la más práctica, ya que los diccionarios tienen claves y valores, lo cual no se traduce directamente a frozenset. La elección depende del contexto específico de tu aplicación.

setAnidado: Set[Union[Tuple[int, ...], FrozenSet[Tuple[str, Union[str, int, float]]]]] = {
   (1, 2, 3),
   (4, 5, 6),
   frozenset({("key1", "value1"), ("key2", 42)}),  # Usando frozenset para representar un diccionario
}

# Ejemplo de Diccionario anidado
# Diccionario que puede tener claves de cadenas de texto y valores que pueden ser Listas, Tuplas o Sets de enteros
diccionarioAnidado: Dict[str, Union[List[int], Tuple[int, ...], Set[int]]] = {
   "lista": [1, 2, 3, 4, 5],     # Lista de enteros
   "tupla": (6, 7, 8, 9, 10),    # Tupla de enteros
   "set": {11, 12, 13, 14, 15}   # Set de enteros
}

# Ejemplo con Optional
# Diccionario que puede tener claves de cadenas de texto y valores que pueden ser Listas de enteros o None
diccionarioOptional: Dict[str, Optional[List[int]]] = {
   "valores": [1, 2, 3, 4, 5],  # Lista de enteros
   "Ningun Valor": None         # None
}


# Ejemplo de variable Optional
opcionalStr: Optional[str] = "Daniel"
opcionalStr = None

opcionalInt: Optional[int] = 18
opcionalInt = None

opcionalFloat: Optional[float] = 20.0
opcionalFloat = None

opcionalBool: Optional[bool] = True
opcionalBool = None

opcionalComplex: Optional[complex] = 10j
opcionalComplex = None

opcionalList: Optional[List[int]] = [1, 2, 3, 4, 5]
opcionalList = None

opcionalTuple: Optional[Tuple[str, ...]] = ("Daniel", "Perez", "Morales")
opcionalTuple = None

opcionalSet: Optional[Set[int]] = {1, 2, 3, 4, 5}
opcionalSet = None

opcionalDict: Optional[Dict[str, int]] = {"edad": 18}
opcionalDict = None

# Ejemplo de estructura de datos anidada con Optional
# Lista que puede contener Tuplas de enteros o None
listaOpcionalAnidada: List[Optional[Tuple[int, ...]]] = [
   (1, 2, 3),
   None,
   (4, 5, 6)
]

# Diccionario que puede tener claves de cadenas de texto y valores que pueden ser Listas de enteros o None
diccionarioOpcionalAnidado: Dict[str, Optional[List[int]]] = {
   "valores1": [1, 2, 3, 4, 5],  # Lista de enteros
   "valores2": None              # None
}

# Set que puede contener enteros o None
setOpcional: Set[Optional[int]] = {1, 2, 3, None}

# Tupla que puede contener cadenas de texto o None
tuplaOpcional: Tuple[Optional[str], Optional[str]] = ("Daniel", None)

from typing import List, Callable

# `map` aplica una función a cada ítem en una lista y devuelve un iterador
# Aquí convertimos cada string terminado en "$" a un entero
variableMap: map = map(lambda i: int(i[:-1]), [str(i) + "$" for i in range(50)])

# `filter` filtra los ítems en un iterador según una función de predicado
# Aquí filtramos los números que son divisibles por 3
variableFilter: filter = filter(lambda i: i % 3 == 0, variableMap)

# Si deseas convertir los resultados de `map` y `filter` a una lista, puedes hacerlo así:
listaMapeada: List[int] = list(variableMap)  # Convertir el resultado de `map` a una lista de enteros
listaFiltrada: List[int] = list(variableFilter)  # Convertir el resultado de `filter` a una lista de enteros

print(listaMapeada, end = "\n", file = stdout)
print(listaFiltrada, end = "\n", file = stdout)


from typing import NoReturn

def error(*, descripcionError: str) -> NoReturn:
   """
   Función que lanza una excepción con la descripción del error.
    
   :param descripcionError: Descripción del error que se incluirá en la excepción.
   :raises ValueError: Siempre lanza una excepción, por lo tanto, nunca retorna normalmente.
   """
   raise ValueError(descripcionError)  # Lanza una excepción que no permite que la función retorne normalmente

# Ejemplo de uso:
e: Optional[ValueError] = None
try:
   error(descripcionError = "Se ha producido un error inesperado")
except ValueError as e:
   print(f"Se capturó un error: {e}", end = "\n", file = stdout)

# Nota: Debido a que la función `error` nunca retorna normalmente, el código después de llamarla no se ejecutará.

from typing import Optional

class Juego:
    def __init__(self: "Juego", nombre: str) -> None:
      """
      Constructor de la clase Juego.
        
      :param nombre: Nombre del juego.
      """
      self.__nombre: str = nombre
      return None

    @property
    def nombre(self: "Juego") -> str:
      """
      Propiedad para obtener el nombre del juego.
      
      :return: El nombre del juego.
      """
      return self.__nombre  # Accede al atributo privado __nombre

    @nombre.setter
    def nombre(self: "Juego", nuevoNombre: str) -> None:
      """
      Propiedad para establecer un nuevo nombre al juego.
      
      :param nuevoNombre: El nuevo nombre del juego.
      """
      self.__nombre = nuevoNombre  # Asigna el nuevo nombre al atributo privado __nombre
      return None

    @nombre.deleter
    def nombre(self: "Juego") -> None:
      """
      Propiedad para eliminar el nombre del juego.
      """
      del self.__nombre  # Elimina el atributo privado __nombre
      return None


# Ejemplo de uso:
marioBros: Juego = Juego(nombre="Super Mario Bros")
print(marioBros.nombre, end = "\n", file = stdout)  # Debería imprimir "Super Mario Bros"

marioBros.nombre = "Mario Kart"
print(marioBros.nombre, end = "\n", file = stdout)  # Debería imprimir "Mario Kart"

del marioBros.nombre
# Intentar acceder a marioBros.nombre después de eliminarlo causará un AttributeError

# Definimos el protocolo Nombre correctamente
class Nombre(Protocol):
   def __call__(self, *, nombre: str) -> str:
      return nombre

# Funciones
def decorador(f: Nombre) -> Callable[[], str]:
   def funcion() -> str:
      nombre: str = "Daniel Benjamin Perez Morales"
      return f"Bienvenido {f(nombre = nombre).title()}"
   return funcion

@decorador
def name(*, nombre: str) -> str:
   return nombre

print(name(), end = "\n", file = stdout)

# En Python, Type es una forma de referirse a tipos de clases y tipos en general en la tipificación estática. Es parte del módulo typing, que proporciona herramientas para la tipificación en tiempo de desarrollo.
class Animal:
   def __init__(self: "Animal") -> None: return None
   def crear_sonido(self: "Animal") -> str:
      return "Some sound"

class Dog(Animal):
   def __init__(self: "Dog") -> None: 
      super().__init__()
      return None
   def crear_sonido(self: "Dog") -> str:
      return "Woof"

class Cat(Animal):
   def __init__(self: "Cat") -> None: 
      super().__init__()
      return None
   def crear_sonido(self: "Cat") -> str:
      return "Meow"

def crear_animal(*, animalType: Type[Animal]) -> Animal:
   """
   Crea una instancia del tipo de animal especificado.

   :param animalType: El tipo de animal a crear.
   :return: Una instancia del animal.
   """
   return animalType()

# Ejemplo de uso
dog = crear_animal(animalType = Dog)
print(dog.crear_sonido(), end = "\n", file = stdout)  # Salida: Woof

cat = crear_animal(animalType = Cat)
print(cat.crear_sonido(), end = "\n", file = stdout)  # Salida: Meow

# TypeVar es una herramienta del módulo typing en Python que permite crear tipos genéricos. Se utiliza para definir variables de tipo en funciones y clases genéricas, lo que permite escribir código más flexible y reutilizable sin sacrificar la comprobación de tipos en tiempo de desarrollo.
# Supongamos que quieres escribir una función que intercambia dos elementos en una lista, independientemente del tipo de elementos que contenga la lista. Usar TypeVar te permitirá crear una función genérica que puede trabajar con cualquier tipo de lista.

T = TypeVar('T')

def intercambiar_elementos(*, lst: List[T], index1: int, index2: int) -> Union[List[T], NoReturn]:
   """
   Intercambia los elementos en las posiciones index1 e index2 de la lista lst.

   :param lst: Lista de elementos de tipo T.
   :param index1: Índice del primer elemento a intercambiar.
   :param index2: Índice del segundo elemento a intercambiar.
   :return: Lista con los elementos intercambiados.
   """
   if index1 < 0 or index1 >= len(lst) or index2 < 0 or index2 >= len(lst):
      raise IndexError("Índice fuera de rango")
   lst[index1], lst[index2] = lst[index2], lst[index1]
   return lst

# Ejemplo de uso
print(intercambiar_elementos(lst = [1, 2, 3], index1 = 0, index2 = 2), end = "\n", file = stdout)  # Salida: [3, 2, 1]
print(intercambiar_elementos(lst = ["a", "b", "c"], index1 = 1, index2 = 2), end = "\n", file = stdout)  # Salida: ["a", "c", "b"]
