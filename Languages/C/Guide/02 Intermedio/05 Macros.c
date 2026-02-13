// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

/*
Las macros son una característica del preprocesador en el lenguaje C que permite la definición de constantes y fragmentos de código que son reemplazados por el preprocesador antes de la compilación.
*/

#include <stdio.h>

// Definición de constantes con macros
// Definimos una constante PI que será reemplazada por su valor 3.14 antes de la compilación
#define PI 3.14

// Definimos una macro que suma dos valores x e y. Los paréntesis adicionales aseguran la precedencia correcta de las operaciones
#define SUMA(x,y) ((x) + (y))

// Macros que controlan el flujo de retorno del programa
// BIEN es reemplazada por "return 0", lo que indica una ejecución exitosa
#define BIEN return 0

// ERROR es reemplazada por "return 1", lo que puede usarse para indicar un error en el programa
#define ERROR return 1

int main(int argc, char *argv[]) {
    // Uso de la macro SUMA para realizar una suma
    printf("Suma: %d\n", SUMA(10, 10)); // SUMA(10, 10) se expande a ((10) + (10)) por el preprocesador

    // Uso de macros condicionales
    // #ifndef verifica si la macro NOMBRE no está definida. Si no lo está, se ejecuta el bloque de código siguiente
    #ifndef NOMBRE
    printf("No tienes nombre\n");
    #endif

    // Comprobación de si la constante PI está definida
    // #ifdef verifica si PI está definida. Si lo está, se ejecuta el bloque de código correspondiente
    #ifdef PI
    printf("PI está definido: %.2f\n", PI); // PI se expande a 3.14
    #else
    printf("PI no está definido\n");
    #endif

    // Eliminar la definición de las macros PI y SUMA para que no se puedan usar después de esta línea
    #undef PI
    #undef SUMA

    // Retorno exitoso del programa utilizando la macro BIEN
    BIEN;

    // Nota: Se ha eliminado la parte de código condicional al final debido a que no estaba relacionada con el tema de las macros

    return 0;
}
