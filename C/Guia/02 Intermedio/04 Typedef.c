// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "04 Typedef" "04 Typedef.c"
// Ejecucion: ./"04 Typedef"

#include <stdio.h>

// Definición de la estructura 'fecha' y su renombramiento con typedef

typedef struct
{
    unsigned int dia;
    unsigned int mes;
    unsigned int año;
} Fecha;

// Renombramiento del tipo de dato 'long int' como 'Precio'
// sintaxis dato a convertir -> dato asociado
typedef long int Precio;

int main(void)
{
    // Declaración de variables utilizando los tipos renombrados
    Precio recomendado = 80, mayorista = 50, minorista = 90;

    Fecha fecha;
    fecha.dia = 13;
    fecha.mes = 12;
    fecha.año = 2005;

    Fecha f = {13, 12, 2005}; // Creación de una variable de tipo 'Fecha'

    // Impresión de los valores
    printf("Precio recomendado: %ld\n", recomendado);
    printf("Precio mayorista: %ld\n", mayorista);
    printf("Precio minorista: %ld\n", minorista);
    printf("Fecha: %d/%d/%d\n", f.dia, f.mes, f.año);

    return 0;
}

/*
# El código proporcionado, se utiliza una estructura `typedef` para definir y renombrar tipos de datos en C, lo cual hace que el código sea más legible y fácil de mantener. Vamos a analizar y mejorar los comentarios del código:

```c
#include <stdio.h>

// Definición de la estructura 'Fecha' y su renombramiento con typedef
typedef struct
{
    unsigned int dia;
    unsigned int mes;
    unsigned int año;
} Fecha;

// Renombramiento del tipo de dato 'long int' como 'Precio'
typedef long int Precio;

int main(void)
{
    // Declaración de variables utilizando los tipos renombrados
    Precio recomendado = 80, mayorista = 50, minorista = 90;

    // Creación de una instancia 'Fecha' y asignación de valores a sus campos
    Fecha fecha;
    fecha.dia = 13;
    fecha.mes = 12;
    fecha.año = 2005;

    // Creación de una variable 'f' de tipo 'Fecha' utilizando inicialización abreviada
    Fecha f = {13, 12, 2005};

    // Impresión de los valores de precios y la fecha
    printf("Precio recomendado: %ld\n", recomendado);
    printf("Precio mayorista: %ld\n", mayorista);
    printf("Precio minorista: %ld\n", minorista);
    printf("Fecha: %d/%d/%d\n", f.dia, f.mes, f.año);

    return 0;
}
```

### Explicación Mejorada:

1. **Definición de Estructuras y `typedef`:**
   - `typedef struct { ... } Fecha;`: Define una estructura `Fecha` que contiene tres campos: `dia`, `mes` y `año`. Esta estructura se renombra como `Fecha` usando `typedef`, lo que permite usar `Fecha` como un tipo de datos en lugar de `struct Fecha`.

2. **Renombramiento de Tipos de Datos:**
   - `typedef long int Precio;`: Define `Precio` como un alias para `long int`, facilitando el uso de `Precio` en lugar de `long int` para declarar variables.

3. **Declaración y Uso de Variables:**
   - `Precio recomendado = 80, mayorista = 50, minorista = 90;`: Declara tres variables de tipo `Precio` e inicializa sus valores.
   - `Fecha fecha; fecha.dia = 13; ...`: Crea una variable `fecha` de tipo `Fecha` y asigna valores a sus campos `dia`, `mes` y `año`.
   - `Fecha f = {13, 12, 2005};`: Crea una nueva variable `f` de tipo `Fecha` utilizando inicialización abreviada con los valores `13`, `12` y `2005` para `dia`, `mes` y `año` respectivamente.

4. **Impresión de Valores:**
   - `printf("Fecha: %d/%d/%d\n", f.dia, f.mes, f.año);`: Imprime la fecha almacenada en la variable `f`, mostrando el día, mes y año separados por barras.

Este código ilustra el uso de `typedef` para simplificar la declaración de estructuras y tipos de datos en C, mejorando así la legibilidad y facilitando el mantenimiento del código.
*/