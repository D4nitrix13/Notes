// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

void funcion(void);
void funcion(void) {
    // Variable static
    static int contador = 0;
    
    contador++;
    printf("El contador es: %d\n", contador);
    return;
}

int main(void) {
    funcion();
    funcion();
    funcion();
    
    return 0;
}
