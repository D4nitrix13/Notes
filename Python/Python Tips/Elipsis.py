#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
import numpy as np

a: np.ndarray = np.random.rand(5, 5, 5)
print(a[..., 0], end = "\n", file = stdout)  # Accede a todas las filas y columnas, pero solo a la primera "capa" en la tercera dimensión

from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):
    @abstractmethod
    def metodo_abstracto(self: "MiClaseAbstracta") -> None:
        ...

def mi_funcion() -> None:
    ...

"""
En Python, `...` (tres puntos) se conoce como el **literal de elipsis**. Tiene varios usos en diferentes contextos:

1. **Marcadores de Código Incompleto:**
   - `...` se usa a menudo como un marcador de posición para indicar que el código no está completo o que se ha omitido por razones de claridad. Es útil para resaltar áreas que necesitan ser implementadas más adelante.

   ```python
   def mi_funcion():
       ...
   ```

   En este ejemplo, `...` indica que la función `mi_funcion` aún no tiene una implementación.

2. **Slicing en Arrays y DataFrames:**
   - En bibliotecas como NumPy y Pandas, `...` se usa en el contexto del slicing para representar múltiples `:` (dos puntos) en arrays multidimensionales, simplificando la sintaxis para acceder a partes de arrays grandes.

   ```python
   from sys import stdout
   import numpy as np

   a: np.ndarray = np.random.rand(5, 5, 5)
   print(a[..., 0], end = "\n", file = stdout)  # Accede a todas las filas y columnas, pero solo a la primera "capa" en la tercera dimensión
   ```

3. **En Clases de Tipo Abstracto:**
   - `...` se utiliza en el contexto de clases abstractas para definir métodos que deben ser implementados por las subclases. Específicamente, se usa en la definición de métodos abstractos en lugar de `pass` para indicar que el método debe ser sobreescrito.

   ```python
   from abc import ABC, abstractmethod

   class MiClaseAbstracta(ABC):
        @abstractmethod
        def metodo_abstracto(self: "MiClaseAbstracta") -> None:
            ...
   ```

   Aquí, `...` indica que el método `metodo_abstracto` debe ser implementado por cualquier subclase que herede de `MiClaseAbstracta`.

4. **Desempaquetado de Argumentos en Funciones:**
   - Aunque menos común, `...` también puede ser usado en ciertos casos avanzados de desempaquetado de argumentos.

En resumen, `...` es una herramienta flexible en Python que puede usarse para indicar partes incompletas del código, simplificar la notación de slicing en arrays multidimensionales, o en contextos de definición de métodos abstractos y otros usos especializados.

En Python, el uso de `...` como valor de retorno de una función (es decir, en la anotación de tipo de retorno) no es estándar y no está permitido. La anotación de tipo de retorno debe ser un tipo de datos válido, como `int`, `str`, `None`, una lista de tipos, etc. El uso de `...` en el contexto de la anotación de tipo de retorno no es reconocido por el sistema de tipos de Python y provocará errores.

Aquí está un ejemplo de cómo usar correctamente las anotaciones de tipo en una función:

1. **Ejemplo Correcto con Anotaciones de Tipo:**

   ```python
   def mi_funcion() -> None:
       pass
   ```

   En este caso, la función `mi_funcion` está anotada para devolver `None`, y el cuerpo de la función está vacío. Esto es una forma válida de indicar que la función no devuelve ningún valor significativo.

2. **Ejemplo de Función con Tipo de Retorno Específico:**

   ```python
   def sumar(*, a: int, b: int) -> int:
       return a + b
   ```

   Aquí, la función `sumar` está anotada para devolver un `int`.

3. **Marcadores de Código Incompleto:**

   Si quieres usar `...` para marcar el código como incompleto (como un marcador de posición), debes hacerlo en el cuerpo de la función y no en la anotación de tipo:

   ```python
   def mi_funcion() -> None:
       ...
   ```

   En este caso, `...` en el cuerpo de la función indica que la implementación está pendiente, mientras que la anotación `-> None` indica que la función no devuelve ningún valor.

Si te encuentras con el error `Unexpected "..."`, probablemente se deba a que `...` se ha usado incorrectamente como tipo de retorno. Asegúrate de usar anotaciones de tipo válidas y coloca `...` solo en el cuerpo de la función si necesitas un marcador de posición.
"""

