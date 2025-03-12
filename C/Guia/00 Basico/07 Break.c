// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "07 Break" "07 Break.c"
// Ejecucion: ./"07 Break"

/*
******************************
*     Tema: Bucles con Break  *
*     Nivel: Basico           *
******************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Bucles con Break en C**
    int i;

    // *Ejemplo de bucle for con break*
    printf("Ejemplo de bucle for con break:\n");
    for (i = 1; i <= 10; i++) {
        printf("%d ", i);   // Imprime el valor de i en cada iteración.
        if (i == 5) {
            // Cuando i llega a 5, salir del bucle usando `break`.
            break;
        }
    }
    printf("\n");

    // *Ejemplo de bucle while con break*
    printf("\nEjemplo de bucle while con break:\n");
    i = 1;  // Reinicia la variable i para el bucle while.
    while (i <= 10) {
        printf("%d ", i);   // Imprime el valor de i en cada iteración.
        if (i == 5) {
            // Cuando i llega a 5, salir del bucle usando `break`.
            break;
        }
        i++;  // Incrementa i en cada iteración.
    }
    printf("\n");

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de Bucles con Break en C :**

1. *Ejemplo de bucle for con break*:
   +---------------------------------+
   | for (i = 1; i <= 10; i++) {     |
   |     printf("%d ", i);           |
   |     if (i == 5) {               |
   |         break;                  |
   |     }                           |
   | }                               |
   +---------------------------------+
   |
   V
   +---------------------------------+
   | Ejemplo de bucle for con break: |
   | 1 2 3 4 5                      |
   +---------------------------------+

2. *Ejemplo de bucle while con break*:
   +---------------------------------+
   | while (i <= 10) {               |
   |     printf("%d ", i);           |
   |     if (i == 5) {               |
   |         break;                  |
   |     }                           |
   |     i++;                        |
   | }                               |
   +---------------------------------+
   |
   V
   +-----------------------------------+
   | Ejemplo de bucle while con break: |
   | 1 2 3 4 5                         |
   +-----------------------------------+
*/
