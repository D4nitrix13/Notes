// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Directiva #if: Permite ejecutar diferentes bloques de código según condiciones
// Se usa `#if defined(...)` para verificar si una constante (en este caso, el sistema operativo) está definida
// Si se está compilando en Windows (_WIN32), se define la macro SISTEMA como "Windows"
// Si es Linux (__linux__), la define como "Linux"
// Si es macOS (__APPLE__), la define como "macOS"
// Si no se cumple ninguna de las condiciones, se define como "Desconocido"
#if defined(_WIN32)
    #define SISTEMA "Windows"
#elif defined(__linux__)
    #define SISTEMA "Linux"
#elif defined(__APPLE__)
    #define SISTEMA "macOS"
#else
    #define SISTEMA "Desconocido"
#endif

// Directiva #ifdef: Verifica si una macro (en este caso, SISTEMA) está definida
// Si SISTEMA está definida, crea una macro PRINT_SISTEMA que imprime el sistema operativo
// Si no está definida, PRINT_SISTEMA imprimirá "Sistema operativo desconocido"
#ifdef SISTEMA
    #define PRINT_SISTEMA printf("Sistema operativo: %s\n", SISTEMA);
#else
    #define PRINT_SISTEMA printf("Sistema operativo desconocido\n");
#endif

// Directiva #ifndef: Si NOMBRE no está definida, se define como "Daniel"
// `#ifndef` (if not defined) se usa para asegurarse de que una macro no esté previamente definida
#ifndef NOMBRE
    #define NOMBRE "Daniel"
#endif

// Directiva #include condicional: Según el sistema operativo, se incluye un fichero de cabecera específico
// Si estamos en Windows, se incluye "windows.h"
// Si estamos en Linux o macOS, se incluye "unistd.h" (tiene funciones del sistema UNIX como sleep)
#ifdef _WIN32
    #include "windows.h"
#elif defined(__linux__)
    #include "unistd.h"
#elif defined(__APPLE__)
    #include "unistd.h"
#endif

// Directiva #pragma: Se usa para dar instrucciones específicas al compilador
// En este caso, deshabilita la advertencia de código 4996, que suele aparecer en compiladores de Windows para ciertas funciones
#pragma warning(disable: 4996)

// Directiva #error: Si la macro NOMBRE no está definida, genera un error en la compilación
// Esto fuerza al programador a definir NOMBRE antes de compilar
#ifndef NOMBRE
    #error "La variable NOMBRE no está definida"
#endif

int main(void) {
    // Uso de la macro NOMBRE, que se imprime en pantalla
    printf("Nombre: %s\n", NOMBRE);

    // Uso de las funciones definidas en los ficheros de cabecera incluidos
    // Si estamos en Windows, se usa la función Sleep de "windows.h"
    // Si estamos en Linux o macOS, se usa la función sleep de "unistd.h"
    #ifdef _WIN32
        printf("Directiva para Windows\n");
        Sleep(1000); // Pausa de 1 segundo (en milisegundos)
    #elif defined(__linux__) || defined(__APPLE__)
        printf("Directiva para Linux o macOS\n");
        sleep(1); // Pausa de 1 segundo
    #endif

    // Uso de la macro PRINT_SISTEMA, que imprime el sistema operativo
    PRINT_SISTEMA;

    return 0;
}

