// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "04 While" "04 While.c" 
// ./"04 While"

/*
******************************
*     Tema: Bucles           *
*     Nivel: Basico          *
******************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // **Bucle While**
    // Variable que representa la condición del bucle.
    int condition = 0;

    // *Bucle While simple*
    // Ejecuta un bloque de código mientras se cumpla la condición `condition < 10`.
    while (condition < 10) {
        printf("%d\n", condition);  // Imprime el valor de `condition`.
        condition += 2;             // Incrementa `condition` en 2 en cada iteración.
    }

    // *Mensaje después del bucle*
    // Se ejecuta después de que la condición del bucle se vuelve falsa.
    printf("Mi condición es mayor o igual que 10\n");

    // *Bucle infinito con break*
    // Ejemplo de bucle infinito que se detiene explícitamente con `break`.
    while (1) {
        printf("Esto es un bucle infinito que se detiene con break\n");
        break;  // Termina el bucle infinito cuando se alcanza el `break`.
    }

    // *Bucle con break en una condición*
    // Ejecuta un bucle hasta que se cumpla una condición específica (`condition == 15`).
    condition = 0;
    while (condition < 20) {
        condition++;  // Incrementa `condition` en cada iteración.
        if (condition == 15) {
            printf("Se detiene la ejecución\n");
            break;  // Termina el bucle cuando `condition` es igual a 15.
        }
        printf("%d\n", condition);  // Imprime el valor de `condition`.
    }

    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de Bucles While :**

1. *Bucle While simple*:
   +---------------------------------+
   | while (condition < 10)          |
   | {                               |
   |     printf("%d\n", condition);  |
   |     condition += 2;             |
   | }                               |
   +---------------------------------+
   |
   V
   +---------------------------------+
   | 0                               |
   | 2                               |
   | 4                               |
   | 6                               |
   | 8                               |
   | Mi condición es mayor o igual que 10 |
   +---------------------------------+

2. *Bucle infinito con break*:
   +---------------------------------+
   | while (1)                       |
   | {                               |
   |     printf("Bucle infinito\n"); |
   |     break;                      |
   | }                               |
   +---------------------------------+
   |
   V
   +---------------------------------+
   | Esto es un bucle infinito que se detiene con break |
   +---------------------------------+

3. *Bucle con break en una condición*:
   +---------------------------------+
   | while (condition < 20)          |
   | {                               |
   |     condition++;                |
   |     if (condition == 15) {      |
   |         printf("Se detiene\n"); |
   |         break;                  |
   |     }                           |
   |     printf("%d\n", condition);  |
   | }                               |
   +---------------------------------+
   |
   V
   +---------------------------------+
   | 1                               |
   | 2                               |
   | ...                             |
   | 14                              |
   | Se detiene                      |
   +---------------------------------+
*/
