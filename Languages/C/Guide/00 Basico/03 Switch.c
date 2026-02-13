// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "03 Switch" "03 Switch.c" 
// Ejecucion: ./"03 Switch"

/*
******************************
*     Tema: Switch Case      *
*     Nivel: Basico          *
******************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Condicional con match case para verificar condiciones dentro de case**
    // Variable que representa la edad.
    int age = 18;

    // *Switch Case para edad*
    // Evalúa la variable `age` y ejecuta el bloque de código correspondiente al valor de `age`.
    switch (age) {
        case 18:
            printf("Eres mayor de edad\n");
            break;
        case 17:
            printf("Eres menor de edad\n");
            break;
        case 5:
            printf("Eres un niño\n");
            break;
        default:
            break;
    }

    // **Condicional con _ como comodín en match case**
    // Variable que representa una letra.
    char letter = 'a';

    // *Switch Case para letra*
    // Utiliza `_` como comodín para cualquier valor no especificado en otros cases.
    switch (letter) {
        case 'a':
            printf("La letra es a\n");
            break;
        case 'b':
            printf("La letra es b\n");
            break;
        default:
            printf("La letra no es a ni b\n");
            break;
    }

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de Switch Case :**

1. *Switch Case para edad*:
   +---------------------------------+
   | switch (age)                    |
   | {                               |
   |     case 18:                    |
   |         // Código si age es 18  |
   |         break;                  |
   |     case 17:                    |
   |         // Código si age es 17  |
   |         break;                  |
   |     case 5:                     |
   |         // Código si age es 5   |
   |         break;                  |
   |     default:                    |
   |         break;                  |
   | }                               |
   +---------------------------------+
   |
   V
   +------------------------------------------------------+
   | Eres mayor de edad                                   |
   | // Otras posibles salidas basadas en el valor de age |
   +------------------------------------------------------+

2. *Switch Case para letra*:
   +------------------------------------------------------+
   | switch (letter)                                      |
   | {                                                    |
   |     case 'a':                                        |
   |         // Código si letter es 'a'                   |
   |         break;                                       |
   |     case 'b':                                        |
   |         // Código si letter es 'b'                   |
   |         break;                                       |
   |     default:                                         |
   |         // Código por defecto si no es ni 'a' ni 'b' |
   |         break;                                       |
   | }                                                    |
   +------------------------------------------------------+
   |
   V
   +---------------------------------------------------------+
   | La letra es a                                           |
   | // Otras posibles salidas basadas en el valor de letter |
   +---------------------------------------------------------+
*/
