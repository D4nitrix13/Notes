// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <stdlib.h>

#define TAM_INICIAL 5
#define INCREMENTO 5

int main(void) {
    int *lista;
    int capacidad = TAM_INICIAL; // Tamaño inicial de la lista
    int longitud = 0; // Número actual de elementos en la lista
    int valor;
    char continuar;

    // Asignar memoria para la lista inicialmente
    lista = (int *)malloc(capacidad * sizeof(int));
    if (lista == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        return 1;
    }

    // Leer valores y agregarlos a la lista
    do {
        printf("Ingrese un valor: ");
        scanf("%d", &valor);

        // Si la lista está llena, redimensionarla
        if (longitud == capacidad) {
            capacidad += INCREMENTO;
            lista = (int *)realloc(lista, capacidad * sizeof(int));
            if (lista == NULL) {
                printf("Error: No se pudo redimensionar la lista.\n");
                return 1;
            }
        }

        // Agregar el valor a la lista
        lista[longitud] = valor;
        longitud++;

        printf("¿Desea ingresar otro valor? (s/n): ");
        scanf(" %c", &continuar);
    } while (continuar == 's' || continuar == 'S');

    // Imprimir la lista
    printf("Lista de valores ingresados:\n");
    for (int i = 0; i < longitud; i++) {
        printf("%d ", lista[i]);
    }
    printf("\n");

    // Liberar la memoria asignada para la lista
    free(lista);

    return 0;
}
