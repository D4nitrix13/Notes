// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#ifndef LIB
#include "../lib/color.h"
#include <stdbool.h>
#define LIB true

// Declaración de la estructura ListaInt
struct ListaInt {
    long int longitud;
    long double *arreglo;
};

// Definición de un alias "List" para "struct ListaInt"
typedef struct ListaInt List;

extern void añadirItem(List *lista, const int item);
extern void eliminarItemValor(List *lista, const int item);
extern void eliminarItemIndice(List *lista, const int indice);
extern void imprimirListaInt(const List *lista);
extern List *crearListaInt(void);
extern void liberarListInt(List *lista);

extern void eliminarItemValor(List *lista, const int item){
    if (!lista->longitud){
        printf("%s%sLista vacia\n%s",colorear("rojo"),style("negrita"),resetColor());
        return;
    }
    bool existeItem = false;
    int indice;
    for (int i = 0; i < lista->longitud; i++){
       if (lista->arreglo[i] == item){
        indice = i;
        existeItem = true;
        break;
       }
    }
    
    if (!existeItem){
        printf("%s%sItem %d no existe\n%s",colorear("rojo"),style("negrita"),item,resetColor());
        return;
    }
    eliminarItemIndice(lista,indice);
    return;

}
extern void eliminarItemIndice(List *lista, const int indice){
    if (!lista->longitud){
       printf("%s%sLista vacia\n%s",colorear("rojo"),style("negrita"),resetColor());
        return;
    }else if (indice > lista->longitud){
        printf("%s%sIndexError: %s%sEl indice al que intenta acceder esta fuera de rango\n\n", colorear("rojo"),style("negrita"),colorear("magneta"),style("subrayado"));
        exit(1);
    }
    long double *array = (long double *)malloc((lista->longitud - 1) * sizeof(long double));
    if (array == NULL) {
        perror("Error al asignar memoria para el nuevo arreglo");
        exit(1);
    }
    bool existe = false;

    for (int i = 0; i < lista->longitud; i++){
        if (i == indice){
            existe = true;
            continue;
        }
        if (existe){
            array[i - 1] = lista->arreglo[i];
            continue;
        }
        array[i] = lista->arreglo[i];
    }
    // Decrementar la longitud de la lista
    lista->longitud--;

    // Liberar la memoria del arreglo anterior
    free(lista->arreglo);

    // Actualizar el puntero del arreglo de la lista al nuevo arreglo
    lista->arreglo = array;
    return;
}

extern void liberarListInt(List *lista){
    free(lista->arreglo);
    free(lista);
    return;
}

extern void añadirItem(List *lista, const int item){
    long double *array = (long double*)malloc((lista->longitud + 1) * sizeof(long double));

    if (array == NULL){
        perror("Error al asignar memoria para el nuevo arreglo");
        exit(1);
    }

    // Copiar los elementos anteriores al nuevo arreglo
    memcpy(array, lista->arreglo, lista->longitud * sizeof(long double));
    /*
    La función `memcpy` se utiliza para copiar un bloque de memoria de una ubicación a otra. En este caso, se está utilizando para copiar los elementos existentes en el arreglo `lista->arreglo` a un nuevo arreglo `array`.

    Aquí está la explicación detallada de cómo funciona esta línea de código:

    ```c
    memcpy(array, lista->arreglo, lista->longitud * sizeof(long double));
    ```

    - `array`: Es el destino de la copia. Es un puntero al nuevo arreglo donde se copiarán los elementos.

    - `lista->arreglo`: Es el origen de la copia. Es un puntero al arreglo existente que contiene los elementos que queremos copiar.

    - `lista->longitud * sizeof(long double)`: Es el número total de bytes que queremos copiar. `lista->longitud` es el número de elementos en el arreglo `lista->arreglo`, y `sizeof(long double)` es el tamaño de cada elemento en bytes. Multiplicar estos dos valores nos da el total de bytes que queremos copiar.

    Entonces, `memcpy` copiará `lista->longitud` elementos de `lista->arreglo` al arreglo `array`, cada elemento con un tamaño de `sizeof(long double)` bytes.

    Esta línea de código asegura que los elementos anteriores en `lista->arreglo` sean copiados al nuevo arreglo `array` antes de agregar el nuevo elemento. Esto garantiza que no se pierdan los datos existentes cuando se agrega un nuevo elemento a la lista.

    memcpy(El destino de la copia,El origen de la copia, El número de bytes que deseas copiar);
    */

    // Agregar el nuevo elemento al final del nuevo arreglo
    array[lista->longitud] = item;

    // Incrementar la longitud de la lista
    lista->longitud++;

    // Liberar la memoria del arreglo anterior
    free(lista->arreglo);

    // Actualizar el puntero del arreglo de la lista al nuevo arreglo
    lista->arreglo = array;

    return;
}

extern void imprimirListaInt(const List *lista){
    if (!lista->longitud){
        printf("%s%sLista vacia\n%s",colorear("rojo"),style("negrita"),resetColor());
        return;
    }
    for (int i = 0; i < lista->longitud; i++){
        printf("%s%s%Lf\n%s",colorear("verde"),style("negrita"),lista->arreglo[i],resetColor());
    }
    printf("\n");
    return;
}

extern List *crearListaInt(void){
    List *l = (List *)malloc(1 * sizeof(List));
    l->longitud = 0;
    l->arreglo = NULL;
    return l;
}


#endif