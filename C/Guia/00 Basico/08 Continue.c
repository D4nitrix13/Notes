// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "08 Continue" "08 Continue.c"
// Ejecucion: ./"08 Continue"

/*
********************************
*     Tema: Bucles con Continue *
*     Nivel: Basico             *
********************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Bucles con Continue en C**
    int i;

    // *Ejemplo de bucle for con continue*
    printf("Ejemplo de bucle for con continue:\n");
    for (i = 1; i <= 10; i++) {
        // Salta la impresión cuando i es igual a 5 usando `continue`.
        if (i == 5) {
            continue;
        }
        printf("%d ", i);   // Imprime el valor de i en cada iteración, excepto cuando i es 5.
    }
    printf("\n");

    // *Ejemplo de bucle while con continue*
    printf("\nEjemplo de bucle while con continue:\n");
    i = 1;  // Reinicia la variable i para el bucle while.
    while (i <= 10) {
        // Salta la impresión cuando i es igual a 5 usando `continue`.
        if (i == 5) {
            i++;   // Incrementa i para evitar un bucle infinito.
            continue;
        }
        printf("%d ", i);   // Imprime el valor de i en cada iteración, excepto cuando i es 5.
        i++;   // Incrementa i en cada iteración.
    }
    printf("\n");

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de Bucles con Continue en C :**

1. *Ejemplo de bucle for con continue*:
   +---------------------------------+
   | for (i = 1; i <= 10; i++) {     |
   |     if (i == 5) {               |
   |         continue;               |
   |     }                           |
   |     printf("%d ", i);           |
   | }                               |
   +---------------------------------+
   |
   V
   +------------------------------------+
   | Ejemplo de bucle for con continue: |
   | 1 2 3 4 6 7 8 9 10                 |
   +------------------------------------+

2. *Ejemplo de bucle while con continue*:
   +---------------------------------+
   | while (i <= 10) {               |
   |     if (i == 5) {               |
   |         i++;                    |
   |         continue;               |
   |     }                           |
   |     printf("%d ", i);           |
   |     i++;                        |
   | }                               |
   +---------------------------------+
   |
   V
   +--------------------------------------+
   | Ejemplo de bucle while con continue: |
   | 1 2 3 4 6 7 8 9 10                   |
   +--------------------------------------+
*/
