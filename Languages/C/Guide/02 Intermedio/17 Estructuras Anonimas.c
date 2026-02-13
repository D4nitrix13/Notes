// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de una estructura anónima
struct {
    int a;           // Un entero
    float b;        // Un número en punto flotante
    double c;       // Un número en punto flotante de doble precisión
    char d;         // Un carácter
    int *x[10];     // Un arreglo de punteros a enteros
} anonima, anonima2, anonima3; // Declaración de tres instancias de la estructura anónima

int main(void) {
    // Asignación de valores a los miembros de la estructura anonima
    anonima.a = 10;
    anonima.b = 18.12;
    anonima.c = 20.45;
    anonima.d = 'a';

    // Asignación de punteros a enteros en el arreglo x
    for (int i = 0; i < 10; i++) {
        anonima.x[i] = &i; // Guardar la dirección de la variable i
    }

    return 0;
}
