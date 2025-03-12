<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List, Callable

# Lista de precios en formato de cadena con el símbolo de dólar
dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

def map(iterable: List[str], func: Callable[[str], int]) -> List[int]:
    """
    Aplica una función a cada elemento de un iterable y devuelve una lista de resultados.

    :param iterable: Lista de cadenas a transformar.
    :param func: Función que transforma una cadena en un entero.
    :return: Lista de enteros transformados.
    """
    mapped: List[int] = list()
    for e in iterable:
        mapped.append(func(e))
    return mapped
    # * forma simplificada con list comprehension
    # return [func(e) for e in iterable]

def filter(iterable: List[int], func: Callable[[int], bool]) -> List[int]:
    """
    Filtra los elementos de un iterable aplicando una función de criterio.

    :param iterable: Lista de enteros a filtrar.
    :param func: Función que determina si un entero debe ser incluido.
    :return: Lista de enteros que cumplen con el criterio de la función.
    """
    filtered: List[int] = list()
    for e in iterable:
        # La misma lógica se puede expresar como:
        # if (func(e) == True): filtered.append(e)
        if func(e):
            filtered.append(e)
    return filtered
    # con list comprehension
    # return [int(e) for e in iterable if func(e)]

def reduce(iterable: List[int], func: Callable[[int, int], int], acum: int = 0) -> int:
    """
    Aplica una función de acumulación a los elementos de un iterable, reduciéndolos a un solo valor.

    :param iterable: Lista de enteros a reducir.
    :param func: Función de acumulación que combina dos enteros en uno.
    :param acum: Valor inicial de acumulación.
    :return: Entero resultante de la reducción.
    """
    for e in iterable:
        acum = func(acum, e)
    return acum

# Aplicar map para convertir los precios de cadena a enteros eliminando el símbolo de dólar
prices: List[int] = map(iterable=dollars, func=lambda dollar: int(dollar[0:-1:1]))

# Filtrar los precios que son mayores o iguales a 20
expensive: List[int] = filter(iterable=prices, func=lambda price: price >= 20)

# Reducir la lista de precios filtrados sumándolos
total: int = reduce(iterable=expensive, func=lambda acum, price: acum + price, acum=0)

# Imprimir el resultado final
print(total, end="\n", file = stdout)  # Esto imprimirá: 52
```

---

## ***Explicación del Código***

1. **Importación de Módulos y Tipos:**
   - *`List` y `Callable` se importan del módulo `typing` para las anotaciones de tipo, proporcionando una mejor claridad y verificación de tipos.*

2. **Lista `dollars`:**
   - *`dollars` es una lista de cadenas que representan precios en dólares.*

3. **Función `map`:**
   - *La función `map` toma un iterable y una función `func` que se aplica a cada elemento del iterable.*
   - *Utiliza un bucle `for` para aplicar `func` a cada elemento `e` del iterable, y agrega el resultado a la lista `mapped`.*
   - *La línea comentada con list comprehension muestra una forma más concisa de lograr lo mismo.*

4. **Función `filter`:**
   - *La función `filter` toma un iterable y una función `func` que determina si un elemento debe ser incluido en la lista resultante.*
   - *Utiliza un bucle `for` para evaluar cada elemento `e` del iterable con `func`. Si `func(e)` es `True`, el elemento se agrega a la lista `filtered`.*
   - *La línea comentada con list comprehension muestra una forma más concisa de lograr lo mismo.*

5. **Función `reduce`:**
   - *La función `reduce` toma un iterable, una función `func` de acumulación y un valor inicial de acumulación `acum`.*
   - *Utiliza un bucle `for` para aplicar `func` a `acum` y cada elemento `e` del iterable, actualizando `acum` en cada iteración.*
   - *Devuelve el valor final de `acum`.*

6. **Transformaciones y Cálculos:**
   - *`prices`: Aplica `map` para convertir las cadenas de precios a enteros, eliminando el símbolo de dólar.*
   - *`expensive`: Aplica `filter` para seleccionar solo los precios que son mayores o iguales a 20.*
   - *`total`: Aplica `reduce` para sumar los precios filtrados.*

7. **Resultado Final:**
   - *Imprime el valor total de los precios que son mayores o iguales a 20, que es `52`.*
