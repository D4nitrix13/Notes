<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Bucles con do while en JavaScript***

- *El bucle `do while` es una estructura de control que se ejecuta al menos una vez y luego se repite mientras se cumpla una condición. Aunque no es tan común como otros tipos de bucles, es importante conocerlo y entender cómo funciona.*

---

## ***Sintaxis***

**La sintaxis del bucle `do while` es la siguiente:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

do {
  // código que se ejecuta al menos una vez
} while (condición);
```

- *En este bucle, el código dentro del bloque `do` se ejecuta una vez antes de que se evalúe la condición en el `while`. Si la condición es `true`, el bucle se repetirá; de lo contrario, se detendrá.*

---

### ***Ejemplo práctico: confirm***

- *Vamos a utilizar la función integrada `confirm` en JavaScript para crear un ejemplo práctico con el bucle `do while`. La función `confirm` muestra un cuadro de diálogo con dos botones: "Aceptar" y "Cancelar". Si el usuario pulsa "Aceptar", la función devuelve `true`. Si pulsa "Cancelar", devuelve `false`.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

confirm("¿Te gusta JavaScript?");
```

- *Llamar a la función `confirm` produce un valor que podemos guardar en una variable.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let respuesta = confirm("¿Te gusta JavaScript?");
console.log(respuesta); // -> true o false
```

---

#### ***Usando do while***

- *Vamos a hacer un programa que saldrá de un bucle `do while` cuando el usuario pulse "Cancelar" en el cuadro de diálogo que muestra la función `confirm`.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let respuesta;

do {
  respuesta = confirm("¿Te gusta JavaScript?");
} while (respuesta);
```

> *¿Por qué hay que poner la variable `respuesta` fuera? Porque si no, no podría ser usada en la condición del bucle. Esto muestra la importancia del ámbito de las variables.*

- *Si el usuario pulsa "Aceptar", la variable `respuesta` valdrá `true` y el bucle se repetirá. Si el usuario pulsa "Cancelar", la variable `respuesta` valdrá `false` y el bucle se detendrá.*

---

### ***Examen interactivo***

---

#### ***¿Cuántas veces como mínimo se ejecutará el código dentro de un bucle `do { ... } while`?***

- *Ninguna vez*
- *Depende de la condición*
- **Una vez** *(Correcta)*

*Este tipo de bucle se ejecutará siempre al menos una vez, sin importar la condición.*

---

### ***Resumen***

- *El bucle `do while` es útil cuando necesitas asegurar que un bloque de código se ejecute al menos una vez antes de que se evalúe la condición. Usando funciones como `confirm`, podemos crear bucles interactivos que respondan a las acciones del usuario.*

---

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/estructuras-de-control/bucles-con-do-while "https://www.aprendejavascript.dev/clase/estructuras-de-control/bucles-con-do-while")*
