// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>    // Incluir la biblioteca estándar de entrada/salida para usar printf y puts
#include <string.h>   // Incluir la biblioteca para funciones de manipulación de cadenas como strcpy, strcat, strlen y memset

int main(void) { // Función principal, punto de entrada del programa
    // Inicializar cadenas
    char str1[] = "Hola";        // Cadena str1 inicializada con "Hola"
    char str2[] = "Mundo";       // Cadena str2 inicializada con "Mundo"
    char str3[20];               // Cadena str3 de tamaño 20 para almacenar resultados
    char str4[20] = "¡Hola, ";    // Cadena str4 inicializada con "¡Hola, "
    char str5[] = "Mundo!";      // Cadena str5 inicializada con "Mundo!"
    int longitud;                // Variable para almacenar la longitud de una cadena

    // Copiar una cadena en otra
    strcpy(str3, str1);          // Copia el contenido de str1 en str3
    puts("strcpy(str3, str1):"); // Imprimir un mensaje
    puts(str3);                  // Imprimir el contenido de str3, que ahora es "Hola"

    // Concatenar dos cadenas
    strcat(str4, str5);          // Concatena str5 al final de str4, resultando en "¡Hola, Mundo!"
    puts("strcat(str4, str5):"); // Imprimir un mensaje
    puts(str4);                  // Imprimir el contenido de str4, que ahora es "¡Hola, Mundo!"

    // Longitud de una cadena
    longitud = strlen(str4);     // Calcula la longitud de str4 y la almacena en longitud
    printf("strlen(str4): %d\n", longitud); // Imprime la longitud de str4

    // Comparar dos cadenas
    if (strcmp(str1, str2) == 0) { // Compara str1 y str2
        printf("Las cadenas son iguales\n"); // Si son iguales, imprime un mensaje
    } else {
        printf("Las cadenas son diferentes\n"); // Si son diferentes, imprime un mensaje
    }

    // Usando memset para establecer todos los elementos de str3 a '\0'
    memset(str3, '\0', sizeof(str3)); // Establece todos los bytes de str3 a 0 (null terminator)
    puts("str3 después de memset:");  // Imprimir un mensaje
    puts(str3);                        // Imprimir el contenido de str3, que ahora es una cadena vacía

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
