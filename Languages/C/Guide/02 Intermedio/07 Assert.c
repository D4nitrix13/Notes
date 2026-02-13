// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>
#include <assert.h> // La librería assert permite verificar condiciones durante la ejecución del programa

int main(void) {
    int x = 5;
    int y = 10;

    // Asegurarse de que x sea igual a 5
    // Si la condición (x == 5) es verdadera, el programa continúa normalmente
    // Si la condición es falsa, el programa se detiene con un mensaje de error
    assert(x == 5);

    // Asegurarse de que y sea menor que 10 (esto fallará)
    // Esta condición es falsa, ya que y es igual a 10, por lo tanto, assert fallará
    // Al fallar, el programa se detiene y se imprime un mensaje de error, indicando el fichero, la línea y la condición fallida
    assert(y < 10);

    // Este mensaje no se imprimirá porque el programa se detiene en el assert anterior
    printf("Todo está bien\n");

    return 0;
}
