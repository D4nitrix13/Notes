// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
// main.c

#include <stdio.h>

// Declaración de la variable externa
extern int variable_externa;

int main(void) {
    // Utilizamos la variable externa
    printf("El valor de la variable externa es: %d\n", variable_externa);
    variable_externa = 100;
    printf("EL nuevo valor de la variable externa es: %d\n", variable_externa);

    return 0;
}
