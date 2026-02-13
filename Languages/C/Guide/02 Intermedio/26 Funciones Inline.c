// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h> // Incluir la biblioteca estándar de entrada/salida para usar printf

// Declaración de la función inline
inline int suma(int a, int b); // Declaración anticipada de la función 'suma' como inline

// Definición de la función inline
inline int suma(int a, int b) { // Definición de la función 'suma' que toma dos enteros como parámetros
    return a + b; // Retorna la suma de 'a' y 'b'
}

int main(void) { // Función principal, punto de entrada del programa
    int x = 10, y = 20; // Declarar dos variables enteras 'x' e 'y' e inicializarlas con 10 y 20
    int resultado; // Declarar una variable entera 'resultado' para almacenar el resultado de la suma

    // Llamada a la función inline
    resultado = suma(x, y); // Llama a la función 'suma' pasando 'x' e 'y' como argumentos y almacena el resultado en 'resultado'

    // Imprimir el resultado de la suma
    printf("La suma de %d y %d es %d\n", x, y, resultado); // Imprime los valores de 'x', 'y' y 'resultado'

    return 0; // Retornar 0 indica que el programa terminó con éxito
}

/*
Para declarar una función `inline` en C, se utiliza la palabra clave `inline` antes de la declaración de la función. Sin embargo, esta es solo una sugerencia al compilador, y el compilador puede optar por no seguir la sugerencia si lo considera apropiado.

En este ejemplo, la función `suma` está declarada como `inline`. Cuando el compilador encuentra una llamada a esta función, puede optar por reemplazar la llamada con el cuerpo de la función en línea, en lugar de realizar una llamada de función normal. Esto puede mejorar el rendimiento en algunos casos.

Es importante tener en cuenta que el uso de funciones `inline` puede aumentar el tamaño del código generado, ya que el cuerpo de la función puede duplicarse en varios lugares donde se llama. Además, las funciones `inline` no se pueden recursivas y no pueden tener definiciones recursivas o tener un bucle `while`.
*/
