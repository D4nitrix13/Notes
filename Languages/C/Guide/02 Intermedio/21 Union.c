// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Definición de la unión
union MiUnion { // Se define una unión llamada 'MiUnion'
    int entero;   // Miembro entero de la unión
    float flotante; // Miembro flotante de la unión
    char caracter;  // Miembro de carácter de la unión
};

int main(void) { // Función principal, punto de entrada del programa
    union MiUnion miUnion; // Declarar una variable 'miUnion' de tipo 'MiUnion'

    // Asignación de valores a la unión
    miUnion.entero = 10; // Asignar el valor 10 al miembro 'entero' de la unión
    printf("Valor entero: %d\n", miUnion.entero); // Imprimir el valor del miembro 'entero'

    // Asignar un valor al miembro 'flotante' de la unión
    miUnion.flotante = 3.14; // Asignar el valor 3.14 al miembro 'flotante'
    printf("Valor flotante: %.2f\n", miUnion.flotante); // Imprimir el valor del miembro 'flotante'

    // Asignar un valor al miembro 'caracter' de la unión
    miUnion.caracter = 'A'; // Asignar el carácter 'A' al miembro 'caracter'
    printf("Valor caracter: %c\n", miUnion.caracter); // Imprimir el valor del miembro 'caracter'

    // Imprimir el tamaño de la unión
    printf("Tamaño de la unión: %lu bytes\n", sizeof(union MiUnion)); // Imprimir el tamaño de la unión en bytes

    return 0; // Retornar 0 indica que el programa terminó con éxito
}

/*
En este ejemplo, hemos definido una unión llamada `MiUnion` que puede contener un entero (`int`), un flotante (`float`) o un caracter (`char`). Luego, en la función `main()`, creamos una instancia de esta unión llamada `miUnion`.

Hacemos varias asignaciones de valores a diferentes miembros de la unión y luego los imprimimos. Notarás que los cambios en un miembro de la unión afectan a los otros. Esto se debe a que todos los miembros comparten la misma ubicación de memoria.

Finalmente, imprimimos el tamaño de la unión utilizando `sizeof()` para demostrar cuánto espacio ocupa en la memoria.
*/
