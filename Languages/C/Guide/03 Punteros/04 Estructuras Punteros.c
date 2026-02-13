// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>    // Librería estándar para entrada y salida
#include <stdlib.h>   // Librería para la gestión de memoria dinámica (malloc, free)
#include <string.h>   // Librería para manipulación de cadenas (strdup)

// Definición de la estructura Persona
// La estructura "Persona" tiene dos miembros:
// - "nombre": un puntero a un carácter (cadena de caracteres)
// - "edad": una variable entera para almacenar la edad de la persona.
struct Persona {
    char *nombre;  // Puntero a char, para almacenar cadenas dinámicamente
    int edad;      // Variable para almacenar la edad
};

// Función para inicializar una persona
// Esta función toma un puntero a una estructura Persona y dos parámetros: nombre y edad.
// Asigna memoria para almacenar el nombre y copia el contenido de la cadena recibida.
void inicializar_persona(struct Persona *p, const char *nombre, int edad) {
    p->nombre = strdup(nombre); // strdup asigna memoria y copia la cadena de 'nombre'
    p->edad = edad;             // Asigna la edad a la estructura
    return;
}

// Función para liberar la memoria asignada a una persona
// Esta función libera la memoria previamente asignada al nombre de la persona,
// evitando fugas de memoria.
void liberar_persona(struct Persona *p) {
    free(p->nombre); // Libera la memoria dinámica asignada para el nombre
    return;
}

// Función para imprimir los datos de una persona
// Recibe un puntero constante a una Persona y muestra su nombre y edad.
void imprimir_persona(const struct Persona *p) {
    printf("Nombre: %s\n", p->nombre); // Imprime el nombre de la persona
    printf("Edad: %d\n", p->edad);     // Imprime la edad de la persona
    return;
}

int main(void) {
    // Declaración e inicialización de una persona utilizando la función inicializar_persona
    struct Persona persona1;
    inicializar_persona(&persona1, "Daniel", 30);  // Inicializa la estructura con nombre y edad

    // Llamada a la función para imprimir los datos de la persona
    printf("Datos de la persona 1:\n");
    imprimir_persona(&persona1);  // Imprime los datos de la persona

    // Liberar la memoria asignada a la persona
    liberar_persona(&persona1);   // Libera la memoria asignada para evitar fugas

    return 0;  // Fin del programa
}
