// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h> // Incluir la biblioteca estándar de entrada/salida para usar printf

int main(void) { // Función principal, punto de entrada del programa
    int numero = 15; // Declarar una variable entera 'numero' e inicializarla con el valor 15
    // Usar un operador ternario para asignar un mensaje dependiendo de si 'numero' es par o impar
    char *mensaje = (numero % 2 == 0) ? "Es par" : "Es impar"; // 
    // 'numero % 2 == 0' evalúa si 'numero' es divisible entre 2 (es par)
    // Si es verdadero, 'mensaje' se asigna a "Es par"; si es falso, se asigna a "Es impar"

    printf("%s\n", mensaje); // Imprimir el mensaje en la consola

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
