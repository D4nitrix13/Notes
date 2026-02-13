// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Definición de la estructura externa
struct Persona {
    char nombre[50]; // Almacena el nombre de la persona
    int edad;        // Almacena la edad de la persona

    // Definición de la estructura interna
    struct Talento {
        char habilidad[50]; // Almacena el nombre de una habilidad
        int nivel;          // Almacena el nivel de la habilidad
    } talento; // Instancia de la estructura interna como miembro de la estructura externa
};

int main(void) {
    // Declaración e inicialización de una estructura externa
    struct Persona persona = {"Daniel", 30, {"Programación", 5}};

    // Acceso a los miembros de la estructura externa
    printf("Nombre: %s\n", persona.nombre);
    printf("Edad: %d\n", persona.edad);

    // Acceso a los miembros de la estructura interna
    printf("Talento:\n");
    printf("Habilidad: %s\n", persona.talento.habilidad);
    printf("Nivel: %d\n", persona.talento.nivel);

    return 0;
}
