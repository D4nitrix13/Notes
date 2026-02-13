// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include "../lib/lib.h"

#define CODE_SUCCESSFUL return 0
#define CODE_NOT_SUCCESSFUL return 1

int main(void){
    List *lista = crearListaInt();
    
    if (lista == NULL){
        perror("List *lista = crearListaInt(); -> Error al asignar la memoria");
        CODE_NOT_SUCCESSFUL;
    }
    for (int i = 0; i < 10; i++) {
        añadirItem(lista, i);   
    }
    imprimirListaInt(lista);
    eliminarItemValor(lista,2);
    imprimirListaInt(lista);
    liberarListInt(lista);
    CODE_SUCCESSFUL;
}