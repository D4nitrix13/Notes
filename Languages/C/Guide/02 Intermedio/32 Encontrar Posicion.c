// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Declaración de la función para encontrar la posición de un valor en un array
int encontrarPosicion(int *array, int tam, int valor);

// Definición de la función para encontrar la posición de un valor en un array
int encontrarPosicion(int *array, int tam, int valor) {
    // Se itera a través de cada elemento del array
    for (int i = 0; i < tam; i++) {
        // Verificamos si el elemento actual es igual al valor buscado
        if (array[i] == valor) {
            return i; // Retorna la posición si se encuentra el valor
        }
    }
    return -1; // Retorna -1 si no se encuentra el valor
}

int main(void) {
    // Inicializamos un array de enteros
    int numeros[] = {10, 20, 30, 40, 50};
    int valorBuscar = 30; // Valor que se busca en el array

    // Encontrar la posición del valor en el array
    int posicion = encontrarPosicion(numeros, sizeof(numeros) / sizeof(numeros[0]), valorBuscar);

    // Verificar si se encontró el valor y mostrar la posición
    if (posicion != -1) {
        printf("El valor %d se encuentra en la posición %d del array.\n", valorBuscar, posicion);
    } else {
        printf("El valor %d no se encuentra en el array.\n", valorBuscar);
    }

    return 0; // Fin del programa
}
