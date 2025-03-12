// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *puntero;

    // Asignación de memoria dinámica para un solo entero
    puntero = (int *)malloc(sizeof(int));
    //  puntero = (int *)calloc(5, sizeof(int)); // Comentado: Asignación de memoria para un arreglo de 5 enteros
    if (puntero == NULL) {
        printf("Error: No se pudo asignar memoria dinámica.\n");
        return 1;
    }

    // Asignación de un valor al entero
    *puntero = 42;
    printf("Puntero -> %p\n", puntero);
    printf("Valor asignado: %d\n", *puntero);

    // Liberación de la memoria dinámica
    free(puntero);

    return 0;
}
