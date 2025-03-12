// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>

int main(void) {
    FILE *fichero;
    char texto[] = "Hola, este es un ejemplo de texto.";
    char buffer[100];
    // Modo combinado: "r+" para lectura y escritura
    fichero = fopen("fichero.txt", "r+");
    if (fichero == NULL) {
        printf("No se pudo abrir el fichero en modo lectura y escritura.\n");
        return 1;
    }
    fputs("Texto añadido en modo combinado.", fichero);
    fseek(fichero, 0, SEEK_SET);
    fgets(buffer, 100, fichero);
    printf("Contenido del fichero (modo combinado): %s", buffer);
    fclose(fichero);

    return 0;
}
