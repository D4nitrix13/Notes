<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

---

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20];

// Utiliza reduce para sumar todos los elementos del array `expensive`.
// El segundo argumento de `reduce`, `0`, es el valor inicial del acumulador `acum`.
const sum = expensive.reduce((acum, price) => acum + price, 0);

console.log(sum); // 52
```

---

## ***Explicación Mejorada***

1. **Array de Números:** *`expensive` es un array que contiene los números `[32, 20]`, que representan precios.*

2. **Método `reduce`:** *`reduce` es un método de los arrays en JavaScript que ejecuta una función reductora (función callback) sobre cada elemento del array, devolviendo un único valor como resultado.*

3. **Función Flecha en `reduce`:** *`(acum, price) => acum + price` es la función reductora utilizada en `reduce`. `acum` es el acumulador que mantiene el resultado parcial de la operación de reducción, y `price` es el valor actual del elemento siendo procesado. En cada iteración, `acum` se actualiza sumando el valor actual de `price` al valor actual de `acum`.*

4. **Valor Inicial (`0`):** *El segundo argumento de `reduce`, `0`, es el valor inicial del acumulador `acum`. En la primera iteración de `reduce`, `acum` se inicializa con este valor (`0`). Esto es útil cuando necesitas iniciar el acumulador con un valor específico antes de procesar los elementos del array.*

5. **Resultado Final:** *Después de completar todas las iteraciones del array `expensive`, `reduce` devuelve el valor final del acumulador `acum`, que es la suma total de todos los elementos del array.*

6. **Impresión del Resultado:** *Se imprime `sum`, que es `52`, la suma total de los elementos `[32, 20]`.*

---

### ***Significado de `0` como Segundo Argumento***

- *El `0` como segundo argumento de `reduce` es el valor inicial del acumulador `acum`. Esto significa que en la primera iteración de `reduce`, `acum` se inicializa con `0`. Si omites este argumento, `reduce` utilizará el primer elemento del array como valor inicial de `acum`.*

---

### ***Modificación del Valor Inicial***

- *Si cambias el valor inicial de `reduce` a otro número, por ejemplo `10`, el acumulador `acum` comenzará con ese valor en la primera iteración. Por lo tanto, el resultado final de `reduce` será la suma total de todos los elementos del array `expensive`, comenzando desde `10` y sumando todos los elementos.*

- *Este código demuestra cómo usar `reduce` de manera efectiva para realizar operaciones de reducción en arrays, en este caso, sumando los elementos del array `expensive`.*
