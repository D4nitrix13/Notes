// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *arreglo;
    int tamaño;

    // Solicitar al usuario el tamaño del arreglo
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &tamaño);

    // Asignar memoria dinámica para el arreglo
    arreglo = (int *)malloc(tamaño * sizeof(int));
    if (arreglo == NULL) {
        printf("Error: No se pudo asignar memoria dinámica.\n");
        return 1;
    }

    // Inicializar el arreglo con valores
    for (int i = 0; i < tamaño; i++) {
        arreglo[i] = i * 2; // Asignar valores al arreglo (en este caso, el doble del índice)
    }

    // Imprimir los valores del arreglo
    printf("Valores del arreglo:\n");
    for (int i = 0; i < tamaño; i++) {
        printf("%d ", arreglo[i]);
    }
    printf("\n");

    // Liberar la memoria asignada al arreglo
    free(arreglo);

    return 0;
}
