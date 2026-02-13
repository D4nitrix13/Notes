// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <stdbool.h> // Se incluye para usar el tipo bool

// Declaración de la función para verificar si un valor existe en un array
int valorExiste(int *array, int tam, int valor);

// Definición de la función para verificar si un valor existe en un array
int valorExiste(int *array, int tam, int valor) {
    // Se itera sobre cada elemento del array
    for (int i = 0; i < tam; i++) {
        // Verificamos si el elemento actual es igual al valor buscado
        if (array[i] == valor) {
            return true; // Retorna true si se encuentra el valor
        }
    }
    return false; // Retorna false si no se encuentra el valor
}

int main(void) {
    // Inicializamos un array de enteros
    int numeros[] = {10, 20, 30, 40, 50};
    int valorBuscar = 30; // Valor que se busca en el array

    // Verificamos si el valor existe en el array
    if (valorExiste(numeros, sizeof(numeros) / sizeof(numeros[0]), valorBuscar)) {
        printf("El valor %d existe en el array.\n", valorBuscar);
    } else {
        printf("El valor %d no existe en el array.\n", valorBuscar);
    }

    return 0; // Fin del programa
}
