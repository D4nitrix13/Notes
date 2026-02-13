// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include <stdlib.h>

// Función para leer un número desde la entrada estándar con un mensaje personalizado.
int leer_numero(char *txt)
{
    int n;
    printf("%s\n", txt); // Imprime el mensaje recibido como parámetro.
    scanf("%d", &n);     // Lee un entero desde la entrada estándar y lo guarda en 'n'.
    return n;            // Devuelve el número leído.
}

/* 
   Compilación:
   Para compilar con información de depuración, se utiliza el parámetro -g con gcc.
   Esto incluye metadatos adicionales y permite el uso de herramientas como gdb para depurar.
   Ejemplo de compilación: gcc -g -o main main.c
   
   Depuración con GDB:
   - Para iniciar la depuración con gdb: gdb ./main
   - Comandos útiles:
     - list: (alias l) Muestra 10 líneas de código, se pueden especificar otras cantidades.
     - break leer_numero: Establece un punto de interrupción en la función leer_numero.
     - run: Ejecuta el programa.
     - next (alias n): Ejecuta la siguiente instrucción.
     - print: Imprime el valor de una variable o expresión.
     - ptype: Muestra el tipo de una variable.
     - continue (alias c): Continúa la ejecución después de un punto de interrupción.
     - clear leer_numero: Borra el punto de interrupción en la función leer_numero.
     - start main: Establece un punto de interrupción en main y comienza la ejecución.
     - step: Paso a paso dentro de una función en modo de depuración.
     - where: Muestra la posición actual en el código.
     - up/down: Mueve el contexto hacia arriba o abajo en la pila de llamadas.
     - finish (alias fin): Ejecuta el resto de la función actual y luego sale.
     - quit o exit: Sale de gdb.
*/

// Función principal que sumará dos números ingresados por el usuario.
int main(void)
{
    printf("Programa para sumar dos números\n");
    int a = leer_numero("Ingrese el primer número: ");   // Lee el primer número.
    int b = leer_numero("Ingrese el segundo número: ");  // Lee el segundo número.
    
    // Error intencional para propósitos de demostración.
    int res = a / b;  // Calcula la división de a entre b (puede causar un error de división por cero).
    
    printf("El resultado de %d / %d = %d\n", a, b, res);  // Imprime el resultado de la división.
    
    return EXIT_SUCCESS;  // Devuelve un código de salida exitoso.
}
