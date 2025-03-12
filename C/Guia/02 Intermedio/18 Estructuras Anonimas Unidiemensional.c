// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de una estructura anónima con arreglos
struct {
    int unidimensional[10]; // Arreglo unidimensional de enteros
    int bidimensional[5][10]; // Arreglo bidimensional de enteros
} anonima[3]; // Declaración de un arreglo de 3 estructuras anónimas

int main(void) {
    // Asignación de valores a los arreglos unidimensionales
    for (int i = 0; i < 10; i++) {
        anonima[0].unidimensional[i] = i;      // Asignar valores 0-9
        anonima[1].unidimensional[i] = i * 2;  // Asignar valores 0, 2, 4, ..., 18
        anonima[2].unidimensional[i] = i * 3;  // Asignar valores 0, 3, 6, ..., 27
    }

    // Asignación de valores a los arreglos bidimensionales
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 10; j++) {
            anonima[0].bidimensional[i][j] = i * j; // Producto de i y j
            anonima[1].bidimensional[i][j] = i + j; // Suma de i y j
            anonima[2].bidimensional[i][j] = i - j; // Resta de i y j
        }
    }

    // Imprimir los valores del arreglo unidimensional de la primera estructura anónima
    printf("Unidimensional (Estructura 1):\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", anonima[0].unidimensional[i]);
    }
    printf("\n");

    // Imprimir los valores del arreglo bidimensional de la segunda estructura anónima
    printf("Bidimensional (Estructura 2):\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", anonima[1].bidimensional[i][j]);
        }
        printf("\n");
    }

    // Imprimir los valores del arreglo bidimensional de la tercera estructura anónima
    printf("Bidimensional (Estructura 3):\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", anonima[2].bidimensional[i][j]);
        }
        printf("\n");
    }

    return 0;
}
