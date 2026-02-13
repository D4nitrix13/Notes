// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "01 Punteros Void" "01 Punteros Void.c"
// Ejecucion: ./"01 Punteros Void"

#include <stdio.h>

int main(void)
{
    int entero = 10;
    float flotante = 3.14;
    char caracter = 'A';

    // Declaración de puntero void
    void *ptr;

    // Asignación de direcciones de memoria a punteros void
    ptr = &entero;
    printf("Valor de entero: %d\n", *(int *)ptr); // Casting a int* para dereferenciar

    ptr = &flotante;
    printf("Valor de flotante: %.2f\n", *(float *)ptr); // Casting a float* para dereferenciar

    ptr = &caracter;
    printf("Valor de caracter: %c\n", *(char *)ptr); // Casting a char* para dereferenciar

    return 0;
}

/*
### Explicación de *(char *)ptr

```c
*(char *)ptr
```

Esto representa una operación de casting y dereferenciación de puntero. Aquí está la explicación detallada:

- **`ptr`:** Es un puntero de tipo `void *`. En C, `void *` es un tipo especial de puntero que puede apuntar a cualquier tipo de dato sin tipo específico.

- **`(char *)ptr`:** Esto es un casting explícito de `ptr` a un puntero de tipo `char *`. El operador `(char *)` indica que `ptr`, que es de tipo `void *`, se está tratando como un puntero a `char`.

- **`*(char *)ptr`:** Significa dereferenciar el puntero `ptr` después de haberlo convertido al tipo `char *`. Es decir, estamos accediendo al valor apuntado por `ptr` como si fuera un puntero a `char`.

### Significado de Casting en Programación

El casting es una operación en la que se cambia la interpretación del tipo de datos de una expresión a otro tipo de datos compatible. En el contexto de punteros, como en `*(char *)ptr`, se utiliza para interpretar un puntero de un tipo (en este caso `void *`) como un puntero de otro tipo (`char *`, `int *`, `float *`, etc.). Es crucial realizar un casting cuando se trabaja con punteros `void *` para poder acceder y manipular los datos correctamente.

### Puntero `void *` en Programación

- **`void *`:** Es un tipo especial de puntero en C que puede apuntar a cualquier tipo de dato sin tipo específico. Es útil cuando se desea tener un puntero genérico que pueda apuntar a cualquier tipo de dato y luego se pueda castear a un tipo de dato específico cuando se necesita.

### Ejemplo en Código

En el código proporcionado:

```c
int entero = 10;
float flotante = 3.14;
char caracter = 'A';

// Declaración de puntero void
void *ptr;

// Asignación de direcciones de memoria a punteros void
ptr = &entero;
printf("Valor de entero: %d\n", *(int *)ptr); // Casting a int* para dereferenciar

ptr = &flotante;
printf("Valor de flotante: %.2f\n", *(float *)ptr); // Casting a float* para dereferenciar

ptr = &caracter;
printf("Valor de caracter: %c\n", *(char *)ptr); // Casting a char* para dereferenciar
```

- `ptr` se utiliza para apuntar a diferentes tipos de datos (`entero`, `flotante`, `caracter`).
- Cada vez que se asigna una dirección de memoria a `ptr`, se hace un casting explícito para que `ptr` se interprete como un puntero al tipo de dato correcto (`int *`, `float *`, `char *`).
- Luego, `*(tipo *)ptr` se utiliza para dereferenciar `ptr` y obtener el valor almacenado en la dirección de memoria apuntada por `ptr`, según el tipo de dato correcto.

Este enfoque permite trabajar con datos de manera genérica usando `void *` y realizar operaciones específicas mediante el casting adecuado en tiempo de compilación.
*/