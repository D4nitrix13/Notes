// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "03 Punteros Funciones" "03 Punteros Funciones.c"
// Ejecucion: ./"03 Punteros Funciones"

#include <stdio.h>

// Función que suma dos enteros
int sumar(int a, int b);
int sumar(int a, int b)
{
    return a + b;
}

// Función que resta dos enteros
int restar(int a, int b);
int restar(int a, int b)
{
    return a - b;
}

int main(void)
{
    // Declaración de un puntero a función que toma dos enteros como argumentos y devuelve un entero
    int (*ptrFuncion)(int, int);

    // Asignar la dirección de la función 'sumar' al puntero a función
    ptrFuncion = &sumar;

    // Utilizar el puntero a función para llamar a la función 'sumar'
    int resultadoSuma = (*ptrFuncion)(5, 3);
    printf("Resultado de la suma: %d\n", resultadoSuma);

    // Asignar la dirección de la función 'restar' al puntero a función
    ptrFuncion = &restar;

    // Utilizar el puntero a función para llamar a la función 'restar'
    int resultadoResta = (*ptrFuncion)(5, 3);
    printf("Resultado de la resta: %d\n", resultadoResta);

    return 0;
}

/*
En C, `int (*ptrFuncion)(int, int);` es una declaración de un puntero a función. Vamos a desglosar cada parte para entender qué significa:

### `int (*ptrFuncion)(int, int);`

- `ptrFuncion`: Es el nombre del puntero a función que estamos declarando.
- `(*ptrFuncion)`: Indica que `ptrFuncion` es un puntero.
- `(int, int)`: Especifica los tipos de los parámetros que la función apuntada por `ptrFuncion` debe aceptar.
- `int`: Indica que la función apuntada por `ptrFuncion` debe devolver un entero.

Entonces, `int (*ptrFuncion)(int, int);` declara un puntero `ptrFuncion` que puede apuntar a una función que toma dos argumentos enteros y devuelve un entero.

### `ptrFuncion = &sumar;`

- `&sumar`: Obtiene la dirección de memoria de la función `sumar`. En C, obtener la dirección de una función devuelve un puntero a esa función del tipo correspondiente (en este caso, un puntero a una función que toma dos `int` y devuelve un `int`).
- `ptrFuncion = &sumar;`: Asigna esta dirección de memoria al puntero `ptrFuncion`, lo que hace que `ptrFuncion` apunte ahora a la función `sumar`.

### `int resultadoSuma = (*ptrFuncion)(5, 3);`

- `(*ptrFuncion)`: Aquí, `(*ptrFuncion)` desreferencia el puntero a función, es decir, llama a la función a la que `ptrFuncion` está apuntando.
- `(5, 3)`: Son los argumentos que se pasan a la función `sumar` (en este caso, `5` y `3`).
- `int resultadoSuma = (*ptrFuncion)(5, 3);`: Llama a la función a través del puntero `ptrFuncion`, ejecutando así la función `sumar` con los argumentos `5` y `3`, y el resultado se guarda en `resultadoSuma`.

### Explicación del Ejemplo Completo:

El programa completo utiliza un puntero a función `ptrFuncion` para poder llamar dinámicamente a las funciones `sumar` y `restar` según sea necesario:

1. **Declaración y Asignación del Puntero a Función:**
   - `int (*ptrFuncion)(int, int);`: Declara `ptrFuncion` como un puntero a función que toma dos enteros y devuelve un entero.
   - `ptrFuncion = &sumar;`: Asigna la dirección de `sumar` a `ptrFuncion`, lo que permite llamar a `sumar` a través de `ptrFuncion`.

2. **Uso del Puntero a Función:**
   - `(*ptrFuncion)(5, 3);`: Llama a la función apuntada por `ptrFuncion`, que puede ser `sumar` o `restar`, dependiendo de la asignación anterior.
   - `printf("Resultado de la suma: %d\n", resultadoSuma);`: Imprime el resultado de la operación, ya sea suma o resta, dependiendo de la función a la que `ptrFuncion` apunte.

Este enfoque permite que el programa sea más flexible al permitir cambiar dinámicamente qué función se llama en tiempo de ejecución utilizando un puntero a función.
*/