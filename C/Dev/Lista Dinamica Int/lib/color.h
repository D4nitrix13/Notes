// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#ifndef COLOR
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "../lib/utilidades.h"

#define COLOR true

static char TOTAL_COLORES[8][9] = {
    "NEGRO",
    "ROJO",
    "VERDE",
    "AMARILLO",
    "AZUL",
    "MAGNETA",
    "CYAN",
    "BLANCO"
};

static char TOTAL_STYLES[5][10] = {
    "NEGRITA",
    "SUBRAYADO",
    "INVERTIDO",
};

static char CODE_COLORES[8][6] = {
    "\x1b[30m",
    "\x1b[31m",
    "\x1b[32m",
    "\x1b[33m",
    "\x1b[34m",
    "\x1b[35m",
    "\x1b[36m",
    "\x1b[37m"
};

static char CODE_STYLES[3][5] = {
   "\x1b[1m",
   "\x1b[4m",
   "\x1b[7m"
};

extern char *resetColor(void);
extern char *resetColor(void){
    return "\x1b[0m";
}

extern char *colorear(char *color);
extern char *colorear(char *color){
   char *copy_color = strdup(color); // Copiamos la cadena a una nueva área de memoria
    if (copy_color == NULL) {
        // Manejo del error de memoria
        return NULL;
    }
    convertirMayusculas(copy_color);
    for (int i = 0; i < sizeof(TOTAL_COLORES) / sizeof(TOTAL_COLORES[0]); i++){
        if (strcmp(copy_color, TOTAL_COLORES[i]) == 0){
            free(copy_color);
            return CODE_COLORES[i];
        }
    }
    free(copy_color);
    return CODE_COLORES[7];
}
// char *Background(char *background);


extern char *style(char *style);
extern char *style(char *style){
    char *style_copy = strdup(style);
    if (style_copy == NULL){
        // Manejo del error de memoria
        return NULL;
    }
    convertirMayusculas(style_copy);
    for (int i = 0; i < (int) (sizeof(TOTAL_STYLES) / sizeof(TOTAL_STYLES[0])); i++){
        if (strcmp(style_copy, TOTAL_STYLES[i]) == 0){
            free(style_copy);
            return CODE_STYLES[i];
        }
    }
    free(style_copy);
    return CODE_STYLES[0];
    
}


#endif