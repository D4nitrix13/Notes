// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>    // Incluir la biblioteca estándar de entrada/salida para usar printf
#include <stdarg.h>   // Incluir la biblioteca para manejar argumentos variádicos

// Función variádica para imprimir una lista de enteros
void imprimirEnteros(int numArgs, ...) {
    va_list args;              // Declara una variable para almacenar los argumentos
    va_start(args, numArgs);   // Inicializa la lista de argumentos variádicos

    // Iterar sobre los argumentos y imprimir cada entero
    for (int i = 0; i < numArgs; i++) {
        int valor = va_arg(args, int); // Obtiene el siguiente argumento como un entero
        printf("%d ", valor);           // Imprime el valor entero
    }

    va_end(args);            // Finaliza el uso de la lista de argumentos
    printf("\n");           // Imprime una nueva línea al final
    return;                 // Fin de la función
}

// Función variádica para imprimir una lista de números de punto flotante
void imprimirDoubles(int numArgs, ...);
void imprimirDoubles(int numArgs, ...) {
    va_list args;              // Declara una variable para almacenar los argumentos
    va_start(args, numArgs);   // Inicializa la lista de argumentos variádicos

    // Iterar sobre los argumentos y imprimir cada número de punto flotante
    for (int i = 0; i < numArgs; i++) {
        double valor = va_arg(args, double); // Obtiene el siguiente argumento como un double
        printf("%.2f ", valor);               // Imprime el valor de punto flotante con 2 decimales
    }

    va_end(args);            // Finaliza el uso de la lista de argumentos
    printf("\n");           // Imprime una nueva línea al final
    return;                 // Fin de la función
}

// Definición de una estructura llamada Persona
typedef struct {
    int id;                  // ID de la persona
    char nombre[20];        // Nombre de la persona, con un límite de 20 caracteres
} Persona;

// Función variádica para imprimir una lista de estructuras Persona
void imprimirPersonas(int numArgs, ...);
void imprimirPersonas(int numArgs, ...) {
    va_list args;              // Declara una variable para almacenar los argumentos
    va_start(args, numArgs);   // Inicializa la lista de argumentos variádicos

    // Iterar sobre los argumentos y imprimir cada estructura Persona
    for (int i = 0; i < numArgs; i++) {
        Persona persona = va_arg(args, Persona); // Obtiene el siguiente argumento como una Persona
        printf("ID: %d, Nombre: %s\n", persona.id, persona.nombre); // Imprime el ID y el nombre de la persona
    }

    va_end(args);            // Finaliza el uso de la lista de argumentos
    return;                 // Fin de la función
}

int main(void) {
    // Ejemplo de llamadas a las funciones variádicas

    // Imprimir enteros
    imprimirEnteros(3, 10, 20, 30); // Llama a la función para imprimir 3 enteros

    // Imprimir doubles
    imprimirDoubles(4, 3.14, 2.718, 1.618, 0.577); // Llama a la función para imprimir 4 números de punto flotante

    // Imprimir estructuras Persona
    Persona p1 = {1, "Daniel"};        // Inicializa la primera estructura Persona
    Persona p2 = {2, "Sixdally"};      // Inicializa la segunda estructura Persona
    imprimirPersonas(2, p1, p2); // Llama a la función para imprimir 2 estructuras Persona

    return 0; // Retorna 0 para indicar que el programa se ejecutó correctamente
}
