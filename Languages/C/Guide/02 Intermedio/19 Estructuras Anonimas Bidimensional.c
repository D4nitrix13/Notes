// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de una estructura anónima con un arreglo
struct {
    int datos[10]; // Arreglo unidimensional de enteros
} anonima[3][10]; // Declaración de un arreglo bidimensional de 3x10 estructuras anónimas

int main(void) {
    // Asignación de valores a los arreglos dentro de la estructura anónima
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 10; j++) {
            anonima[i][j].datos[j] = i * j; // Asignar el producto de i y j
        }
    }

    // Imprimir los valores de los arreglos dentro de la estructura anónima
    for (int i = 0; i < 3; i++) {
        printf("Estructura %d:\n", i + 1);
        for (int j = 0; j < 10; j++) {
            printf("%d ", anonima[i][j].datos[j]); // Imprimir los valores del arreglo
        }
        printf("\n"); // Nueva línea al final de cada estructura
    }

    return 0;
}
