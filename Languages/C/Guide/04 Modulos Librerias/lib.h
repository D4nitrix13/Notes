// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
// operaciones.h

#ifndef OPERACIONES_H
#define OPERACIONES_H true

// Prototipos de las funciones
/**
 * Suma dos enteros.
 *
 * Esta función toma dos enteros y devuelve su suma.
 *
 * @param a El primer entero.
 * @param b El segundo entero.
 * @return La suma de los dos enteros.
 */
int suma(int a, int b);
int resta(int a, int b);

int suma(int a, int b) {
    return a + b;
}

int resta(int a, int b) {
    return a - b;
}
#endif
