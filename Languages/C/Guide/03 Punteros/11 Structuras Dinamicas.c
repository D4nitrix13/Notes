// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>  // Incluir la biblioteca estándar de entrada/salida para usar printf
#include <stdlib.h> // Incluir la biblioteca estándar para funciones de gestión de memoria como malloc y free
#include <string.h> // Incluir la biblioteca para funciones de manipulación de cadenas como strlen y strcpy

// Definición de la estructura Persona
struct Persona {
    char *nombre; // Puntero a un carácter para almacenar el nombre (cadena de texto)
    int edad;     // Variable entera para almacenar la edad
};

// Declaración de la función crearPersona que devuelve un puntero a una estructura Persona
struct Persona *crearPersona(char *nombre, int edad);

// Definición de la función crearPersona
struct Persona *crearPersona(char *nombre, int edad) {
    // Asignar memoria para una nueva estructura Persona
    struct Persona *nuevaPersona = (struct Persona *)malloc(sizeof(struct Persona));
    
    // Comprobar si la asignación de memoria fue exitosa
    if (nuevaPersona == NULL) {
        // Imprimir un mensaje de error y salir si no se pudo asignar memoria
        printf("Error: No se pudo asignar memoria para la persona.\n");
        exit(1); // Terminar el programa con un código de error
    }

    // Asignar memoria para el nombre (cadena de caracteres) y copiar el nombre proporcionado
    nuevaPersona->nombre = (char *)malloc((strlen(nombre) + 1) * sizeof(char));
    
    // Comprobar si la asignación de memoria para el nombre fue exitosa
    if (nuevaPersona->nombre == NULL) {
        // Imprimir un mensaje de error y salir si no se pudo asignar memoria
        printf("Error: No se pudo asignar memoria para el nombre.\n");
        exit(1); // Terminar el programa con un código de error
    }
    
    // Copiar el nombre proporcionado a la memoria asignada
    strcpy(nuevaPersona->nombre, nombre);

    // Asignar la edad a la nueva persona
    nuevaPersona->edad = edad;

    // Devolver el puntero a la nueva persona creada
    return nuevaPersona;
}

int main(void) { // Función principal, punto de entrada del programa
    // Crear una nueva persona y asignar el puntero devuelto a persona1
    struct Persona *persona1 = crearPersona("Daniel", 30);

    // Imprimir los detalles de la persona
    printf("Persona 1:\n");
    printf("Nombre: %s\n", persona1->nombre); // Imprimir el nombre de la persona
    printf("Edad: %d\n", persona1->edad);     // Imprimir la edad de la persona

    // Liberar la memoria asignada para el nombre y la estructura Persona
    free(persona1->nombre); // Liberar la memoria del nombre
    free(persona1);         // Liberar la memoria de la estructura Persona

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
