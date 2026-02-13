"""
Built-in Functions -> Funciones integradas en python
--------------------------------------------------------------|
A            | B             | C             | D              |
abs()        | bin()         | callable()    | delattr()      |
aiter()      | bool()        | chr()         | dict()         |
all()        | breakpoint()  | classmethod() | dir()          |
anext()      | bytearray()   | compile()     | divmod()       |
any()        | bytes()       | complex()     |                |
ascii()      |               |               |                |
--------------------------------------------------------------|
E            | F             | G             | H              |
enumerate()  | filter()      | getattr()     | hasattr()      |
eval()       | float()       | globals()     | hash()         |
exec()       | format()      |               | help()         |   
             | frozenset()   |               | hex()          |
--------------------------------------------------------------|
I            | L            | M             | N               |   
id()         | len()        | map()         | next()          |
input()      | list()       | max()         |                 |
int()        | locals()     | memoryview()  |                 |
isinstance() |              | min()         |                 |
issubclass() |              |               |                 |
iter()       |              |               |                 |
--------------------------------------------------------------|
O            | P             | R             | S              |
object()     | pow()         | range()       | set()          |
oct()        | print()       | repr()        | setattr()      |
open()       | property()    | reversed()    | slice()        |
ord()        |               | round()       | sorted()       |
             |               |               | staticmethod() |
             |               |               | str()          |
             |               |               | sum()          |
             |               |               | super()        |
--------------------------------------------------------------|
T            | U             | V             | Z              |
tuple()      | type()        | vars()        | zip()          |
type()       |               |               |                |
--------------------------------------------------------------|
_            |               |               |                |
__import__() |               |               |                |
--------------------------------------------------------------|
"""

from sys import stdout
from typing import List, NoReturn, Union, AsyncGenerator
from asyncio import run

def abs_funcion() -> None:
    # abs()
    """
    La función abs() en Python devuelve el valor absoluto de un número.
    El valor absoluto de un número es su distancia desde 0 en la línea de números reales,
    sin tener en cuenta la dirección. Por lo tanto, abs(-5) es 5 y abs(5) también es 5.
    """
    print(abs(-5), end="\n", file=stdout)  # Imprime: 5
    print(abs(5))  # Imprime: 5
    print(abs(0))  # Imprime: 0
    return None

def aiter_funcion() -> None:
    # aiter()
    """
    La función aiter() es una función incorporada en Python que se utiliza en el contexto de la programación asíncrona. Esta función se utiliza para obtener un objeto iterador asíncrono de un objeto iterable asíncrono.

    Un objeto iterable asíncrono es un objeto que define un método __aiter__() que devuelve un objeto iterador asíncrono. Un objeto iterador asíncrono es un objeto que define un método __anext__() que devuelve un objeto Future.

    En Python, aiter() es un método que puedes implementar en tus propias clases para hacer que sean iterables asíncronamente. Este método debe devolver un objeto que implemente el método __anext__(), el cual se utiliza para obtener los siguientes elementos de la iteración.
    """

    async def async_generator() -> AsyncGenerator[int, None]:
        for i in range(5):
            yield i

    async def print_values():
        async_iter: AsyncGenerator[int, None] = async_generator()
        async for value in async_iter:
            print(value)

    # Ejecutar la función asíncrona
    run(main=print_values())
    """
    En Python, `yield` es una palabra clave utilizada en funciones para definir generadores. Los generadores son una forma de crear iteradores de manera más sencilla y eficiente que usando clases y métodos iteradores tradicionales. La palabra clave `yield` se usa para producir una secuencia de valores en lugar de retornar un solo valor como en una función normal.

    ### ¿Qué hace `yield`?

    1. **Suspende la ejecución:** Cuando se usa `yield`, la ejecución de la función se suspende y el valor especificado se devuelve al llamador. La próxima vez que se reanude la ejecución, se continuará justo después del `yield`.

    2. **Retorna un valor:** `yield` produce un valor y permite que el bucle que está iterando sobre el generador continúe. 

    3. **Mantiene el estado:** La función generadora conserva su estado entre llamadas. Esto significa que puede continuar desde donde se quedó en la última llamada a `yield`.

    ### Ejemplo Básico

    Aquí tienes un ejemplo básico de cómo se usa `yield`:

    ```python
    def simple_generator():
        yield 1
        yield 2
        yield 3

    # Usando el generador
    gen = simple_generator()
    for value in gen:
        print(value)
    ```

    **Salida:**

    ```
    1
    2
    3
    ```

    En este ejemplo:

    - `simple_generator` es una función generadora que usa `yield` para devolver los valores 1, 2 y 3.
    - Cuando se itera sobre el generador `gen`, se obtiene cada valor uno a uno.

    ### Comparación con `return`

    - **`return`:** En una función normal, `return` devuelve un valor y termina la ejecución de la función. La próxima vez que se llame a la función, comenzará de nuevo desde el principio.
    - **`yield`:** En una función generadora, `yield` devuelve un valor y suspende la ejecución de la función. La próxima vez que se reanude la ejecución, continuará desde donde se detuvo.

    ### Generadores vs Iteradores

    - **Generador:** Es una función que usa `yield`. Retorna un iterador que se puede usar para iterar sobre los valores generados.
    - **Iterador:** Es un objeto que implementa los métodos `__iter__()` y `__next__()`. Los generadores son una forma conveniente de crear iteradores.

    ### Ejemplo Avanzado

    Aquí hay un ejemplo más avanzado que muestra cómo `yield` puede ser usado para generar una secuencia de números:

    ```python
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    # Usando el generador de Fibonacci
    for number in fibonacci(5):
        print(number)
    ```

    **Salida:**

    ```
    0
    1
    1
    2
    3
    ```

    En este ejemplo, `fibonacci` es una función generadora que produce los primeros `n` números de la secuencia de Fibonacci. La llamada a `yield` permite al generador producir un valor a la vez y conservar su estado entre iteraciones.
    """

    return None

def all_funcion() -> None:
    # all()

    """
    La función all() en Python toma un iterable (como una lista o un conjunto) y devuelve True si todos los elementos del iterable son verdaderos (o si el iterable está vacío)
    """
    # Todos los elementos son verdaderos
    print(all([True, True, True]), end="\n", file=stdout)  # Imprime: True

    # Uno de los elementos es falso
    print(all([True, False, True]), end="\n", file=stdout)  # Imprime: TrueFalse

    # El iterable está vacío
    print(all([]), end="\n", file=stdout)  # Imprime: True
    return None

def funcion_anext() -> None:
    """
    La función anext() es una función de la biblioteca estándar asyncio de Python.
    Se utiliza para obtener el próximo elemento de un iterador asíncrono.
    
    La función __anext__() es un método especial en Python que se utiliza para implementar iteradores asíncronos. Es parte del protocolo de iteradores asíncronos y se usa en combinación con __aiter__() para crear iteradores que se pueden recorrer de manera asíncrona con async for.
    """
    
    return None


def any_funcion() -> None:
    """
    La función any() en Python toma un iterable (como una lista o un conjunto) y devuelve True si al menos uno de los elementos del iterable es verdadero.
    Si el iterable está vacío, devuelve False.
    """
    # Al menos un elemento es verdadero
    print(any([False, False, True]))  # Imprime: True

    # Todos los elementos son falsos
    print(any([False, False, False]))  # Imprime: False

    # El iterable está vacío
    print(any([]))  # Imprime: False


def ascii_funcion() -> None:
    r"""La función ascii() en Python convierte un objeto en una cadena de caracteres ASCII. Los caracteres no ASCII se escapan con secuencias de escape \x, \u o \U."""
    noAsciiString: str = "Héllo, Wórld!"
    asciiString: str = ascii(noAsciiString)
    print(asciiString, end="\n", file=stdout)  # Imprime: 'H\\xe9llo, W\\xf3rld!'
    return None

def bin_funcion() -> None:
    """
    La función bin() en Python convierte un número entero en una cadena binaria.
    """
    number: int = 10
    binaryNumber: str = bin(number)
    print(binaryNumber, end="\n", file=stdout)  # Imprime: '0b1010'


def bool_funcion() -> None:
    """
    La función bool() en Python convierte un valor en un valor booleano (True o False).
    """
    # Cuando se usa en un valor no vacío o no cero, bool() devuelve True
    print(bool(10), end="\n", file=stdout)  # Imprime: True
    print(bool("Hello"), end="\n", file=stdout)  # Imprime: True

    # Cuando se usa en un valor vacío o cero, bool() devuelve False
    print(bool(0), end="\n", file=stdout)  # Imprime: False
    print(bool(0.0), end="\n", file=stdout)  # Imprime: False
    print(bool(""), end="\n", file=stdout)  # Imprime: False
    print(bool(False), end="\n", file=stdout)  # Imprime: False
    return None

def breakpoint_funcion() -> None:
    """
    La función breakpoint() en Python se utiliza para establecer un punto de interrupción en el código, que permite la depuración interactiva. Cuando se ejecuta el código y se alcanza el punto de interrupción, la ejecución se detiene y puedes examinar el estado del programa.
    """
    queso: int = 10
    pan: int = 20
    breakpoint()  # La ejecución se detendrá aquí si estás utilizando un depurador
    total: int = queso + pan
    print(total, end="\n", file=stdout)
    """
    pdb es el acrónimo de Python DeBugger. Es un módulo incorporado en Python que se utiliza para la depuración de código. Proporciona una interfaz interactiva para ejecutar código, evaluar expresiones, inspeccionar variables, controlar la ejecución del programa y mucho más.
    """
    return None


def bytearray_funcion() -> None:
    """
    La función bytearray() en Python crea y devuelve un objeto bytearray, que es una matriz de bytes."""
    # Crear un bytearray a partir de una lista list() o tuple() o un set() de enteros
    listaBytearray: bytearray = bytearray([65, 66, 67, 68])
    print(listaBytearray, end="\n", file=stdout)  # Imprime: bytearray(b'ABCD')

    # Crear un bytearray a partir de una cadena de caracteres
    listaBytearray = bytearray("Hello, World!", "utf-8")
    print(listaBytearray, end="\n", file=stdout)  # Imprime: bytearray(b'Hello, World!')
    print(type(listaBytearray), end="\n", file=stdout)  # Imprime: <class 'bytearray'>  

    # La b antes de la cadena en bytearray(b'ABCD') indica que la cadena es una cadena de bytes, no una cadena de texto normal.
    return None

def bytes_funcion() -> None:
    """
    La función bytes() en Python crea y devuelve un objeto de bytes, que es una secuencia inmutable de bytes.
    """
    # Crear un objeto de bytes a partir de una lista de enteros
    byte: bytes = bytes([65, 66, 67, 68])
    print(byte)  # Imprime: b'ABCD'

    # Crear un objeto de bytes a partir de una cadena de caracteres
    byte = bytes("Hello, World!", "utf-8") # tambien utf-16
    print(byte, end="\n", file=stdout)  # Imprime: b'Hello, World!'

    return None

if __name__ == "__main__":
    aiter_funcion()
