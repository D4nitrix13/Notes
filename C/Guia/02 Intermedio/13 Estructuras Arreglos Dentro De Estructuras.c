// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de la estructura Empleado
// Esta estructura almacena información sobre un empleado, incluyendo su ID, nombre y salarios.
struct Empleado {
    int id;                    // Identificación única del empleado
    char *nombre;             // Puntero a una cadena de caracteres que representa el nombre
    float salarios[12];       // Arreglo para almacenar los salarios mensuales (12 meses)
};

int main(void) {
    // Declaración e inicialización de una estructura Empleado
    // Se inicializa con un ID, nombre y un arreglo de salarios para cada mes del año.
    struct Empleado empleado1 = {
        1, 
        "Daniel", 
        {2000.50, 2100.75, 2200.25, 2300.00, 2400.50, 2500.75, 
         2600.25, 2700.00, 2800.50, 2900.75, 3000.25, 3100.00}
    };

    // Acceso a los miembros de la estructura
    printf("ID: %d\n", empleado1.id);         // Imprime el ID del empleado
    printf("Nombre: %s\n", empleado1.nombre);  // Imprime el nombre del empleado

    // Impresión de los salarios de cada mes
    printf("Salarios mensuales:\n");
    for (int i = 0; i < 12; i++) {  // Itera sobre los 12 meses
        printf("Mes %d: %.2f\n", i+1, empleado1.salarios[i]); // Imprime el salario de cada mes
    }

    return 0; // Finaliza el programa
}

