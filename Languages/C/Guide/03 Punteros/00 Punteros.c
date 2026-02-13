// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "00 Punteros" "00 Punteros.c" 
// Ejecucion: ./"00 Punteros"

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Declaración de variables
    int num = 10;
    int *ptrNum; // Declaración de un puntero a un entero

    // Asignación de la dirección de memoria de 'num' al puntero
    ptrNum = &num;

    // Imprimir el valor de 'num' y la dirección de memoria almacenada en el puntero
    printf("Valor de num: %d\n", num);
    printf("Dirección de memoria de num: %p\n", &num);
    printf("Valor almacenado en el puntero: %d\n", *ptrNum);
    printf("Dirección de memoria almacenada en el puntero: %p\n", (void *)ptrNum);

    // Modificar el valor de 'num' a través del puntero
    *ptrNum = 20;
    printf("Nuevo valor de num: %d\n", num);

    // Declaración e inicialización de un puntero nulo
    int *ptrNulo = NULL;

    // Arreglo de enteros y puntero a la primera posición del arreglo
    int arreglo[] = {1, 2, 3, 4, 5};
    int *ptrArreglo = arreglo;

    // Acceso a los elementos del arreglo a través del puntero
    printf("Elementos del arreglo accedidos a través del puntero:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("Elemento %d: %d\n", i + 1, *(ptrArreglo + i));
    }

    // Comprobación de si un puntero es nulo
    if (ptrNulo == NULL)
    {
        perror("El puntero es nulo.\n");
        free(ptrNulo);
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("El puntero no es nulo.\n");
    }

    return 0;
}

/*
### Código y Explicación

1. **Declaración de Variables y Punteros:**

    ```c
    int num = 10;
    int *ptrNum; // Declaración de un puntero a un entero

    // Asignación de la dirección de memoria de 'num' al puntero
    ptrNum = &num;
    ```

    - `int num = 10;`: Declara una variable entera `num` y le asigna el valor `10`.
    - `int *ptrNum;`: Declara un puntero a un entero, `ptrNum`.
    - `ptrNum = &num;`: Asigna la dirección de memoria de `num` al puntero `ptrNum` usando el operador `&`.

2. **Imprimir Valores y Direcciones de Memoria:**

    ```c
    printf("Valor de num: %d\n", num);
    printf("Dirección de memoria de num: %p\n", (void*)&num);
    printf("Valor almacenado en el puntero: %d\n", *ptrNum);
    printf("Dirección de memoria almacenada en el puntero: %p\n", (void*)ptrNum);
    ```

    - `printf("Valor de num: %d\n", num);`: Imprime el valor de `num`.
    - `printf("Dirección de memoria de num: %p\n", (void*)&num);`: Imprime la dirección de memoria de `num`.
    - `printf("Valor almacenado en el puntero: %d\n", *ptrNum);`: Imprime el valor apuntado por `ptrNum` (que es el valor de `num`).
    - `printf("Dirección de memoria almacenada en el puntero: %p\n", (void*)ptrNum);`: Imprime la dirección de memoria almacenada en `ptrNum`.

3. **Modificación del Valor Usando el Puntero:**

    ```c
    *ptrNum = 20;
    printf("Nuevo valor de num: %d\n", num);
    ```

    - `*ptrNum = 20;`: Cambia el valor de `num` a `20` usando el puntero `ptrNum`.
    - `printf("Nuevo valor de num: %d\n", num);`: Imprime el nuevo valor de `num`.

4. **Puntero Nulo y Comprobación:**

    ```c
    int *ptrNulo = NULL;

    if (ptrNulo == NULL)
    {
        perror("El puntero es nulo.\n");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("El puntero no es nulo.\n");
    }
    ```

    - `int *ptrNulo = NULL;`: Declara e inicializa un puntero nulo.
    - `if (ptrNulo == NULL)`: Comprueba si el puntero es nulo y, si lo es, imprime un mensaje de error y termina el programa.

5. **Arreglo y Puntero a la Primera Posición del Arreglo:**

    ```c
    int arreglo[] = {1, 2, 3, 4, 5};
    int *ptrArreglo = arreglo;
    ```

    - `int arreglo[] = {1, 2, 3, 4, 5};`: Declara un arreglo de enteros.
    - `int *ptrArreglo = arreglo;`: Declara un puntero a entero `ptrArreglo` y lo inicializa con la dirección del primer elemento del arreglo `arreglo`. No es necesario usar `&` aquí porque el nombre del arreglo `arreglo` ya es una referencia a su primera posición en memoria.

### Uso de `*(ptrArreglo + i)`

El código `*(ptrArreglo + i)` se usa para acceder a los elementos del arreglo usando aritmética de punteros.

- `ptrArreglo + i`: Calcula la dirección del i-ésimo elemento del arreglo.
- `*(ptrArreglo + i)`: Dereferencia la dirección calculada para obtener el valor del i-ésimo elemento.

### ASCII Art para Ilustrar `*(ptrArreglo + i)`

Supongamos que `ptrArreglo` apunta al primer elemento del arreglo `arreglo`.

```plaintext
arreglo:   [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ]
Dirección:  1000  1004  1008  1012  1016  (Suponiendo que cada int ocupa 4 bytes)
ptrArreglo: ^
           1000  (ptrArreglo apunta al primer elemento)

*(ptrArreglo + 0)  -> *(1000 + 0*4) -> *1000  -> 1
*(ptrArreglo + 1)  -> *(1000 + 1*4) -> *1004  -> 2
*(ptrArreglo + 2)  -> *(1000 + 2*4) -> *1008  -> 3
*(ptrArreglo + 3)  -> *(1000 + 3*4) -> *1012  -> 4
*(ptrArreglo + 4)  -> *(1000 + 4*4) -> *1016  -> 5
```

Aquí, `ptrArreglo` es la dirección del primer elemento del arreglo. La aritmética de punteros `ptrArreglo + i` calcula la dirección del i-ésimo elemento. La dereferencia `*(ptrArreglo + i)` nos da el valor almacenado en esa dirección.
*/