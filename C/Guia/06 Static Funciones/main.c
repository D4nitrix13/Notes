// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
// main.c

#include <stdio.h>

// Declaración de la función static
static void funcionStatic(void);
static void funcionStatic(void) {
    printf("Esta es una función static.\n");
}

// Función principal
int main(void) {
    // Llamada a la función static
    funcionStatic();
    return 0;
}
