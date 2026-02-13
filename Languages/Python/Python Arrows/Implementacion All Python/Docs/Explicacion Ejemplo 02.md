<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

- *Este código muestra cómo implementar funciones genéricas `map`, `filter`, y `reduce` en Python utilizando tipos genéricos y funciones de orden superior (`Callable`, `TypeVar`). Aquí te explico cada parte:*

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List, Callable, TypeVar, Union, Any, Iterator

# Datos de ejemplo
dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

# Tipos genéricos
E = TypeVar("E")  # Tipo de elemento en la lista
R = TypeVar("R")  # Tipo de retorno de la función
A = TypeVar("A")  # Tipo acumulado para reduce

# Función map genérica
def map(iterable: List[E], func: Callable[[E], R]) -> Iterator[R]:
    mapped: List[R] = []
    for e in iterable:
        mapped.append(func(e))
    return iter(mapped)
    # * Implementación utilizando comprensión de listas
    # return (func(e) for e in iterable)


# Función filter genérica
def filter(iterable: Iterator[E], func: Callable[[E], bool]) -> Iterator[E]:
    filtered: List[E] = list()
    for e in iterable:
        if func(e):
            filtered.append(e)
    return iter(filtered)
    # * Implementación utilizando comprensión de listas
    # return (e for e in iterable if func(e))


# Función reduce genérica
def reduce(iterable: List[E], func: Callable[[A, E], A], acum: Union[A, Any] = 0) -> A:
    for e in iterable:
        acum = func(acum, e)
    return acum

# Aplicar map para convertir los precios de cadena a enteros eliminando el símbolo de dólar
prices: Iterator[int] = map(iterable=dollars, func=lambda dollar: int(dollar[0:-1:1]))

# Filtrar los precios que son mayores o iguales a 20
expensive: Iterator[int] = filter(iterable=prices, func=lambda price: price >= 20)

# Convertir expensive a una lista antes de imprimir
expensiveList: List[int] = list(expensive)
print(f"Precios caros: {expensiveList}", end="\n", file = stdout)  # Esto imprimirá: Precios caros: [32, 20]

# Reducir la lista de precios filtrados sumándolos
total: int = reduce(iterable=expensiveList, func=lambda acum, price: acum + price, acum=0)

# Imprimir el resultado final
print(f"Total: {total}", end="\n", file = stdout)  # Esto imprimirá: Total: 52
```

1. **Tipos Genéricos (`TypeVar`):**
   - *`E`, `R`, y `A` son tipos genéricos que representan elementos de una lista, el tipo de retorno de una función y el tipo acumulado para la función `reduce`, respectivamente.*

2. **Función `map` genérica:**
   - *`map` toma una lista de elementos de tipo `E` y una función que convierte cada elemento de `E` a `R`.*
   - *Utiliza un bucle `for` para aplicar la función `func` a cada elemento del `iterable`.*
   - *Crea una lista `mapped` de elementos de tipo `R` y luego la convierte en un iterador con `iter()`.*
   - *Devuelve el iterador de `mapped`, lo que permite una evaluación perezosa de los resultados.*

3. **Función `filter` genérica:**
   - *`filter` toma un iterador de elementos de tipo `E` y una función `func` que devuelve `True` o `False` para cada elemento.*
   - *Utiliza un bucle `for` para iterar sobre cada elemento del `iterable`.*
   - *Si `func(e)` es `True`, agrega el elemento `e` a la lista `filtered`.*
   - *Devuelve un iterador de `filtered`, también con evaluación perezosa.*

4. **Función `reduce` genérica:**
   - *`reduce` toma una lista de elementos de tipo `E`, una función binaria `func` que acumula un resultado de tipo `A`, y un valor inicial opcional `acum`.*
   - *Utiliza un bucle `for` para iterar sobre cada elemento del `iterable`.*
   - *Aplica la función `func` a `acum` y `e`, actualizando `acum` con el resultado.*
   - *Devuelve `acum`, que es el resultado final de la reducción.*

5. **Uso de las funciones genéricas:**
   - *Se define una lista `dollars` que contiene precios representados como cadenas.*
   - *`map` se utiliza para convertir estos precios en enteros eliminando el símbolo `$`.*
   - *`filter` se aplica sobre los precios convertidos para obtener aquellos que son mayores o iguales a 20.*
   - *Los precios filtrados se convierten en una lista y se imprimen.*
   - *`reduce` suma los precios filtrados para obtener el total, que se imprime como resultado final.*

- *Este enfoque muestra cómo utilizar funciones genéricas en Python para operaciones comunes como mapeo, filtrado y reducción, proporcionando flexibilidad y reutilización de código.*
