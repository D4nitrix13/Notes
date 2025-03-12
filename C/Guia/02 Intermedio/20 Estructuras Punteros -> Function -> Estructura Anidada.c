// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <string.h>  // Necesario para usar strcpy

// Definición de la estructura Fecha
// Esta estructura almacena un día, mes y año como una representación de una fecha.
struct Fecha {
    int dia;
    int mes;
    int año;
};

// Definición de la estructura Persona
// La estructura Persona incluye una cadena de caracteres para el nombre,
// un entero para la edad y una estructura Fecha anidada para la fecha de nacimiento.
struct Persona {
    char nombre[50];              // Almacena el nombre de la persona
    int edad;                     // Almacena la edad de la persona
    struct Fecha fecha_nacimiento; // Anidación de la estructura Fecha dentro de Persona
};

// Función para imprimir los datos de una persona
// Recibe una estructura Persona por valor y muestra sus datos en la salida estándar.
void imprimir_persona(struct Persona p) {
    printf("Nombre: %s\n", p.nombre);  // Imprime el nombre
    printf("Edad: %d\n", p.edad);      // Imprime la edad
    // Imprime la fecha de nacimiento usando los miembros de la estructura Fecha
    printf("Fecha de nacimiento: %d/%d/%d\n", p.fecha_nacimiento.dia, p.fecha_nacimiento.mes, p.fecha_nacimiento.año);
    return;
}

// Función para modificar la edad de una persona mediante un puntero
// Se pasa un puntero a una estructura Persona, lo que permite modificar la edad directamente en la estructura original.
void modificar_edad(struct Persona *p, int nueva_edad) {
    p->edad = nueva_edad;  // Modifica el valor de la edad a través del puntero
    return;
}

int main(void) {
    // Declaración e inicialización de una variable de tipo Persona
    // Aquí inicializamos la estructura Persona con un nombre, edad y fecha de nacimiento.
    struct Persona persona = {"Daniel", 30, {15, 5, 1990}};
    
    // Declaración manual de otra persona
    struct Persona persona2;
    strcpy(persona2.nombre, "Daniel");    // Asigna un nombre usando strcpy para cadenas
    persona2.edad = 30;                   // Asigna la edad directamente
    persona2.fecha_nacimiento.dia = 15;   // Asigna el día de nacimiento
    persona2.fecha_nacimiento.mes = 5;    // Asigna el mes de nacimiento
    persona2.fecha_nacimiento.año = 1990; // Asigna el año de nacimiento

    // Llamada a la función para imprimir los datos de la persona
    printf("Datos originales de la persona:\n");
    imprimir_persona(persona);  // Imprime los datos de persona1

    // Llamada a la función para modificar la edad de la persona
    modificar_edad(&persona, 35);  // Modifica la edad de persona1 a 35

    // Imprimir los datos de la persona después de modificar la edad
    printf("\nDatos de la persona después de modificar la edad:\n");
    imprimir_persona(persona);  // Imprime los datos actualizados de persona1
    imprimir_persona(persona2); // Imprime los datos de persona2

    return 0;  // Finaliza el programa
}
