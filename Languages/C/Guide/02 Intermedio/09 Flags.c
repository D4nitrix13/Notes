// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

enum Colores{
    ROJO = 1,
    AZUL = 2,
    VERDE = 4,
    NARANJA = 8,
    NEGRO = 16,
    BLANCO = 32,
    TODOS = ROJO | AZUL | VERDE | NARANJA | NEGRO | BLANCO
};

void muestraColores(int color);
void muestraColores(int color){
    if (color & ROJO) printf("ROJO\n");
    if (color & AZUL) printf("AZUL\n");
    if (color & VERDE) printf("VERDE\n");
    if (color & NARANJA) printf("NARANJA\n");
    if (color & NEGRO) printf("NEGRO\n");
    if (color & BLANCO) printf("BLANCO\n");

    return;
}

// Definición de flags
#define FLAG_1 (1 << 0) // Representa el bit 0
#define FLAG_2 (1 << 1) // Representa el bit 1
#define FLAG_3 (1 << 2) // Representa el bit 2
#define FLAG_4 (1 << 3) // Representa el bit 3

int main(void) {
    // Variable que almacenará los flags
    unsigned int flags = 0;

    // Establecer flags
    flags |= FLAG_1; // Establece el bit 0
    flags |= FLAG_3; // Establece el bit 2

    // Verificar si un flag está establecido
    if (flags & FLAG_1) {
        printf("FLAG_1 está establecido\n");
    }

    // Limpiar un flag
    flags &= ~FLAG_3; // Limpia el bit 2

    // Verificar si un flag está establecido después de limpiarlo
    if (!(flags & FLAG_3)) {
        printf("FLAG_3 no está establecido\n");
    }

    // Alternativamente, puedes usar XOR para cambiar un flag
    flags ^= FLAG_2; // Si FLAG_2 está establecido, lo limpiará; si no está establecido, lo establecerá

    // Verificar el estado de todos los flags
    printf("Estado de los flags:\n");
    printf("FLAG_1: %s\n", (flags & FLAG_1) ? "Establecido" : "No establecido");
    printf("FLAG_2: %s\n", (flags & FLAG_2) ? "Establecido" : "No establecido");
    printf("FLAG_3: %s\n", (flags & FLAG_3) ? "Establecido" : "No establecido");
    printf("FLAG_4: %s\n", (flags & FLAG_4) ? "Establecido" : "No establecido");
    muestraColores(TODOS);
    return 0;
}
