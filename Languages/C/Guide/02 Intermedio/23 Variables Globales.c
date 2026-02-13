// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h> // Incluir la biblioteca estándar de entrada/salida para usar printf

// Variable global
int globalVariable = 10; // Declarar una variable global llamada 'globalVariable' y asignarle el valor 10

// Función que usa la variable global
void funcion(void); // Declaración de la función 'funcion'

void funcion(void) { // Definición de la función 'funcion'
    // Imprimir el valor de la variable global
    printf("Valor de globalVariable dentro de la función: %d\n", globalVariable); // Accede a la variable global y la imprime
    return; // Finalizar la función
}

int main(void) { // Función principal, punto de entrada del programa
    // Acceso y modificación de la variable global
    printf("Valor de globalVariable en el main antes de modificar: %d\n", globalVariable); // Imprime el valor inicial de la variable global
    globalVariable = 20; // Modifica el valor de 'globalVariable' a 20
    printf("Valor de globalVariable en el main después de modificar: %d\n", globalVariable); // Imprime el nuevo valor de la variable global

    // Llamada a la función que utiliza la variable global
    funcion(); // Llama a la función 'funcion' que imprimirá el valor de 'globalVariable'

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
