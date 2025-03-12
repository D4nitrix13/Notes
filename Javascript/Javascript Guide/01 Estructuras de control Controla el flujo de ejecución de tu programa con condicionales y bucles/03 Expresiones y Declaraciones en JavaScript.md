<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Expresiones y Declaraciones en JavaScript***

- *En JavaScript, existen dos tipos fundamentales de ele-mentos que forman el núcleo de la escritura de código: **expresiones** y **declaraciones**. Aunque estos términos pueden parecer confusos al principio, son esenciales para comprender cómo funciona JavaScript.*

---

## ***Declaraciones***

- *Las declaraciones en JavaScript son sentencias que definen la creación de una variable, función o clase. En otras palabras, las declaraciones son instrucciones que le damos a JavaScript para que realice una tarea específica.*

> *Nota: Las funciones y las clases se cubrirán más adelante en el curso.*

- *Por ejemplo, una declaración de variable es una sentencia que asigna un nombre y un valor a una variable. El siguiente código es un ejemplo de una declaración de variable:*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let nombre = "Daniel";
```

- *Este código por sí mismo no produce ningún valor que pueda ser usado directamente con el método `console.log`. Si intentas hacerlo, obtendrás un error:*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

console.log(let nombre = "Daniel"); // SyntaxError
```

---

### ***Expresiones***

- *Las expresiones en JavaScript son sentencias que producen un valor. Las expresiones pueden ser tan simples como un solo número o una cadena de texto, o tan complejas como el cálculo de una operación matemática, la evaluación de diferentes valores o la llamada a una función.*

**Por ejemplo, una expresión numérica es una sentencia que produce un número:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

2 + 3; // -> 5
```

- **De hecho, lo que guardamos en las variables son resultados de expresiones. Por ejemplo, en el siguiente código, la expresión `2 + 3` se evalúa y el resultado se guarda en la variable `resultado`:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let resultado = 2 + 3;
```

- *En este código, declaramos la variable `resultado` y le asignamos el valor de la expresión `2 + 3`.*

---

#### ***¿Por qué es importante la diferencia?***

- *La diferencia entre declaraciones y expresiones es crucial porque no podemos usar una declaración donde se espera una expresión y viceversa.*

- *Por ejemplo, en estructuras de control como `if` y `while`, se espera una expresión que se evalúe a un valor booleano. Por lo tanto, no podemos usar una declaración en su lugar:*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// ❌ Ambos códigos están mal y sirven para ilustrar que no debes usar declaraciones cuando se esperan expresiones

if (let nombre = "Daniel") { // ❌ SyntaxError
  console.log("Hola, Daniel");
}

while (let i = 0) { // ❌ SyntaxError
  console.log("Iteración");
  i = i + 1;
}
```

---

### ***Examen interactivo***

---

#### ***¿Qué son las declaraciones en JavaScript y para qué se utilizan?***

- **Las declaraciones en JavaScript son sentencias que definen la creación de una variable, función o clase para que puedan ser usadas posteriormente en el código.** *¡Eso es!*
- *Las declaraciones en JavaScript son sentencias que producen un valor. Se utilizan para calcular un valor y devolverlo en una expresión.*
- *Las declaraciones en JavaScript son sentencias que se utilizan para realizar operaciones matemáticas complejas.*

---

#### ***¿Qué son las expresiones en JavaScript y para qué se utilizan?***

- *Las expresiones en JavaScript son sentencias que definen la creación de una variable.*
- **Las expresiones en JavaScript son sentencias que producen un valor.** *¡Eso es!*
- *Las expresiones sólo se usan como condiciones de los condicionales `if` y los bucles.*

---

### ***Resumen***

- *Entender la diferencia entre expresiones y declaraciones en JavaScript es fundamental para escribir código correcto y eficiente. Las declaraciones son instrucciones que le damos a JavaScript para crear y definir variables, funciones y clases, mientras que las expresiones son sentencias que producen un valor y se utilizan para realizar cálculos y evaluaciones en el código.*

---

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/estructuras-de-control/expresiones-y-declaraciones "https://www.aprendejavascript.dev/clase/estructuras-de-control/expresiones-y-declaraciones")*
