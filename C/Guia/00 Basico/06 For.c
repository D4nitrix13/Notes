// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "06 For" "06 For.c" 
// Ejecucion: ./"06 For"

/*
******************************
*     Tema: Arrays           *
*     Nivel: Basico          *
******************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Arrays en C**
    // Declaración e inicialización de arrays unidimensionales y bidimensionales.
    int lista[] = {10, 20, 30, 40, 50};   // Array unidimensional de 5 elementos.
    int matriz[3][3] = {                 // Array bidimensional de 3x3 elementos.
        {1, 2, 3},                       // Primera fila de la matriz.
        {4, 5, 6},                       // Segunda fila de la matriz.
        {7, 8, 9}                        // Tercera fila de la matriz.
    };

    // *Impresión de elementos del array unidimensional*
    printf("Elementos del array unidimensional:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", lista[i]);    // Imprime cada elemento del array unidimensional.
    }
    printf("\n");

    // *Impresión de elementos del array bidimensional*
    printf("Elementos del array bidimensional:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz[i][j]);   // Imprime cada elemento del array bidimensional.
        }
        printf("\n");
    }

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de Arrays en C :**

1. *Array Unidimensional*:
   +-------------------------------------+
   | int lista[] = {10, 20, 30, 40, 50}; |
   | for (int i = 0; i < 5; i++) {       |
   |     printf("%d ", lista[i]);        |
   | }                                   |
   +-------------------------------------+
   |
   V
   +-------------------------------------+
   | Elementos del array unidimensional: |
   | 10 20 30 40 50                      |
   +-------------------------------------+

2. *Array Bidimensional*:
   +---------------------------------------+
   | int matriz[3][3] = {                  |
   |     {1, 2, 3},                        |
   |     {4, 5, 6},                        |
   |     {7, 8, 9}                         |
   | };                                    |
   | for (int i = 0; i < 3; i++) {         |
   |     for (int j = 0; j < 3; j++) {     |
   |         printf("%d ", matriz[i][j]);  |
   |     }                                 |
   |     printf("\n");                     |
   | }                                     |
   +---------------------------------------+
   |
   V
   +------------------------------------+
   | Elementos del array bidimensional: |
   | 1 2 3                              |
   | 4 5 6                              |
   | 7 8 9                              |
   +------------------------------------+
*/