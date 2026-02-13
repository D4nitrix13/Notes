// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h> // Incluir la biblioteca estándar de entrada/salida para usar printf

int main(void) { // Función principal, punto de entrada del programa
    int puntaje = 85; // Declarar una variable entera 'puntaje' y asignarle el valor 85
    char calificacion; // Declarar una variable de tipo carácter 'calificacion' para almacenar la calificación

    // Asignar la calificación según el puntaje usando el operador ternario
    calificacion = (puntaje >= 90) ? 'A' : // Si 'puntaje' es mayor o igual a 90, asignar 'A'
                   (puntaje >= 80) ? 'B' : // Si 'puntaje' es mayor o igual a 80, asignar 'B'
                   (puntaje >= 70) ? 'C' : // Si 'puntaje' es mayor o igual a 70, asignar 'C'
                   'D'; // Si 'puntaje' es menor que 70, asignar 'D'

    // Imprimir la calificación
    printf("La calificación es: %c\n", calificacion); // Imprimir el valor de 'calificacion'

    return 0; // Retornar 0 indica que el programa terminó con éxito
}
