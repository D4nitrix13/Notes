// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>

int main(void) {
    FILE *fichero;
    char buffer[100];
    // Modo "a": anexar al fichero
    fichero = fopen("fichero.txt", "a");
    if (fichero == NULL) {
        printf("No se pudo abrir el fichero en modo anexar.\n");
        return 1;
    }
    fprintf(fichero, "Esta línea será anexada al fichero.\n");
    fclose(fichero);
    printf("Se ha anexado al fichero.\n");
    return 0;
}