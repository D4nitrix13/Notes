// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>  // Incluir la biblioteca estándar de entrada/salida para usar printf y scanf
#include <stdlib.h> // Incluir la biblioteca estándar para funciones de gestión de memoria como malloc y free

// Declaración de la función crearArreglo que toma un entero como parámetro y devuelve un puntero a entero
int *crearArreglo(int tamano);

// Definición de la función crearArreglo
int *crearArreglo(int tamano) {
    // Asignar memoria para un arreglo de tamaño 'tamano'
    // malloc devuelve un puntero a la memoria asignada
    int *arreglo = (int *)malloc(tamano * sizeof(int));
    
    // Comprobar si la asignación de memoria fue exitosa
    if (arreglo == NULL) {
        // Imprimir un mensaje de error si no se pudo asignar memoria
        printf("Error: No se pudo asignar memoria para el arreglo.\n");
        exit(1); // Salir del programa si no se pudo asignar memoria
    }

    // Inicializar el arreglo con valores consecutivos, comenzando desde 1
    for (int i = 0; i < tamano; i++) {
        arreglo[i] = i + 1; // Asignar a cada posición del arreglo su índice + 1
    }

    // Devolver el puntero al arreglo recién creado
    return arreglo;
}

int main(void) { // Función principal, punto de entrada del programa
    int tamano = 5; // Definir el tamaño del arreglo como 5
    int *miArreglo; // Declarar un puntero para almacenar la dirección del arreglo

    // Llamar a la función crearArreglo y asignar el puntero devuelto a miArreglo
    miArreglo = crearArreglo(tamano);

    // Imprimir los valores del arreglo
    printf("Arreglo devuelto por la función:\n");
    for (int i = 0; i < tamano; i++) {
        printf("%d ", miArreglo[i]); // Imprimir cada elemento del arreglo
    }
    printf("\n"); // Imprimir un salto de línea al final

    // Liberar la memoria asignada para el arreglo
    free(miArreglo); // Devolver la memoria asignada para evitar fugas de memoria

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
