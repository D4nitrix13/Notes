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

# Lista de precios que son considerados caros
expensive: List[int] = [32, 20]

# Suma de los elementos en la lista 'expensive'
totalSum: int = sum(expensive)

# Imprime la suma total de los elementos en la lista
print(totalSum, end = "\n", file = stdout)  # Esto imprimirá: 52
```

---

## ***Explicación***

1. **Importación de Tipos:** *Se importa `List` del módulo `typing` para las anotaciones de tipo.*

2. **Lista de Precios Caros:** *`expensive` es una lista de enteros (`int`), donde cada entero representa un precio que se considera caro.*

3. **Uso de `sum`:**
   - *Se utiliza la función incorporada `sum` para calcular la suma de todos los elementos en la lista `expensive`.*
   - *El resultado de `sum(expensive)` es la suma de los elementos en la lista, que se almacena en la variable `totalSum`.*

4. **Impresión de la Suma Total:**
   - *Se imprime la suma total de los elementos en la lista `expensive`, que está almacenada en `totalSum`.*
   - *El resultado es `52`, que es la suma de `32` y `20`.*

---

### ***Comentarios Mejorados***

- **Lista de Precios Caros:** *`expensive` contiene los precios que son considerados caros.*
- **Cálculo de la Suma Total:** *`totalSum` es la suma de todos los elementos en la lista `expensive`, calculada utilizando la función `sum`.*
- **Impresión del Resultado:** *La impresión muestra la suma total de los elementos en la lista, que en este caso es `52`.*

- *Este código demuestra cómo se puede utilizar la función `sum` en Python para sumar los elementos de una lista de manera eficiente.*
