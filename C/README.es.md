<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***Guía de Sintaxis y Código en C***

- *¡Bienvenido! Este repositorio proporciona una guía completa sobre la sintaxis y el código en C, incluyendo ejemplos prácticos. Aquí aprenderás los fundamentos del lenguaje C y cómo escribir programas eficientes y bien estructurados.*

## ***Autor***

- **Nombre:** **Daniel Benjamin Perez Morales**
- **GitHub:** *[D4nitrix13](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")*
- **Correo Electrónico:** *<danielperezdev@proton.me>*

## ***Índice***

- [***Guía de Sintaxis y Código en C***](#guía-de-sintaxis-y-código-en-c)
  - [***Autor***](#autor)
  - [***Índice***](#índice)
  - [***Introducción***](#introducción)
  - [***Configuración del Entorno***](#configuración-del-entorno)
    - [***Instalación de un Compilador***](#instalación-de-un-compilador)
    - [***Instalación de Visual Studio Code***](#instalación-de-visual-studio-code)
  - [***Estructura Básica de un Programa en C***](#estructura-básica-de-un-programa-en-c)
  - [***Variables y Tipos de Datos***](#variables-y-tipos-de-datos)
    - [***Declaración y Asignación***](#declaración-y-asignación)
    - [***Tipos de Datos***](#tipos-de-datos)
  - [***Operadores***](#operadores)
    - [***Aritméticos***](#aritméticos)
    - [***Relacionales***](#relacionales)
    - [***Lógicos***](#lógicos)
  - [***Estructuras de Control***](#estructuras-de-control)
    - [***Condicionales***](#condicionales)
    - [***Bucles***](#bucles)
  - [***Funciones***](#funciones)
    - [***Declaración y Definición***](#declaración-y-definición)
  - [***Arreglos***](#arreglos)
    - [***Declaración y Uso***](#declaración-y-uso)
  - [***Punteros***](#punteros)
    - [***Declaración y Uso de Punteros***](#declaración-y-uso-de-punteros)
  - [***Estructuras***](#estructuras)
    - [***Declaración y Uso de Estructuras***](#declaración-y-uso-de-estructuras)
  - [***Entrada y Salida***](#entrada-y-salida)
    - [***Uso de `scanf` y `printf`***](#uso-de-scanf-y-printf)
  - [***Manejo de Memoria***](#manejo-de-memoria)
    - [***Uso de `malloc` y `free`***](#uso-de-malloc-y-free)
  - [***Ejemplos Prácticos***](#ejemplos-prácticos)
  - [***Recursos Adicionales***](#recursos-adicionales)
  - [***Contribuciones***](#contribuciones)
  - [***Licencia***](#licencia)

## ***Introducción***

- *C es un lenguaje de programación de propósito general, conocido por su eficiencia y control de bajo nivel. Es ampliamente utilizado en sistemas operativos, software embebido y aplicaciones de alto rendimiento.*

## ***Configuración del Entorno***

### ***Instalación de un Compilador***

1. **Windows:** *Instala [MinGW](https://code.visualstudio.com/docs/cpp/config-mingw "https://code.visualstudio.com/docs/cpp/config-mingw") o [TDM-GCC](https://jmeubank.github.io/tdm-gcc/ "https://jmeubank.github.io/tdm-gcc/").*
2. **macOS:** *Usa [Homebrew](https://brew.sh/ "https://brew.sh/") para instalar GCC: `brew install gcc`.*

    ```bash
    brew install gcc
    ```

3. **Linux:** *Instala GCC con el gestor de paquetes de tu distribución, por ejemplo: para distribuciones basadas en Debian Ubuntu `sudo apt-get install gcc`.*

    ```bash
    sudo apt-get install build-essential
    ```

### ***Instalación de Visual Studio Code***

1. **Descarga:** *Descarga e instala Visual Studio Code desde el [sitio web oficial](https://code.visualstudio.com/ "https://code.visualstudio.com/").*

    ```bash
    sudo snap install --classic code # or code-insiders
    ```

2. **Extensiones:** *Instala la extensión "C/C++" de Microsoft para soporte de lenguaje, depuración y más.*

## ***Estructura Básica de un Programa en C***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
#include <stdio.h>

int main(void) {
    printf("¡Hola, mundo!\n");
    return 0;
}
```

## ***Variables y Tipos de Datos***

### ***Declaración y Asignación***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int edad = 25;
float altura = 1.75;
char inicial = 'D';
```

### ***Tipos de Datos***

- **`int`:** *Entero*
- **`float`:** *Número de punto flotante*
- **`double`:** *Número de punto flotante de doble precisión*
- **`char`:** *Carácter*

## ***Operadores***

### ***Aritméticos***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int suma = 5 + 3;
int resta = 5 - 3;
int multiplicacion = 5 * 3;
int division = 5 / 3;
int modulo = 5 % 3;
```

### ***Relacionales***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int esIgual = (5 == 3);
int esDiferente = (5 != 3);
int esMayor = (5 > 3);
int esMenor = (5 < 3);
```

### ***Lógicos***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int y = (5 > 3) && (3 < 5);
int o = (5 > 3) || (3 > 5);
int no = !(5 > 3);
```

## ***Estructuras de Control***

### ***Condicionales***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
if (edad >= 18) {
    printf("Eres mayor de edad.\n");
} else {
    printf("Eres menor de edad.\n");
}
```

### ***Bucles***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
// Bucle for
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}

// Bucle while
int j = 0;
while (j < 10) {
    printf("%d\n", j);
    j++;
}
```

## ***Funciones***

### ***Declaración y Definición***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int sumar(int a, int b) {
    return a + b;
}

int main(void) {
    int resultado = sumar(5, 3);
    printf("Resultado: %d\n", resultado);
    return 0;
}
```

## ***Arreglos***

### ***Declaración y Uso***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int numeros[5] = {1, 2, 3, 4, 5};
printf("El primer número es %d\n", numeros[0]);
```

## ***Punteros***

### ***Declaración y Uso de Punteros***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int valor = 10;
int *ptr = &valor;
printf("El valor es %d\n", *ptr);
```

## ***Estructuras***

### ***Declaración y Uso de Estructuras***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
struct Persona {
    char nombre[50];
    int edad;
};

struct Persona persona1 = {"Daniel", 25};
printf("Nombre: %s, Edad: %d\n", persona1.nombre, persona1.edad);
```

## ***Entrada y Salida***

### ***Uso de `scanf` y `printf`***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int edad;
printf("Introduce tu edad: ");
scanf("%d", &edad);
printf("Tu edad es %d\n", edad);
```

## ***Manejo de Memoria***

### ***Uso de `malloc` y `free`***

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me
int *ptr = (int *)malloc(sizeof(int));
*ptr = 100;
printf("Valor: %d\n", *ptr);
free(ptr);
```

## ***Ejemplos Prácticos***

1. *[Lista dinamica]("")*
2. *[Lista Enlazada]("")*
3. *[Dictionarios]("")*

## ***Recursos Adicionales***

- *[Documentación de C](https://devdocs.io/c/ "https://devdocs.io/c/")*
- *[Tutorial de C](https://www.learn-c.org/ "https://www.learn-c.org/")*

## ***Contribuciones***

*¡Las contribuciones son bienvenidas! Si tienes sugerencias, correcciones o mejoras para esta guía, siéntete libre de abrir un problema o enviar una solicitud de extracción.*

## ***Licencia***

> *Este repositorio se publica bajo la Licencia MIT. Siéntete libre de utilizar, modificar y distribuir el contenido de acuerdo con los términos de esta licencia.*
