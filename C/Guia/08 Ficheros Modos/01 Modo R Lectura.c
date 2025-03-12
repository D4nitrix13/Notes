// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>

int main(void){
    FILE *fichero;
    char buffer[100];
    // Modo "r": leer del fichero
    fichero = fopen("fichero.txt", "r");
    if (fichero == NULL) {
        printf("No se pudo abrir el fichero en modo lectura.\n");
        return 1;
    }
    fgets(buffer, 100, fichero);
    printf("Contenido del fichero (modo lectura): %s", buffer);
    fclose(fichero);

    
    return;

}