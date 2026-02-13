// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de la estructura Empleado
// Esta estructura almacena información sobre un empleado, como su ID, nombre y salario.
struct Empleado {
    int id;                 // Identificación única del empleado
    char nombre[50];       // Arreglo de caracteres para almacenar el nombre del empleado
    float salario;         // Salario del empleado
};

int main(void) {
    // Declaración e inicialización de un arreglo bidimensional de empleados
    // Se crea un arreglo de estructuras Empleado con 2 filas y 5 columnas.
    // Cada fila representa un grupo de empleados.
    struct Empleado empleados[2][5] = {
        {
            {1, "Daniel", 2500.50},
            {2, "María", 2800.75},
            {3, "Pedro", 3000.25},
            {4, "Ana", 2700.00},
            {5, "Carlos", 3200.80}
        },
        {
            {6, "Laura", 2900.35},
            {7, "Pablo", 3100.60},
            {8, "Elena", 2600.45},
            {9, "Luis", 3300.70},
            {10, "Sofía", 3400.90}
        }
    };

    // Acceso a los empleados en el arreglo bidimensional mediante bucles anidados
    for (int i = 0; i < 2; i++) { // Itera sobre las filas del arreglo
        for (int j = 0; j < 5; j++) { // Itera sobre las columnas de cada fila
            printf("Empleado [%d][%d]\n", i, j); // Imprime la posición del empleado
            printf("ID: %d\n", empleados[i][j].id);                   // Imprime el ID del empleado
            printf("Nombre: %s\n", empleados[i][j].nombre);           // Imprime el nombre del empleado
            printf("Salario: %.2f\n", empleados[i][j].salario);       // Imprime el salario del empleado
            printf("\n"); // Imprime una línea en blanco para separación
        }
    }

    return 0; // Finaliza el programa
}
