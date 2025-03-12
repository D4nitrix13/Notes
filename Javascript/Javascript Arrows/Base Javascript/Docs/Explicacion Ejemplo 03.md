<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion Ejemplo 03***

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

// Ejemplo de uso: Aplicar una arrow function que duplica el número 15.
console.log(apply(15, (num) => {
  return 2 * num;
}));
```

---

## ***Conceptos Clave***

1. **Arrow Functions:** *Las arrow functions son una forma más concisa de escribir funciones en JavaScript, especialmente útiles para funciones anónimas.*

2. **Sintaxis Compacta:** *La sintaxis de arrow functions permite reducir la cantidad de código necesario en comparación con funciones tradicionales.*

---

### ***Características***

- **Simplicidad:** *Las arrow functions son ideales para funciones simples y de una sola línea como en el ejemplo de duplicar un número.*
- **Legibilidad Mejorada:** *Facilitan la lectura y comprensión del código al eliminar la necesidad de la palabra clave `function` y el uso de `{}` en casos simples.*

---

### ***Ejemplo Práctico***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

function apply(num, f) {
  return f(num);
}

// Ejemplo de uso: Aplicar una arrow function que duplica el número 15.
console.log(apply(15, (num) => {
  return 2 * num;
}));
```

- *Este ejemplo muestra cómo utilizar una arrow function como argumento de la función `apply`, aplicando la función directamente al número 15 para duplicarlo. Las arrow functions son especialmente útiles en contextos donde se necesita una función corta y concisa.*
