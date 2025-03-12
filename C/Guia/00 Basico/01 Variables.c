// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "01 Variables" "01 Variables.c" 
// Ejecucion: ./"01 Variables"

/*
******************************
*     Tema: Tipos de Datos    *
*     Nivel: Basico           *
******************************
*/

// Instrucción del preprocesador: Incluye los ficheros de cabecera estándar para entrada y salida (stdio.h), booleanos (stdbool.h) y números complejos (complex.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf.
#include <stdbool.h>    // stdbool.h define el tipo de dato booleano.
#include <complex.h>    // complex.h define los tipos de datos y funciones para números complejos.

int main(void) {
    /**
     * **Comentario Doxygen:** 
     * Se utiliza para generar documentación automáticamente a partir del código fuente.
    */

    // **Variables y constantes**
    // Definición y inicialización de variables y constantes de diferentes tipos de datos.

    float variable_flotante = 10.5;     // *variable_flotante*: Variable de tipo float.
    const int constante = 3.141592;     // *constante*: Constante de tipo int.

    // **Tipos de datos enteros**
    int numero = 10;                    // *Entero estándar*.
    short int numero_corto = 10;        // *Entero corto*.
    long int numero_largo = 100000;     // *Entero largo*.
    long long numero_muy_largo = 10000000000;  // *Entero muy largo*.

    // **Tipos de datos flotantes**
    float flotante = 3.141592;                // *Número flotante*.
    double doble = 1.4142;                    // *Número de doble precisión*.
    long double doble_largo = 3.423482349283479283;  // *Número de precisión extendida*.

    // **Tipos de datos complejos**
    float _Complex complejo_float = 1.0 + 2.0i;         // *Número complejo de tipo float*.
    double _Complex complejo_doble = 1.0 + 2.0i;        // *Número complejo de tipo double*.
    long double _Complex complejo_largo_doble = 1.0 + 2.0i;  // *Número complejo de tipo long double*.

    // **Tipos de datos de caracteres**
    char caracteres = 'A';                // *Carácter*.
    unsigned char caracter_sin_signo = 'B';  // *Carácter sin signo*.

    // **Tipo de dato booleano**
    bool boleano = true;      // *Booleano verdadero*.
    bool boleano_2 = false;   // *Booleano falso*.

    // **Impresión de valores**
    // Imprime los valores de las variables definidas anteriormente.
    printf("\n Hola, Lenguaje C rendimiento 100%% \n\n");
    printf("Entero: %d\n", numero);
    printf("Entero corto: %hd\n", numero_corto);
    printf("Entero largo: %ld\n", numero_largo);
    printf("Entero muy largo: %lld\n", numero_muy_largo);

    printf("Flotante: %f\n", flotante);
    printf("Doble: %lf\n", doble);
    printf("Doble largo: %Lf\n", doble_largo);

    printf("Complejo flotante: %f + %fi\n", crealf(complejo_float), cimagf(complejo_float));
    printf("Complejo doble: %lf + %lfi\n", creal(complejo_doble), cimag(complejo_doble));
    printf("Complejo largo doble: %Lf + %Lfi\n", creall(complejo_largo_doble), cimagl(complejo_largo_doble));

    printf("Carácter: %c\n", caracteres);
    printf("Carácter sin signo: %c\n", caracter_sin_signo);

    printf("Booleano: %d\n", boleano);
    printf("Booleano 2: %d\n", boleano_2);
    
    return 0;  // *Indica que el programa terminó correctamente*.
}

/*
** Ilustración ASCII de los tipos de datos :**

1. *Tipos Enteros*:
   +--------+
   |  int   |  // Entero estándar.
   +--------+
   | short  |  // Entero corto.
   +--------+
   |  long  |  // Entero largo.
   +--------+
   |  long  |
   |  long  |  // Entero muy largo.
   +--------+

2. *Tipos Flotantes*:
   +--------+
   | float  |  // Flotante.
   +--------+
   | double |  // Doble precisión.
   +--------+
   |  long  |
   | double |  // Precisión extendida.
   +--------+

3. *Tipos Complejos*:
   +-----------------+
   | float _Complex  |  // Complejo de tipo float.
   +-----------------+
   | double _Complex |  // Complejo de tipo double.
   +-----------------+
   | long double _Complex  |  // Complejo de tipo long double.
   +-----------------+

4. *Tipos de Caracteres*:
   +--------+
   |  char  |  // Carácter.
   +--------+
   | uchar  |  // Carácter sin signo.
   +--------+

5. *Tipo Booleano*:
   +------+
   | bool |  // Booleano (true/false).
   +------+

*Nota*: Los números complejos usan la notación `real + imaginario * i`.
*/

/*
# **para imprimir variables en C**

1. **Enteros**

    - **`%d`:** *Para enteros.*
    - **`%hd`:** *Para enteros cortos (short int).*
    - **`%ld`:** *Para enteros largos (long int).*
    - **`%lld`:** *Para enteros muy largos (long long).*

2. **Float**

   - **`%f`:** *Para flotantes (float).*
   - **`%lf`:** *Para dobles (double).*
   - **`%Lf`:** *Para dobles largos (long double).*
   - **`%f` + `%fi`, `%lf` + `%lfi`, `%Lf` + `%Lfi`:** *Para imprimir los componentes reales e imaginarios de los números complejos.*

3. **Caracteres**

   - **`%c`:** *Para caracteres.*
   - **`%d`:** *Para valores booleanos (bool).*

> [!NOTE]
> *Es importante recordar que, para imprimir los componentes reales e imaginarios de los números complejos, se utilizan las funciones `crealf()`, `cimagf()`, `creal()`, `cimag()`, `creall()` y `cimagl()` para obtener la parte real e imaginaria de los números complejos de tipo `float`, `double` y `long double` respectivamente.*

---

## ***Datos interesantes***

1. **Enteros:**

   - **`int`:** *32 bits en la mayoría de las implementaciones modernas (puede ser 16 bits en sistemas embebidos o antiguos).*

   - **`short int`:** *16 bits.*

   - **`long int`:** *32 bits en sistemas de 32 bits y 64 bits en sistemas de 64 bits.*

   - **`long long`:** *64 bits.*

2. **Punto flotante:**

   - **`float`:** *32 bits.*

   - **`double`:** *64 bits.*

   - **`long double`:** *64 bits o 80 bits en la mayoría de las implementaciones modernas.*

3. **Caracteres:**

   - **`char`:** *8 bits.*

   - **`unsigned char`:** *8 bits.*

4. **Booleano:**

   - **`bool`:** *No está definido por el estándar C, pero suele ser 8 bits (1 byte) ya que se suele tratar como un tipo de datos entero.*

> [!IMPORTANT]
> *Es importante tener en cuenta que estos tamaños pueden variar dependiendo del compilador y la arquitectura del sistema. Por lo tanto, si necesitas conocer con precisión los tamaños en bits de los tipos de datos en tu sistema específico, puedes utilizar la función `sizeof()` en C para obtener la cantidad de bytes que ocupa cada tipo de datos y luego multiplicar por 8 para obtener la cantidad en bits. Por ejemplo:*

```c
printf("Tamaño de int en bits: `%lu`\n", sizeof(int) * 8);
```

*Esto imprimirá el tamaño del tipo de datos `int` en bits en tu sistema específico.*

*/