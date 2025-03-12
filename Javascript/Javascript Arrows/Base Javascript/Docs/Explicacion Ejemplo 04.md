<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion Ejemplo 04***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

/**
 * Función que aplica una función dada a un número y devuelve el resultado.
 *
 * @param {number} num - El número al que se aplicará la función.
 * @param {function} f - La función que se aplicará al número.
 * @returns {*} El resultado de aplicar la función al número.
 */
function apply(num, f) {
  return f(num);
}

// Ejemplo de uso: Aplicar una arrow function de una línea que duplica el número 15.
console.log(apply(15, (num) => 2 * num));
```

---

## ***Conceptos Clave***

1. **Arrow Functions de una Línea:** *Las arrow functions permiten una sintaxis aún más compacta cuando la función consiste en una sola expresión.*

2. **Simplicidad y Claridad:** *Las arrow functions de una línea son ideales para funciones simples y de operaciones matemáticas como en el ejemplo de duplicar un número.*

---

### ***Características***

- **Sintaxis Concisa:** *Elimina la necesidad de `{}` y `return` explícito para expresiones simples, mejorando la legibilidad y reduciendo el código.*

---

### ***Ejemplo Práctico***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

function apply(num, f) {
  return f(num);
}

// Ejemplo de uso: Aplicar una arrow function de una línea que duplica el número 15.
console.log(apply(15, (num) => 2 * num));
```

- *Este ejemplo demuestra cómo aplicar una arrow function de una línea como argumento de la función `apply`, realizando la operación de duplicar el número 15 de manera clara y concisa. Las arrow functions de una línea son una característica poderosa de JavaScript para simplificar la escritura de funciones cortas y directas.*
