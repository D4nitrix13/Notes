<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion Ejemplo 01***

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

// Ejemplo de uso: Aplicar la función double al número 15.
console.log(apply(15, function double(num) {
  return 2 * num;
}));
```

---

## ***Conceptos Clave***

1. **Funciones Anónimas:** *Se pueden definir funciones directamente en el lugar donde se necesitan sin asignarles un nombre explícito.*

2. **Flexibilidad:** *Esto permite pasar funciones directamente como argumentos a otras funciones como en el ejemplo de `apply`.*

---

### ***Características***

- **Expresividad:** *Facilita la escritura de código conciso y directo al definir funciones en línea.*
- **Contextualidad:** *Útil cuando la función que se pasa como argumento es específica para un uso particular y no necesita ser reutilizada en otros contextos.*

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

- *Este ejemplo muestra cómo definir una función anónima directamente como argumento de `apply`, demostrando la versatilidad de JavaScript en el manejo de funciones.*
