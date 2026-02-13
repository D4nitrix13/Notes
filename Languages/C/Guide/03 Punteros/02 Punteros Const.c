// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "02 Punteros Const" "02 Punteros Const.c"
// Ejecucion: ./"02 Punteros Const"

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int num = 10;
    const int *ptr; // Puntero a un entero constante

    // Asignación de la dirección de memoria de 'num' al puntero
    ptr = &num;

    // Intento de modificar el valor a través del puntero (comentado porque dará error)
    // *ptr = 20; // Esto dará un error, ya que no se puede modificar el valor a través del puntero

    // Imprimir el valor apuntado por el puntero (sí se puede acceder, pero no modificar)
    printf("Valor de num: %d\n", *ptr);

    return EXIT_SUCCESS;
}
