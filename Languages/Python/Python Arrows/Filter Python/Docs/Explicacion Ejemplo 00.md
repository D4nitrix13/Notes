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
from typing import List

# Lista de precios en formato entero
prices: List[int] = [32, 15, 12, 17, 20]

# Utilizando filter con una función lambda para seleccionar precios mayores o iguales a 20
# Esta línea devuelve un generador de tipo <filter object at 0x...>
priceFilter = filter(lambda price: price >= 20, prices)
print(priceFilter, end="\n", file = stdout)  # Esto imprimirá: <filter object at 0x...>

# Convertir el generador a una lista para obtener los precios filtrados
expensive: List[int] = list(priceFilter)
print(expensive, end="\n", file = stdout)  # Esto imprimirá: [32, 20]
```

---

## ***Explicación***

1. **Importación de Tipos:** *Se importa `List` del módulo `typing` para las anotaciones de tipo.*

2. **Lista de Precios:** *`prices` es una lista de enteros (`int`), donde cada entero representa un precio.*

3. **Uso de `filter`:**
   - *Se utiliza `filter` junto con una función lambda para seleccionar elementos de la lista `prices`.*
   - *La función lambda `lambda price: price >= 20` toma cada elemento `price` y devuelve `True` si el precio es mayor o igual a 20, y `False` en caso contrario.*
   - *El resultado de `filter` es un generador, que se almacena en la variable `priceFilter`.*

4. **Impresión del Generador:** *La impresión de `priceFilter` muestra el tipo `<filter object at 0x...>`, indicando que es un generador.*

5. **Conversión a Lista:**
   - *Para obtener los precios filtrados como una lista de enteros, se convierte el generador `priceFilter` a una lista utilizando `list()`.*
   - *El resultado se almacena en la variable `expensive`, que es una lista de enteros (`List[int]`).*

6. **Impresión de la Lista de Precios Filtrados:** *Finalmente, se imprime la lista `expensive`, mostrando los precios que son mayores o iguales a 20.*

### ***Comentarios Mejorados***

- **Lista de Precios:** *`prices` es la lista original de precios en formato entero.*
- **Generador de Precios Filtrados:** *`priceFilter` es el generador resultante de aplicar `filter` a `prices`, utilizando una función lambda para seleccionar los precios mayores o iguales a 20.*
- **Conversión a Lista:** *La conversión del generador a una lista nos da `expensive`, que contiene los precios filtrados en formato entero.*

- *Este código muestra cómo se puede utilizar `filter` en Python para seleccionar elementos de una lista de manera eficiente.*
