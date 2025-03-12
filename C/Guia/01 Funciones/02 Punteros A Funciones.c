// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Compilacion: gcc -o "02 Punteros A Funciones" "02 Punteros A Funciones.c"
// Ejecucion: ./"02 Punteros A Funciones"

// Definición de la función sumar_dos_numeros
int sumar_dos_numeros(int x, int y) {
    return x + y;
    // Devuelve la suma de los dos números recibidos como parámetros.
}

int main(void) {
    int (*punteroSuma)(int, int); // Declaración de un puntero a una función
    // int (*punteroSuma)(int, int): Declara 'punteroSuma' como un puntero a una función que toma dos enteros como argumentos y devuelve un entero.

    punteroSuma = &sumar_dos_numeros; // Asignación del puntero a la dirección de la función sumar_dos_numeros
    // punteroSuma = &sumar_dos_numeros: Asigna al puntero 'punteroSuma' la dirección de memoria de la función 'sumar_dos_numeros'.

    // Invocación de la función a través del puntero
    int resultado = (*punteroSuma)(3, 5);
    // (*punteroSuma)(3, 5): Invoca la función apuntada por 'punteroSuma', pasando los valores 3 y 5 como argumentos.

    printf("Resultado: %d\n", resultado); // Impresión del resultado obtenido
    // Imprime el resultado de la suma calculada por la función apuntada por 'punteroSuma'.

    return 0; // Finalización exitosa del programa
}
