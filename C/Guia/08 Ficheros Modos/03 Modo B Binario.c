// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>

int main(void) {
    FILE *fichero;
    char texto[] = "Hola, este es un ejemplo de texto.";
    char buffer[100];
    // Modo "b": abrir en modo binario
    fichero = fopen("fichero.bin", "wb");
    if (fichero == NULL) {
        printf("No se pudo abrir el fichero binario en modo escritura.\n");
        return 1;
    }
    fwrite(texto, sizeof(char), sizeof(texto), fichero);
    fclose(fichero);
    printf("Se ha escrito en el fichero binario.\n");
    return 0;
}
