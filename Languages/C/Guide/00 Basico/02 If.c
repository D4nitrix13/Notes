// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "02 If" "02 If.c" 
// Ejecucion: ./"02 If"

/*
*****************************
*     Tema: Condicionales   *
*     Nivel: Basico         *
*****************************
*/

// ***Instrucción del preprocesador*:** Incluye los ficheros de cabecera estándar para entrada y salida (stdio.h), booleanos (stdbool.h) y manejo de cadenas de texto (string.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.
#include <stdbool.h>    // stdbool.h define el tipo de dato booleano.
#include <string.h>     // string.h contiene funciones para manipulación de cadenas de texto.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Condicionales con if**
    // Definición de variables para las condicionales.
    bool condition = false;   // Variable booleana inicializada a falso.
    int number = 18;          // Variable entera inicializada a 18.
    char *string = "";        // Puntero a cadena de texto inicializado a cadena vacía.

    // *Condicional if simple*
    // Si la condición es verdadera, se ejecuta el bloque de código dentro del if.
    if (condition) {
        printf("La condición del if se cumple\n");
    }

    // *Condicional if-else if-else*
    // Evalúa múltiples condiciones y ejecuta el bloque de código correspondiente a la primera condición verdadera.
    if (number > 10 && number < 20) {
        printf("Es mayor que 10 y menor que 20\n");
    } else if (number == 25) {
        printf("Es igual a 25\n");
    } else {
        printf("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25\n");
    }

    // **Condicional con inspección de valor**
    // *Inspección de valor en cadenas de texto*
    // Verifica si la cadena de texto es vacía.
    if (!*string) {
        printf("Mi cadena de texto es vacía\n");
    }

    // *Comparación de cadenas de texto*
    // Compara la cadena de texto con otra cadena específica.
    if (strcmp(string, "Mi cadena de textoooooo") == 0) {
        printf("Estas cadenas de texto coinciden\n");
    }

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de los condicionales :**

1. *Condicional if*:
   +----------------------------+
   | if (condition)             |
   | {                          |
   |     // Código si verdadero |
   | }                          |
   +----------------------------+
   |
   V
   +-------------------------------+
   | La condición del if se cumple |
   +-------------------------------+

2. *Condicional if-else if-else*:
   +-------------------------------------------------------+
   | if (number > 10 && number < 20)                       |
   | {                                                     |
   |     // Código si number entre 10 y 20                 |
   | }                                                     |
   | else if (number == 25)                                |
   | {                                                     |
   |     // Código si number es 25                         |
   | }                                                     |
   | else                                                  |
   | {                                                     |
   |     // Código si ninguna condición anterior se cumple |
   | }                                                     |
   +-------------------------------------------------------+
   |
   V
   +---------------------------------------------------+
   | Es mayor que 10 y menor que 20                    |
   | // Otras posibles salidas basadas en la condición |
   +---------------------------------------------------+

3. *Condicional con inspección de valor*:
   +-------------------------------------+
   | if (!*string)                       |
   | {                                   |
   |     // Código si string está vacío  |
   | }                                   |
   +-------------------------------------+
   |
   V
   +-------------------------------------+
   | Mi cadena de texto es vacía         |
   +-------------------------------------+

4. *Comparación de cadenas de texto*:
   +-----------------------------------------------------+
   | if (strcmp(string, "Mi cadena de textoooooo") == 0) |
   | {                                                   |
   |     // Código si las cadenas coinciden              |
   | }                                                   |
   +-----------------------------------------------------+
   |
   V
   +------------------------------------------------+
   | Estas cadenas de texto coinciden               |
   +------------------------------------------------+
*/