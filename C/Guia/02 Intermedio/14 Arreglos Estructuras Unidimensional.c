// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de la estructura Empleado
// Esta estructura almacena información básica sobre un empleado, como su ID, nombre y salario.
struct Empleado {
    int id;                 // Identificación única del empleado
    char nombre[50];       // Arreglo de caracteres para almacenar el nombre del empleado
    float salario;         // Salario del empleado
};

int main(void) {
    // Declaración e inicialización de una lista de empleados
    // Se crea un arreglo de estructuras Empleado con 3 empleados, cada uno con su ID, nombre y salario.
    struct Empleado empleados[3] = {
        {1, "Daniel", 2500.50},
        {2, "María", 2800.75},
        {3, "Pedro", 3000.25}
    };

    // Acceso a los empleados en la lista mediante un bucle
    for (int i = 0; i < 3; i++) { // Itera sobre los 3 empleados
        // Imprime la información de cada empleado
        printf("ID: %d\n", empleados[i].id);                  // Imprime el ID del empleado
        printf("Nombre: %s\n", empleados[i].nombre);          // Imprime el nombre del empleado
        printf("Salario: %.2f\n", empleados[i].salario);      // Imprime el salario del empleado
        printf("\n");                                          // Imprime una línea en blanco para separación
    }

    return 0; // Finaliza el programa
}
