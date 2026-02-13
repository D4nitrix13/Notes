// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>    // Incluir la biblioteca estándar de entrada/salida para usar printf
#include <stdarg.h>   // Incluir la biblioteca para manejar funciones variádicas

// Función variádica para calcular el promedio de una lista de números
double promedio(int numArgs, ...); // Declaración de la función variádica 'promedio'

// Definición de la función variádica 'promedio'
double promedio(int numArgs, ...) {
    va_list args;            // Declara una lista de argumentos
    double suma = 0.0;      // Inicializa la variable 'suma' a 0.0
    
    va_start(args, numArgs);    // Inicializa la lista de argumentos a partir del último parámetro fijo
    
    // Itera a través de los argumentos sumando los valores
    for (int i = 0; i < numArgs; i++) {
        suma += va_arg(args, double); // Extrae el siguiente argumento de tipo double y lo suma a 'suma'
    }
    
    va_end(args);    // Finaliza la lista de argumentos
    
    return suma / numArgs; // Devuelve el promedio dividiendo la suma por el número de argumentos
}

int main(void) { // Función principal, punto de entrada del programa
    // Calcula el promedio de 3 números
    double prom = promedio(3, 5.0, 7.0, 9.0); // Llama a la función 'promedio' con 3 argumentos y almacena el resultado en 'prom'
    printf("El promedio es: %.2f\n", prom); // Imprime el promedio con 2 decimales
    
    // Calcula el promedio de 5 números
    prom = promedio(5, 12.0, 15.0, 18.0, 20.0, 25.0); // Llama a la función 'promedio' con 5 argumentos
    printf("El promedio es: %.2f\n", prom); // Imprime el nuevo promedio

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
