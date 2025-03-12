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
from typing import Iterable, List

# Lista de precios en formato string con el símbolo '$'
dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

# Utilizando map con una función lambda para convertir los precios a enteros
# Esta línea devuelve un generador de tipo <map object at 0x...>
priceGenerator: Iterable[int] = map(lambda dollar: int(dollar[0:-1:1]), dollars)
print(priceGenerator, end="\n", file = stdout)  # Esto imprimirá: <map object at 0x...>

# Convertir el generador a una lista para obtener los precios como enteros
prices: List[int] = list(priceGenerator)
print(prices, end="\n", file = stdout)  # Esto imprimirá: [32, 15, 12, 17, 20]
```

---

## ***Explicación***

1. **Importación de Tipos:** *Se importa `List` del módulo `typing` para las anotaciones de tipo.*

2. **Lista de Precios en Dólares:** *`dollars` es una lista de cadenas de texto (`str`), donde cada cadena representa un precio con el símbolo '$'.*

3. **Uso de `map`:**
   - *Se utiliza `map` junto con una función lambda para transformar cada elemento de la lista `dollars`.*
   - *La función lambda `lambda dollar: int(dollar[0:-1:1])` toma cada cadena `dollar`, elimina el último carácter (`$`), y convierte el resultado a un entero (`int`).*
   - *El resultado de `map` es un generador, que se almacena en la variable `priceGenerator`.*

4. **Impresión del Generador:** *La impresión de `priceGenerator` muestra el tipo `<map object at 0x...>`, indicando que es un generador.*

5. **Conversión a Lista:**
   - *Para obtener los precios como una lista de enteros, se convierte el generador `priceGenerator` a una lista utilizando `list()`.*
   - *El resultado se almacena en la variable `prices`, que es una lista de enteros (`List[int]`).*

6. **Impresión de la Lista de Precios:** *Finalmente, se imprime la lista `prices`, mostrando los precios como enteros.*

---

### ***Comentarios Mejorados***

- **Lista de Precios en Dólares:** *`dollars` es la lista original de precios en formato de cadena con el símbolo '$'.*
- **Generador de Precios:** *`priceGenerator` es el generador resultante de aplicar `map` a `dollars`, utilizando una función lambda para convertir cada cadena a un entero.*
- **Conversión a Lista:** *La conversión del generador a una lista nos da `prices`, que contiene los precios en formato entero.*

- *Este código muestra cómo se puede utilizar `map` en Python para transformar elementos de una lista de manera eficiente.*
