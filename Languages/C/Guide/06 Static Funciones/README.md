<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***En C, la palabra clave `static` se puede utilizar en el contexto de funciones para limitar el alcance de la función al fichero en el que se define. Esto significa que la función solo es visible y accesible desde dentro del fichero en el que se define***

*Aquí tienes un ejemplo de cómo usar una función `static` en C:*

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
// main.c

#include <stdio.h>

// Declaración de la función static
static void funcionStatic(void);
static void funcionStatic(void) {
    printf("Esta es una función static.\n");
}

// Función principal
int main(void) {
    // Llamada a la función static
    funcionStatic();
    return 0;
}
```

*En este ejemplo, la función `funcionStatic()` está marcada como `static`, lo que significa que solo es visible dentro de `fichero.c`. Si intentas llamar a `funcionStatic()` desde otro fichero, obtendrás un error de enlace.*

*La declaración `static` también se puede aplicar a variables dentro de una función, lo que hace que la variable conserve su valor entre llamadas a la función. Por ejemplo:*

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

void funcion(void);
void funcion(void) {
    // Variable static
    static int contador = 0;
    
    contador++;
    printf("El contador es: %d\n", contador);
    return;
}

int main(void) {
    funcion();
    funcion();
    funcion();
    
    return 0;
}
```

*En este caso, la variable `contador` conserva su valor entre las llamadas a la función `funcion()`, lo que produce una salida de:*

```txt
El contador es: 1
El contador es: 2
El contador es: 3
```

*Es importante tener en cuenta que las funciones y variables `static` solo son visibles dentro del fichero en el que se definen, lo que significa que no pueden ser accedidas desde otros ficheros fuente mediante enlace externo. Esto puede ser útil para encapsular la funcionalidad dentro de un fichero y evitar conflictos de nombres con otras partes del programa.*
