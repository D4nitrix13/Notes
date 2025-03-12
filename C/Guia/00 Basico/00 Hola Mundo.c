// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "00 Hola Mundo" "00 Hola Mundo.c"
// Ejecucion: ./"00 Hola Mundo"

/*
***************************
*     Tema: Hola Mundo    *
*    Nivel: Básico        *
***************************
*/

// Instrucción del preprocesador: Incluye el fichero de cabecera estándar para entrada y salida (Standard Input Output).

#include <stdio.h>   // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// Comentario en una sola línea: Se usa para agregar notas o explicaciones breves en el código.
// Esto es un comentario en una sola línea.

/*
** Comentario en varias líneas **
* Se usa para comentarios más extensos que abarcan varias líneas. Es útil para documentar partes del código que requieren explicaciones detalladas. *
*/

// Función principal: Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    /*
    ** printf **
    * Función estándar para imprimir texto en la consola. Es parte de la biblioteca stdio.h.
    * Sintaxis:
    * printf("formato", argumentos);
    * \n es un carácter de escape que representa una nueva línea.
    */
    printf("Hola C");  // *Imprime el texto "Hola C" en la consola*.

    /*
    ** return 0 **
    * Termina la función `main` y devuelve 0 al sistema operativo, indicando que el programa finalizó correctamente.
    * Concepto: Indica que el programa terminó correctamente.
    * Características: `0` normalmente indica éxito; otros valores indican diferentes tipos de errores.
    */
    return 0;  // *Indica que el programa terminó correctamente*.
}
