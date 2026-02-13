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

## ***Explicación***

1. **Importación de Tipos:** *Se importa `List` del módulo `typing` para las anotaciones de tipo.*

2. **Lista de Precios Caros:** *`expensive` es una lista de enteros (`int`), donde cada entero representa un precio que se considera caro.*

3. **Uso de `sum`:**
   - *La función `sum` se utiliza para calcular la suma de todos los elementos en la lista `expensive`.*
   - *El argumento `start=0` especifica el valor inicial de la suma, que en este caso es `0`. Esto es útil para asegurar que la suma se inicie desde cero, aunque en este caso particular no es estrictamente necesario ya que `0` es el valor predeterminado de `start`.*

4. **Impresión de la Suma Total:**
   - *Se imprime la suma total de los elementos en la lista `expensive`, que está almacenada en `total_sum`.*
   - *El resultado es `52`, que es la suma de `32` y `20`.*

---

### ***Comentarios Mejorados***

- **Lista de Precios Caros:** *`expensive` contiene los precios que son considerados caros.*
- **Cálculo de la Suma Total:** *`total_sum` es la suma de todos los elementos en la lista `expensive`, calculada utilizando la función `sum` con un valor inicial de `0`.*
- **Impresión del Resultado:** *La impresión muestra la suma total de los elementos en la lista, que en este caso es `52`.*

- *Este código demuestra cómo se puede utilizar la función `sum` en Python para sumar los elementos de una lista de manera eficiente, incluyendo el uso del parámetro `start` para especificar un valor inicial para la suma.*
