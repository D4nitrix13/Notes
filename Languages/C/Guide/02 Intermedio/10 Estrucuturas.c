// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>
#include <string.h> // Librería que contiene funciones para manejar cadenas de caracteres

// Definición de la estructura
// Las estructuras permiten agrupar diferentes tipos de datos bajo un solo nombre.
// En este caso, la estructura "Persona" agrupa un nombre, una edad y una altura.
struct Persona {
    char nombre[50]; // Cadena de caracteres para almacenar el nombre de la persona (hasta 49 caracteres + '\0')
    int edad;        // Entero que almacena la edad de la persona
    float altura;    // Flotante que almacena la altura de la persona en metros
};

int main(void) {
    // Declaración e inicialización de una estructura
    // Se declara una variable de tipo struct Persona llamada persona1
    struct Persona persona1;

    // Se copia el nombre "Daniel" en el miembro nombre de la estructura persona1
    // La función strcpy de la librería <string.h> se usa para copiar cadenas de caracteres
    strcpy(persona1.nombre, "Daniel");
    
    // Se asignan valores a los miembros de la estructura
    persona1.edad = 30;          // Asignamos la edad
    persona1.altura = 1.75;      // Asignamos la altura

    // Acceso a los miembros de la estructura
    // Para acceder a los miembros de una estructura, se usa el operador punto (.)
    printf("Datos de la persona:\n");
    printf("Nombre: %s\n", persona1.nombre);  // Imprime el nombre
    printf("Edad: %d\n", persona1.edad);      // Imprime la edad
    printf("Altura: %.2f\n", persona1.altura); // Imprime la altura con dos decimales

    // También puedes declarar una estructura e inicializarla al mismo tiempo
    // Aquí se declara e inicializa una estructura persona2 en una sola línea
    struct Persona persona2 = {"María", 25, 1.60};

    // Acceso a los miembros de la segunda estructura
    printf("\nDatos de otra persona:\n");
    printf("Nombre: %s\n", persona2.nombre);  // Imprime el nombre de persona2
    printf("Edad: %d\n", persona2.edad);      // Imprime la edad de persona2
    printf("Altura: %.2f\n", persona2.altura); // Imprime la altura de persona2 con dos decimales

    return 0;
}
