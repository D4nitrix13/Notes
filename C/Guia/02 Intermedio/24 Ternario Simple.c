// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h> // Incluir la biblioteca estándar de entrada/salida para usar printf

int main(void) { // Función principal, punto de entrada del programa
    int a = 10; // Declarar una variable 'a' y asignarle el valor 10
    int b = 20; // Declarar una variable 'b' y asignarle el valor 20

    // Operador ternario para determinar el máximo entre 'a' y 'b'
    int maximo = (a > b) ? a : b; // Si 'a' es mayor que 'b', 'maximo' recibe el valor de 'a', de lo contrario recibe el valor de 'b'

    // Imprimir el valor máximo
    printf("El máximo es: %d\n", maximo); // Imprimir el valor de 'maximo'

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
