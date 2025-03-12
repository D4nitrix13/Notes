// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>

int main(void) {
    FILE *fichero;
    char texto[] = "Hola, este es un ejemplo de texto.";
    char buffer[100];

    // Modo "w": escribir en el fichero
    fichero = fopen("fichero.txt", "w");
    if (fichero == NULL) {
        printf("No se pudo abrir el fichero en modo escritura.\n");
        return 1;
    }
    fprintf(fichero, "%s\n", texto);
    fclose(fichero);
    printf("Se ha escrito en el fichero.\n");

    return 0;
}
