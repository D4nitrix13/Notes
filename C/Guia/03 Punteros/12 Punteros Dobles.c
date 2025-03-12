// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h> // Incluir la biblioteca estándar de entrada/salida para usar funciones como printf

int main(void) { // Función principal, punto de entrada del programa
    int numero = 42; // Declarar una variable entera llamada 'numero' y asignarle el valor 42
    int *puntero1; // Declarar un puntero a un entero; 'puntero1' almacenará la dirección de memoria de un entero
    int **puntero2; // Declarar un puntero a un puntero a un entero; 'puntero2' almacenará la dirección de memoria de un puntero

    // Asignar la dirección de memoria de 'numero' al puntero1
    puntero1 = &numero; // El operador '&' obtiene la dirección de memoria de 'numero'

    // Asignar la dirección de memoria de 'puntero1' al puntero2
    puntero2 = &puntero1; // 'puntero2' ahora apunta a la dirección de 'puntero1'

    // Imprimir los valores
    printf("Valor de 'numero': %d\n", numero); // Imprime el valor de 'numero' (42)
    
    // Imprimir el valor al que apunta puntero1, que es el valor de 'numero'
    printf("Valor de '*puntero1': %d\n", *puntero1); // El operador '*' desreferencia 'puntero1' para obtener el valor en la dirección a la que apunta (42)
    
    // Imprimir el valor al que apunta puntero2 (que a su vez apunta a puntero1)
    printf("Valor de '**puntero2': %d\n", **puntero2); // Desreferenciamos puntero2 para obtener el valor de 'numero'; desreferenciamos dos veces

    // Imprimir las direcciones de memoria
    printf("Dirección de memoria de 'numero': %p\n", (void *)&numero); // Imprime la dirección de memoria de 'numero'; '&' obtiene la dirección
    printf("Dirección de memoria de 'puntero1': %p\n", (void *)puntero1); // Imprime la dirección de memoria a la que apunta puntero1 (dirección de 'numero')
    printf("Dirección de memoria de 'puntero2': %p\n", (void *)puntero2); // Imprime la dirección de memoria a la que apunta puntero2 (dirección de puntero1)

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
