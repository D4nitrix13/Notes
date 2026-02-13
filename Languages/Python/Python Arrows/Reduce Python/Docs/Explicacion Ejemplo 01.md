<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 01***

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List

# Lista de precios que son considerados caros
expensive: List[int] = [32, 20]

# Suma de los elementos en la lista 'expensive' con un valor inicial de 0
totalSum: int = sum(expensive, start=0)

# Imprime la suma total de los elementos en la lista
print(totalSum, end="\n", file = stdout)  # Esto imprimirá: 52
```

---

## ***Explicación***

1. **Importación de Módulos y Tipos:**
   - *`List` se importa del módulo `typing` para las anotaciones de tipo.*
   - *`reduce` se importa del módulo `functools` para realizar la reducción de la lista.*

2. **Lista de Precios Caros:**
   - *`expensive` es una lista de enteros (`int`), donde cada entero representa un precio que se considera caro.*

3. **Uso de `reduce` con Valor Inicial:**
   - *`reduce` aplica una función acumulativa a los elementos de la lista, desde el primer hasta el último elemento, para reducir la lista a un único valor.*
   - *La función lambda `lambda acum, price: acum + price` toma dos argumentos: `acum` (acumulador) y `price` (precio actual), y devuelve la suma de ambos. `acum` almacena el resultado acumulado de la suma, y `price` es el precio actual de la lista que se está procesando.*
   - *`reduce` recibe un tercer argumento opcional: el valor inicial del acumulador. En este caso, el valor inicial es `0`.*
   - *`reduce` aplica esta función a cada elemento de la lista `expensive`, acumulando la suma total en `totalSum` a partir del valor inicial `0`.*

4. **Impresión de la Suma Total:**
   - *`print(totalSum, end="\n", file = stdout)` imprime la suma total de los elementos en la lista `expensive`, que está almacenada en `totalSum`.*
   - *El resultado es `52`, que es la suma de `32` y `20`.*

---

### ***Comentarios Mejorados***

- **Lista de Precios Caros:** *`expensive` contiene los precios que son considerados caros.*
- **Cálculo de la Suma Total:** *`totalSum` es la suma de todos los elementos en la lista `expensive`, calculada utilizando la función `reduce` con una función lambda que suma los valores, y un valor inicial de `0`.*
- **Impresión del Resultado:** *La impresión muestra la suma total de los elementos en la lista, que en este caso es `52`.*

- *Este código muestra cómo se puede utilizar la función `reduce` en Python para sumar los elementos de una lista de manera eficiente, aplicando una operación acumulativa definida por una función lambda, y comenzando desde un valor inicial específico.*
