<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***C Syntax and Code Guide***

- *Welcome! This repository provides a comprehensive guide on C syntax and code, including practical examples. Here, you will learn the fundamentals of the C language and how to write efficient and well-structured programs.*

## ***Author***

- **Name:** **Daniel Benjamin Perez Morales**
- **GitHub:** *[D4nitrix13](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")*
- **Email:** *<danielperezdev@proton.me>*

## ***Table of Contents***

- [***C Syntax and Code Guide***](#c-syntax-and-code-guide)
  - [***Author***](#author)
  - [***Table of Contents***](#table-of-contents)
  - [***Introduction***](#introduction)
  - [***Environment Setup***](#environment-setup)
    - [***Installing a Compiler***](#installing-a-compiler)
    - [***Installing Visual Studio Code***](#installing-visual-studio-code)
  - [***Basic Structure of a C Program***](#basic-structure-of-a-c-program)
  - [***Variables and Data Types***](#variables-and-data-types)
    - [***Declaration and Assignment***](#declaration-and-assignment)
    - [***Data Types***](#data-types)
  - [***Operators***](#operators)
    - [***Arithmetic***](#arithmetic)
    - [***Relational***](#relational)
    - [***Logical***](#logical)
  - [***Control Structures***](#control-structures)
    - [***Conditionals***](#conditionals)
    - [***Loops***](#loops)
  - [***Functions***](#functions)
    - [***Declaration and Definition***](#declaration-and-definition)
  - [***Arrays***](#arrays)
    - [***Declaration and Use***](#declaration-and-use)
  - [***Pointers***](#pointers)
    - [***Declaration and Use of Pointers***](#declaration-and-use-of-pointers)
  - [***Structures***](#structures)
    - [***Declaration and Use of Structures***](#declaration-and-use-of-structures)
  - [***Input and Output***](#input-and-output)
    - [***Using `scanf` and `printf`***](#using-scanf-and-printf)
  - [***Memory Management***](#memory-management)
    - [***Using `malloc` and `free`***](#using-malloc-and-free)
  - [***Practical Examples***](#practical-examples)
  - [***Additional Resources***](#additional-resources)
  - [***Contributions***](#contributions)
  - [***License***](#license)

## ***Introduction***

- *C is a general-purpose programming language known for its efficiency and low-level control. It is widely used in operating systems, embedded software, and high-performance applications.*

## ***Environment Setup***

### ***Installing a Compiler***

1. **Windows:** *Install [MinGW](https://code.visualstudio.com/docs/cpp/config-mingw "https://code.visualstudio.com/docs/cpp/config-mingw") or [TDM-GCC](https://jmeubank.github.io/tdm-gcc/ "https://jmeubank.github.io/tdm-gcc/").*
2. **macOS:** *Use [Homebrew](https://brew.sh/ "https://brew.sh/") to install GCC: `brew install gcc`.*

    ```bash
    brew install gcc
    ```

3. **Linux:** *Install GCC with your distribution's package manager, for example, for Debian-based distributions like Ubuntu: `sudo apt-get install gcc`.*

    ```bash
    sudo apt-get install build-essential
    ```

### ***Installing Visual Studio Code***

1. **Download:** *Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/ "https://code.visualstudio.com/").*

    ```bash
    sudo snap install --classic code # or code-insiders
    ```

2. **Extensions:** *Install the "C/C++" extension by Microsoft for language support, debugging, and more.*

## ***Basic Structure of a C Program***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
    return 0;
}
```

## ***Variables and Data Types***

### ***Declaration and Assignment***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int age = 25;
float height = 1.75;
char initial = 'D';
```

### ***Data Types***

- **`int`:** *Integer*
- **`float`:** *Floating-point number*
- **`double`:** *Double precision floating-point number*
- **`char`:** *Character*

## ***Operators***

### ***Arithmetic***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int sum = 5 + 3;
int difference = 5 - 3;
int product = 5 * 3;
int quotient = 5 / 3;
int remainder = 5 % 3;
```

### ***Relational***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int isEqual = (5 == 3);
int isNotEqual = (5 != 3);
int isGreater = (5 > 3);
int isLesser = (5 < 3);
```

### ***Logical***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int andOp = (5 > 3) && (3 < 5);
int orOp = (5 > 3) || (3 > 5);
int notOp = !(5 > 3);
```

## ***Control Structures***

### ***Conditionals***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
if (age >= 18) {
    printf("You are an adult.\n");
} else {
    printf("You are a minor.\n");
}
```

### ***Loops***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
// For loop
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}

// While loop
int j = 0;
while (j < 10) {
    printf("%d\n", j);
    j++;
}
```

## ***Functions***

### ***Declaration and Definition***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int add(int a, int b) {
    return a + b;
}

int main(void) {
    int result = add(5, 3);
    printf("Result: %d\n", result);
    return 0;
}
```

## ***Arrays***

### ***Declaration and Use***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int numbers[5] = {1, 2, 3, 4, 5};
printf("The first number is %d\n", numbers[0]);
```

## ***Pointers***

### ***Declaration and Use of Pointers***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int value = 10;
int *ptr = &value;
printf("The value is %d\n", *ptr);
```

## ***Structures***

### ***Declaration and Use of Structures***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
struct Person {
    char name[50];
    int age;
};

struct Person person1 = {"Daniel", 25};
printf("Name: %s, Age: %d\n", person1.name, person1.age);
```

## ***Input and Output***

### ***Using `scanf` and `printf`***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int age;
printf("Enter your age: ");
scanf("%d", &age);
printf("Your age is %d\n", age);
```

## ***Memory Management***

### ***Using `malloc` and `free`***

```c
// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me
int *ptr = (int *)malloc(sizeof

(int));
*ptr = 100;
printf("Value: %d\n", *ptr);
free(ptr);
```

## ***Practical Examples***

1. *[Dynamic List]("")*
2. *[Linked List]("")*
3. *[Dictionaries]("")*

## ***Additional Resources***

- *[C Documentation](https://devdocs.io/c/ "https://devdocs.io/c/")*
- *[C Tutorial](https://www.learn-c.org/ "https://www.learn-c.org/")*

## ***Contributions***

*Contributions are welcome! If you have suggestions, corrections, or improvements for this guide, feel free to open an issue or submit a pull request.*

## ***License***

> *This repository is published under the MIT License. Feel free to use, modify, and distribute the content according to the terms of this license.*
