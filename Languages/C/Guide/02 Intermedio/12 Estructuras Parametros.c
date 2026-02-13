// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>   // Librería estándar para entrada y salida
#include <string.h>  // Librería para manipular cadenas de caracteres, como strcpy

// Definición de la estructura Persona
// Una estructura es un tipo de dato que agrupa varias variables de distintos tipos bajo un mismo nombre.
// En este caso, la estructura "Persona" tiene dos miembros: "nombre" y "edad".
struct Persona {
    char nombre[50];  // Arreglo de caracteres para almacenar el nombre (máximo 49 caracteres más el terminador nulo '\0')
    int edad;         // Variable entera para almacenar la edad de la persona
};

// Declaración de un nuevo tipo de datos usando typedef
// "typedef" permite crear un alias para un tipo de datos.
// Aquí, "typedef struct Persona Persona;" define un nuevo nombre "Persona" para el tipo "struct Persona",
// lo que simplifica la creación de variables de este tipo.
typedef struct Persona Persona;

int main(void) {
    // Declaración de una variable de tipo Persona
    // Gracias al uso de typedef, no es necesario escribir "struct Persona", sino solo "Persona".
    Persona persona1;

    // Asignación de valores a los miembros de la estructura
    // strcpy se usa para copiar la cadena "Daniel" en el miembro "nombre" de la estructura persona1.
    strcpy(persona1.nombre, "Daniel");
    // Se asigna el valor 30 al miembro "edad" de la estructura persona1.
    persona1.edad = 30;

    // Acceso a los miembros de la estructura
    // Se utiliza el operador punto (.) para acceder a los miembros de la estructura y mostrar sus valores.
    printf("Datos de la persona:\n");
    printf("Nombre: %s\n", persona1.nombre);  // Se imprime el nombre almacenado en la estructura
    printf("Edad: %d\n", persona1.edad);      // Se imprime la edad almacenada en la estructura

    return 0; // Finaliza el programa exitosamente
}
