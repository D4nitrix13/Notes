<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List

dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

# Implementacion de todos
print(sum(filter(lambda dollar: dollar >= 20, map(lambda dollar: int(dollar[0:-1:1]), dollars))),end="\n", file = stdout)
```

1. **Lista de Precios en Dólares:**
   - *`dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']`: Esta lista contiene los precios representados como cadenas de texto, donde cada precio tiene un símbolo de dólar al final.*

2. **Función `map`:**
   - *`map(lambda dollar: int(dollar[0:-1:1]), dollars)`: Utiliza `map` para convertir cada precio de cadena a entero eliminando el símbolo de dólar al final.*
     - *`lambda dollar: int(dollar[0:-1:1])`: Esta función lambda toma cada cadena `dollar` (por ejemplo, `'32$'`) y extrae los caracteres antes del último (`'32'`) convirtiéndolo a entero (`32`).*

3. **Función `filter`:**
   - *`filter(lambda dollar: dollar >= 20, ...)`: Utiliza `filter` para seleccionar solo aquellos precios convertidos que son mayores o iguales a 20.*
     - *`lambda dollar: dollar >= 20`: Esta función lambda evalúa si `dollar` es mayor o igual a 20.*

4. **Función `sum`:**
   - *`sum(...)`: Utiliza `sum` para sumar todos los precios filtrados que cumplen con la condición especificada por `filter`.*

5. **Impresión del Resultado:**
   - *`print(..., end="\n", file = stdout)`: Imprime el resultado final. El argumento `end="\n"` asegura que se imprima un salto de línea al finalizar la salida.*

**Explicación de la Expresión Completa:**

- `sum(filter(lambda dollar: dollar >= 20, map(lambda dollar: int(dollar[0:-1:1]), dollars)))`
  - *Primero, `map(lambda dollar: int(dollar[0:-1:1]), dollars)` convierte cada elemento de `dollars` a un entero quitando el último carácter (`'$'`).*
  - *Luego, `filter(lambda dollar: dollar >= 20, ...)` filtra estos números para seleccionar solo aquellos que son mayores o iguales a 20.*
  - *Finalmente, `sum(...)` suma todos los valores filtrados, proporcionando el resultado total deseado.*

- *Esta combinación de funciones es eficiente y utiliza técnicas funcionales para procesar datos de manera concisa y legible en Python.*
