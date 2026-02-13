// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "01 Random" "01 Random.c"
// Ejecucion: ./"01 Random"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Función para generar un número aleatorio en un rango específico [min, max]
int random_con_rango(int min, int max);
int random_con_rango(int min, int max)
{
    return min + rand() % (max - min + 1);
}

// Función para generar un número aleatorio sin un rango específico
int random_sin_rango(void);
int random_sin_rango(void)
{
    return rand();
}

int main(void)
{
    // Semilla para la función de generación de números aleatorios
    srand(time(NULL));

    // Generar y mostrar un número aleatorio en el rango [10, 20]
    printf("Número aleatorio en el rango [10, 20]: %d\n", random_con_rango(10, 20));

    // Generar y mostrar un número aleatorio sin un rango específico
    printf("Número aleatorio sin rango específico: %d\n", random_sin_rango());

    return 0;
}

/*
Claro, vamos a explicar las partes específicas del código que mencionaste.

### `srand(time(NULL));`

La función `srand` se utiliza para inicializar la semilla del generador de números aleatorios. La semilla es el punto de partida para la secuencia de números aleatorios generados por `rand`.

- `time(NULL)` devuelve el tiempo actual en segundos desde el 1 de enero de 1970 (la época Unix). Cada vez que ejecutas el programa, `time(NULL)` devuelve un valor diferente (siempre que al menos un segundo haya pasado desde la última ejecución).
- Al pasar el valor de `time(NULL)` a `srand`, garantizas que la secuencia de números aleatorios generada por `rand` será diferente cada vez que ejecutes el programa.

En resumen, `srand(time(NULL))` inicializa el generador de números aleatorios con el tiempo actual, asegurando que las secuencias de números aleatorios sean diferentes en cada ejecución del programa.

### `return min + rand() % (max - min + 1);`

Esta línea genera un número aleatorio en un rango específico `[min, max]`. Veamos cómo funciona:

1. `rand()` genera un número aleatorio entre `0` y `RAND_MAX`.
2. `rand() % (max - min + 1)` toma ese número aleatorio y lo mapea a un valor entre `0` y `(max - min)`. Esto se hace utilizando el operador módulo (`%`), que devuelve el resto de la división de `rand()` por `(max - min + 1)`.
3. `min + rand() % (max - min + 1)` desplaza el rango de `0 a (max - min)` a `min a max`.

### Ejemplo visual con ASCII art

Supongamos que queremos generar un número aleatorio en el rango `[10, 20]`.

1. `rand()` genera un número aleatorio. Supongamos que `rand()` devuelve `314159`.
2. Calculamos `rand() % (max - min + 1)`. Aquí `max` es `20` y `min` es `10`. Así que `(max - min + 1)` es `11`.

   ```plaintext
   314159 % 11 = 2
   ```

   Así que `rand() % (11)` devuelve `2`.

3. Ahora sumamos `min` al resultado:

   ```plaintext
   10 + 2 = 12
   ```

   Así que el número aleatorio generado en el rango `[10, 20]` es `12`.

### ASCII Art Explicación

Visualizando el proceso:

```plaintext
     +-----------------------+
     | 0        11        22 |  -> Posibles valores de rand() % 11
     | |         |         | |
     | |         |         | |
     | 0         10       20 |
     +-----------------------+
        \        \        \
         0        1        2      -> Ejemplo cuando rand() % 11 == 2
          \        \        \
           +10      +10      +10  -> Desplazamiento por min (10)
            \        \        \
             10       11       12  -> Resultado final: 12
```

En este ejemplo, el valor de `rand() % 11` puede ser cualquier número de `0` a `10`. Luego sumamos `10` a este valor, desplazándolo al rango `[10, 20]`.

En resumen, `return min + rand() % (max - min + 1);` genera un número aleatorio en el rango `[min, max]` al primero mapear `rand()` a un valor entre `0` y `(max - min)` y luego desplazarlo por `min`.
*/