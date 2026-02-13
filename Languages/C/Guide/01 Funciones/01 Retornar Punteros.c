// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "01 Retornar Punteros" "01 Retornar Punteros.c"
// Ejecucion: ./"01 Retornar Punteros"

#include <stdio.h>
#include <stdlib.h>

// Función para sumar dos números y devolver el resultado como un puntero
int *sumar(int x, int y) {
    int *resultado = (int*) malloc(1 * sizeof(int));
    // int *resultado: Declara una variable llamada 'resultado' que es un puntero a un entero.
    // malloc: Asigna dinámicamente memoria para almacenar un entero (int).
    // 1 * sizeof(int): Solicita exactamente 1 entero de memoria, el tamaño en bytes de un entero en el sistema.

    if (resultado == NULL) {
        perror("Error: No se pudo asignar memoria.\n");
        exit(1);
    }
    // Verificación de si la asignación de memoria fue exitosa

    *resultado = x + y;
    // *resultado: Almacena la suma de 'x' e 'y' en el espacio de memoria apuntado por 'resultado'.
    // Esto es conocido como desreferenciación, donde se accede al valor apuntado por un puntero.

    return resultado;
    // Devuelve el puntero 'resultado' que contiene la dirección de memoria donde se encuentra la suma.
}

int main(void) {
    int a = 5, b = 3;
    int *punteroResultado;

    // Llamada a la función sumar y almacenamiento del puntero al resultado
    punteroResultado = sumar(a, b);
    // punteroResultado: Variable que almacenará el puntero devuelto por la función 'sumar'.

    // Impresión del resultado
    printf("La suma de %d y %d es: %d\n", a, b, *punteroResultado);
    // *punteroResultado: Desreferencia el puntero para obtener el valor almacenado en la dirección de memoria apuntada.

    // Liberación de la memoria asignada
    free(punteroResultado);
    // free(punteroResultado): Libera la memoria asignada dinámicamente para evitar fugas de memoria.

    return 0;
    // Finalización exitosa del programa.
}

