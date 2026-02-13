#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# optimising code in python

# version 3.9 python

from sys import stdout, exit  # Importa 'stdout' desde el módulo 'sys' para imprimir en la salida estándar.
from time import perf_counter  # Importa 'perf_counter' para medir tiempos de ejecución con alta precisión.

# Mide el tiempo de inicio del benchmark.
start_time: float = perf_counter()

# Mide el tiempo de finalización del benchmark.
end_time: float = perf_counter()

# Imprime el tiempo total transcurrido en segundos.
print("total:", end_time - start_time, end="\n", file=stdout)

def main() -> None:
    # Importa 'disable' para desactivar el recolector de basura y 'repeat' y 'timeit' para medir el tiempo de ejecución.
    from gc import disable
    from timeit import repeat, timeit
    
    # Desactiva el recolector de basura para evitar que interfiera con los resultados del benchmark.
    disable()
    
    # Define un código de ejemplo para la lista por comprensión.
    list_comp: str = """lista: List[int] = [i for i in range(0, 10, 1)]"""
    
    # Define un código de ejemplo para el bucle 'for' que agrega elementos a una lista.
    for_loop: str = """\
lista: List[int] = list()
for i in range(0, 10, 1):
    lista.append(i)
"""

    # Mide el tiempo de ejecución del código de lista por comprensión usando 'repeat'.
    # 'repeat' ejecuta el código varias veces (5 repeticiones) y devuelve una lista con el tiempo de ejecución de cada repetición.
    list_comp_time1: float = min(repeat(stmt=list_comp, repeat=5, number=1_000_000))
    
    # Mide el tiempo de ejecución del código del bucle 'for' usando 'repeat'.
    # 'repeat' ejecuta el código varias veces (5 repeticiones) y devuelve una lista con el tiempo de ejecución de cada repetición.
    for_comp_time1: float = min(repeat(stmt=for_loop, repeat=5, number=1_000_000))

    # Mide el tiempo de ejecución del código de lista por comprensión usando 'timeit'.
    # 'timeit' ejecuta el código una vez y mide el tiempo total para un número especificado de repeticiones.
    list_comp_time2: float = timeit(stmt=list_comp, number=1_000_000)
    
    # Mide el tiempo de ejecución del código del bucle 'for' usando 'timeit'.
    # 'timeit' ejecuta el código una vez y mide el tiempo total para un número especificado de repeticiones.
    for_comp_time2: float = timeit(stmt=for_loop, number=1_000_000)

    # Imprime el tiempo de ejecución de la lista por comprensión usando 'repeat'.
    print(f"List compilation 1: {list_comp_time1:.3f}s", end="\n", file=stdout)
    
    # Imprime el tiempo de ejecución del bucle 'for' usando 'repeat'.
    print(f"For Loop 1: {for_comp_time1:.3f}s", end="\n", file=stdout)

    # Imprime el tiempo de ejecución de la lista por comprensión usando 'timeit'.
    print(f"List compilation 2: {list_comp_time2:.3f}s", end="\n", file=stdout)
    
    # Imprime el tiempo de ejecución del bucle 'for' usando 'timeit'.
    print(f"For Loop 2: {for_comp_time2:.3f}s", end="\n", file=stdout)

    # La función no devuelve ningún valor.
    return None

# Verifica si el script se está ejecutando como el principal y, en ese caso, llama a la función 'main'.
if __name__ == "__main__":
    main()
    exit(0)

"""
# Explicación de Módulos y Funciones:

1. **`from sys import stdout`**
   - `stdout` es el flujo de salida estándar. Usamos esto para imprimir resultados en la consola de forma más explícita.

2. **`from time import perf_counter`**
   - `perf_counter` mide el tiempo de ejecución de manera precisa, incluyendo el tiempo de suspensión del sistema. Es ideal para medir tiempos de ejecución en benchmarks.

3. **`from gc import disable`**
   - `gc` es el módulo de recolección de basura. `disable()` se usa para desactivar temporalmente la recolección de basura para evitar que el recolector de basura interfiera con las mediciones de tiempo.

4. **`from timeit import repeat, timeit`**
   - `repeat()` ejecuta un bloque de código varias veces y devuelve una lista con los tiempos de ejecución de cada repetición. Esto es útil para obtener una idea del tiempo mínimo requerido para una tarea repetida.
   - `timeit()` ejecuta un bloque de código un número específico de veces y mide el tiempo total, lo que es útil para benchmarks sencillos y pruebas de rendimiento.

## Buenas Prácticas para Benchmarking:

1. **Desactivar el recolector de basura:** Para evitar que el recolector de basura afecte los tiempos de ejecución, es útil desactivarlo durante el benchmarking. Esto se hace con `gc.disable()`.

2. **Usar `repeat` y `timeit` para comparar resultados:** `repeat` proporciona tiempos detallados para varias repeticiones, lo que ayuda a obtener una estimación más precisa del tiempo mínimo requerido para una tarea. `timeit` ofrece una forma sencilla de medir el tiempo total de ejecución.

3. **Medir tiempos en un rango de repeticiones:** Usar un número alto de repeticiones (como 1,000,000 en tu caso) ayuda a obtener mediciones más estables y a reducir el impacto de variaciones en el tiempo de ejecución.

4. **Documentar el propósito de las mediciones:** Asegúrate de documentar claramente qué estás midiendo y por qué, para que otros puedan entender el propósito del benchmark.

Siguiendo estas prácticas, puedes realizar benchmarks más precisos y útiles para evaluar el rendimiento de diferentes enfoques en Python.
"""

"""
# Parámetros en `timeit` y `repeat`

1. **`stmt`:**
   - **Qué es:** `stmt` es un parámetro que representa el código que quieres medir. Es una cadena de texto que contiene el código que se va a ejecutar y cuyo tiempo de ejecución deseas medir.
   - **Uso:** Este parámetro se utiliza para especificar el bloque de código a ser ejecutado repetidamente. Por ejemplo, en tu caso, `stmt=list_comp` y `stmt=for_loop` son bloques de código que crean listas usando comprensión de listas y un bucle `for`, respectivamente.

2. **`repeat`:**
   - **Qué es:** `repeat` es un parámetro utilizado en la función `repeat` del módulo `timeit`. Indica cuántas veces se debe ejecutar el código especificado en `stmt` para obtener una lista de tiempos de ejecución.
   - **Uso:** `repeat` ejecuta el código `stmt` un número determinado de veces y devuelve una lista con los tiempos de ejecución de cada repetición. Esto te permite obtener una idea de cómo varía el tiempo de ejecución en diferentes ejecuciones. En tu código, `repeat=5` significa que el código se ejecutará 5 veces y se recogerán los tiempos de cada ejecución.

3. **`number`:**
   - **Qué es:** `number` es un parámetro que se usa en ambas funciones `timeit` y `repeat`. Indica cuántas veces debe ejecutarse el código `stmt` en cada repetición de la medición.
   - **Uso:** `number` especifica el número de veces que el código debe ser ejecutado en una sola llamada a la función. Por ejemplo, `number=1_000_000` significa que el código en `stmt` se ejecutará 1,000,000 veces en cada repetición. Esto ayuda a obtener una medición precisa del tiempo necesario para ejecutar el código un gran número de veces.

## Ejemplo Explicativo

### Resumen
- **`stmt`:** El código a medir (como una cadena de texto).
- **`repeat`:** Cuántas veces ejecutar el código para obtener una lista de tiempos.
- **`number`:** Cuántas veces ejecutar el código en cada repetición para medir el tiempo total.

Estos parámetros te permiten ajustar el nivel de precisión y detalle de tus benchmarks para evaluar el rendimiento de diferentes enfoques en Python.
"""