// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "05 Do While" "05 Do While.c" 
// Ejecucion: ./"05 Do While"

/*
******************************
*     Tema: Bucle Do-While   *
*     Nivel: Basico          *
******************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Bucle Do-While**
    // Variable que almacenará el número ingresado por el usuario.
    int numero;

    // *Bucle Do-While para ingresar números*
    // Solicita al usuario que ingrese un número y lo imprime hasta que se ingrese un número negativo.
    do {
        // Solicitar al usuario que ingrese un número
        printf("Por favor, ingrese un número (ingrese un número negativo para salir): ");
        scanf("%d", &numero);   // Lee el número ingresado por el usuario.

        // Imprimir el número ingresado
        printf("Número ingresado: %d\n", numero);

    } while (numero >= 0);  // Continuar el bucle mientras el número ingresado sea no negativo.

    // Mensaje al finalizar el bucle
    printf("Fin del programa.\n");

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de Bucle Do-While :**

1. *Bucle Do-While para ingresar números*:
   +---------------------------------+
   | do                              |
   | {                               |
   |     printf("Ingrese un número: "); |
   |     scanf("%d", &numero);       |
   |     printf("Número ingresado: %d\n", numero); |
   | } while (numero >= 0);          |
   +---------------------------------+
   |
   V
   +---------------------------------+
   | Por favor, ingrese un número: 5 |
   | Número ingresado: 5             |
   | Por favor, ingrese un número: -1 |
   | Número ingresado: -1            |
   | Fin del programa.               |
   +---------------------------------+
*/
