// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "09 Goto" "09 Goto.c"
// Ejecucion: ./"09 Goto"

/*
*********************************
*     Tema: Uso de Goto en C     *
*     Nivel: Basico              *
*********************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // Declaración e inicialización de la variable de iteración
    int i = 1;

inicio: // Etiqueta de destino del goto

    // Imprime el número de iteración actual
    printf("Iteración %d\n", i);
    // Incrementa el contador de iteración
    i++;
    // Comprueba si se han completado todas las iteraciones
    if (i <= 5) {
        goto inicio; // Salta de nuevo al inicio del bucle usando `goto`
    }

    // Indica el fin del programa
    printf("Fin del programa\n");

    // Retorna 0 para indicar una ejecución exitosa del programa
    return 0;
}

/*
** Ilustración ASCII de Uso de Goto en C :**

1. *Uso de Goto en C*:
   +---------------------------------+
   | int i = 1;                      |
   |                                 |
   | inicio:                         |
   | printf("Iteración %d\n", i);    |
   | i++;                            |
   | if (i <= 5) {                   |
   |     goto inicio;                |
   | }                               |
   | printf("Fin del programa\n");   |
   | return 0;                       |
   +---------------------------------+
   |
   V
   +---------------------------------+
   | Iteración 1                     |
   | Iteración 2                     |
   | Iteración 3                     |
   | Iteración 4                     |
   | Iteración 5                     |
   | Fin del programa                |
   +---------------------------------+
*/
