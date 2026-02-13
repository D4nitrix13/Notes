// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <string.h> // Librería necesaria para usar la función strcpy

// Definición de la estructura Persona
// Las estructuras permiten agrupar varios tipos de datos en una sola entidad. 
// En este caso, la estructura "Persona" tiene dos miembros: "nombre" (una cadena de caracteres) y "edad" (un entero).
struct Persona {
    char nombre[50]; // Arreglo de caracteres para almacenar el nombre (hasta 49 caracteres más el terminador nulo '\0')
    int edad;        // Entero para almacenar la edad
};

// Declaración de un nuevo tipo de datos usando typedef
// "typedef" se usa para darle un nuevo nombre (alias) a un tipo de datos existente.
// En este caso, "struct Persona" se renombra como simplemente "Persona" para simplificar la declaración.
typedef struct Persona Persona;

int main(void) {
    // Declaración de una variable de tipo Persona
    // Gracias al typedef, ya no es necesario escribir "struct Persona", solo usamos "Persona".
    Persona persona1;

    // Asignación de valores a los miembros de la estructura
    // La función strcpy copia la cadena "Daniel" al miembro "nombre" de la estructura.
    strcpy(persona1.nombre, "Daniel");
    
    // Asignamos el valor 30 al miembro "edad" de la estructura.
    persona1.edad = 30;

    // Acceso a los miembros de la estructura
    // Usamos el operador punto (.) para acceder y mostrar los valores almacenados en los miembros de la estructura.
    printf("Datos de la persona:\n");
    printf("Nombre: %s\n", persona1.nombre); // Imprime el nombre
    printf("Edad: %d\n", persona1.edad);     // Imprime la edad

    return 0;
}
