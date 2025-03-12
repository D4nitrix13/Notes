// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int filas, columnas;

    // Solicitar al usuario el número de filas y columnas
    printf("Ingrese el número de filas: ");
    scanf("%d", &filas);
    printf("Ingrese el número de columnas: ");
    scanf("%d", &columnas);

    // Asignar memoria para el arreglo bidimensional
    int **arreglo = (int **)malloc(filas * sizeof(int *));
    if (arreglo == NULL) {
        printf("Error: No se pudo asignar memoria para las filas.\n");
        return 1;
    }

    for (int i = 0; i < filas; i++) {
        arreglo[i] = (int *)malloc(columnas * sizeof(int));
        if (arreglo[i] == NULL) {
            printf("Error: No se pudo asignar memoria para las columnas.\n");
            // Liberar la memoria previamente asignada para las filas
            for (int j = 0; j < i; j++) {
                free(arreglo[j]);
            }
            free(arreglo);
            return 1;
        }
    }

    // Inicializar el arreglo bidimensional con valores
    int contador = 1;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            arreglo[i][j] = contador++;
        }
    }

    // Imprimir los valores del arreglo bidimensional
    printf("Valores del arreglo bidimensional:\n");
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            printf("%d ", arreglo[i][j]);
        }
        printf("\n");
    }

    // Liberar la memoria asignada al arreglo bidimensional
    for (int i = 0; i < filas; i++) {
        free(arreglo[i]);
    }
    free(arreglo);

    return 0;
}
