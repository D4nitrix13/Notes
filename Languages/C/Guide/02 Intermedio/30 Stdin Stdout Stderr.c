// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

int main(void)
{
    // Redirigiendo la salida estándar a un fichero
    FILE *fichero = stdout; // Redirige a la salida estándar
    fprintf(fichero, "Este es un mensaje que será redirigido a la salida estándar (stdout).\n");

    // Leyendo desde la entrada estándar
    char buffer[100];
    printf("Por favor, ingrese una cadena: ");
    fgets(buffer, sizeof(buffer), stdin);         // Lee desde la entrada estándar
    fprintf(stdout, "Usted ingresó: %s", buffer); // Escribe en la salida estándar

    // Ejemplo de uso de stderr
    fprintf(stderr, "Este es un mensaje de error que se enviará a la salida de error (stderr).\n");
    
    // Simular un error
    int errorOcurrido = 1; // Variable para simular si ha ocurrido un error
    if (errorOcurrido) {
        fprintf(stderr, "Error: Ocurrió un problema al procesar la información.\n");
    }

    return 0;
}

