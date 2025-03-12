<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion Ejemplo 02***

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

// Ejemplo de uso: Aplicar una función anónima que duplica el número 15.
console.log(apply(15, function(num) {
  return 2 * num;
}));
```

---

## ***Conceptos Clave***

1. **Funciones Anónimas:** *Son funciones que no tienen un nombre explícito y se definen directamente en el lugar donde se necesitan.*

2. **Uso Contextual:** *Las funciones anónimas son útiles cuando la función es específica para un uso particular y no necesita ser referenciada en otras partes del código.*

---

### ***Características***

- **Flexibilidad:** *Permite definir funciones de manera directa y concisa en el momento de su uso.*
- **Ejemplo Específico:** *Ideal para situaciones donde la lógica de la función es simple y no justifica la definición de una función con nombre.*

---

### ***Ejemplo Práctico***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

function apply(num, f) {
  return f(num);
}

// Ejemplo de uso: Aplicar una función anónima que duplica el número 15.
console.log(apply(15, function(num) {
  return 2 * num;
}));
```

- *Este ejemplo ilustra cómo utilizar una función anónima para duplicar el número 15 usando la función `apply`. La función anónima se define en línea como un argumento de `apply`, demostrando la flexibilidad de JavaScript en la definición de funciones.*
