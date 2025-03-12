// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "03 Qsort" "03 Qsort.c"
// Ejecucion: ./"03 Qsort"

#include <stdio.h>
#include <stdlib.h>

// Función de comparación para qsort
int comparar_enteros(const void *a, const void *b);
int comparar_enteros(const void *a, const void *b)
{
    // Casting Convertir los parámetros void* a enteros
    int intA = *(int *)a;
    int intB = *(int *)b;
    /*
    - Imagina que `qsort` es como un organizador que toma dos objetos (`a` y `b`) y te pregunta cuál debería ir primero. Tu función de comparación (`comparar_enteros`) es la que decide basándose en los valores de `a` y `b`. Si `a` es menor que `b`, devuelve `-1` para indicar que `a` debe ir antes. Si `a` es mayor que `b`, devuelve `1` para indicar que `b` debe ir antes. Si son iguales, devuelve `0` para indicar que el orden no importa entre `a` y `b`.

    - Esto se repite para todos los pares de elementos en el arreglo hasta que esté completamente ordenado.
    */

    // Realizar la comparación
    if (intA < intB)
        return -1;
    if (intA > intB)
        return 1;
    return 0;
}

int main(void)
{
    // Arreglo de enteros desordenados
    int arreglo[] = {5, 2, 8, 3, 1};

    // Tamaño del arreglo
    int tamano = sizeof(arreglo) / sizeof(arreglo[0]);

    // Ordenar el arreglo utilizando qsort
    qsort(arreglo, tamano, sizeof(int), comparar_enteros);

    // Imprimir el arreglo ordenado
    printf("Arreglo ordenado:\n");
    for (int i = 0; i < tamano; i++)
    {
        printf("%d ", arreglo[i]);
    }
    printf("\n");

    return 0;
}

/*
La función `qsort` en C se utiliza para ordenar elementos de un arreglo en base a una función de comparación proporcionada por el usuario. Aquí tienes una explicación detallada junto con un ejemplo mejorado:

```c
#include <stdio.h>
#include <stdlib.h>

// Función de comparación para qsort
int comparar_enteros(const void *a, const void *b);

int main(void)
{
    // Arreglo de enteros desordenados
    int arreglo[] = {5, 2, 8, 3, 1};

    // Tamaño del arreglo
    int tamano = sizeof(arreglo) / sizeof(arreglo[0]);

    // Ordenar el arreglo utilizando qsort
    qsort(arreglo, tamano, sizeof(int), comparar_enteros);

    // Imprimir el arreglo ordenado
    printf("Arreglo ordenado:\n");
    for (int i = 0; i < tamano; i++)
    {
        printf("%d ", arreglo[i]);
    }
    printf("\n");

    return 0;
}

// Función de comparación para qsort
int comparar_enteros(const void *a, const void *b)
{
    // Casting: Convertir los parámetros void* a enteros
    int intA = *(int *)a;
    int intB = *(int *)b;

    // Realizar la comparación
    if (intA < intB)
        return -1;
    if (intA > intB)
        return 1;
    return 0;
}
```

### Explicación de `qsort` y su Uso:

1. **Declaración y Uso de `qsort`:**
   - `qsort(arreglo, tamano, sizeof(int), comparar_enteros);`
     - `arreglo`: Es el puntero al inicio del arreglo que se desea ordenar.
     - `tamano`: Es el número de elementos en el arreglo.
     - `sizeof(int)`: Es el tamaño en bytes de cada elemento del arreglo (en este caso, enteros).
     - `comparar_enteros`: Es la función de comparación que define el orden deseado.

2. **Función de Comparación `comparar_enteros`:**
   - `int comparar_enteros(const void *a, const void *b)`: Esta función toma dos punteros `void *` como parámetros, que luego son convertidos a punteros a enteros (`int *`).
   - `int intA = *(int *)a;` y `int intB = *(int *)b;`: Estas líneas convierten los punteros `void *` a enteros para realizar la comparación.
   - La función compara `intA` y `intB`:
     - Si `intA` es menor que `intB`, retorna `-1`.
     - Si `intA` es mayor que `intB`, retorna `1`.
     - Si son iguales, retorna `0`.
   - Estos valores de retorno determinan el ordenamiento ascendente del arreglo en función de cómo la función de comparación interpreta los elementos.

3. **Ordenamiento y Salida:**
   - Después de llamar a `qsort`, el arreglo `arreglo` queda ordenado de menor a mayor según la función de comparación `comparar_enteros`.
   - Se imprime el arreglo ordenado usando un bucle `for` simple.

### Explicar la Función de Comparación:

- Imagina que `qsort` es como un organizador que toma dos objetos (`a` y `b`) y te pregunta cuál debería ir primero. Tu función de comparación (`comparar_enteros`) es la que decide basándose en los valores de `a` y `b`. Si `a` es menor que `b`, devuelve `-1` para indicar que `a` debe ir antes. Si `a` es mayor que `b`, devuelve `1` para indicar que `b` debe ir antes. Si son iguales, devuelve `0` para indicar que el orden no importa entre `a` y `b`.

- Esto se repite para todos los pares de elementos en el arreglo hasta que esté completamente ordenado.

La función `qsort` es poderosa porque permite ordenar arreglos de manera eficiente utilizando diferentes criterios definidos por el usuario a través de una función de comparación.*/