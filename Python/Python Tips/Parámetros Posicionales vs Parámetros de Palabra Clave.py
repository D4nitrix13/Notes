#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from sys import exit

def funcion(*, n: str) -> None:
    print(f"El valor de n es: {n}", end = "\n", file = stdout )
    return None

funcion(n = "ejemplo")  # Correcto
# funcion('ejemplo')  # Incorrecto, esto causará un error
exit(0)

"""
<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***En Python, la sintaxis `def funcion(*, p: str)` define una función en la que el parámetro `p` es un parámetro de palabra clave. Esto significa que `p` debe ser especificado como un argumento de palabra clave cuando se llama a la función, no como un argumento posicional***

**Aquí está un desglose de cómo funciona:**

1. **Parámetros Posicionales vs. Parámetros de Palabra Clave:**
   - **Parámetros Posicionales:** *Son aquellos que se pasan a la función por posición. Por ejemplo, en `funcion(a, b)`, `a` y `b` son parámetros posicionales.*
   - **Parámetros de Palabra Clave:** *Son aquellos que se pasan a la función usando su nombre, como en `funcion(p = 'valor')`.*

2. **Uso del `*` en la Firma de la Función:**
   - *Cuando se coloca un `*` en la firma de una función, indica que todos los parámetros que siguen a este deben ser proporcionados como argumentos de palabra clave. En el caso de `def funcion(*, p: str)`, el parámetro `p` debe ser pasado usando su nombre, por ejemplo, `funcion(p = 'valor')`.*

3. **Ejemplo:**

   ```python
   #!/usr/bin/env python3

   # Autor: Daniel Benjamin Perez Morales
   # GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
   # Correo electrónico: danielperezdev@proton.me

   from sys import stdout
   from sys import exit

   def funcion(*, n: str) -> None:
       print(f"El valor de n es: {n}", end = "\n", file = stdout )
       return None

   funcion(n = "ejemplo")  # Correcto
   # funcion('ejemplo')  # Incorrecto, esto causará un error
   exit(0)
   ```

*En el ejemplo anterior, `funcion` requiere que el parámetro `p` sea especificado como una palabra clave. Si intentas pasar `p` como un argumento posicional, obtendrás un error.*

*Este enfoque puede ser útil para mejorar la legibilidad del código y asegurar que los argumentos se pasen de manera explícita, reduciendo la posibilidad de errores relacionados con el orden de los argumentos.*
"""