<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 01***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20];
let sum = 0;

// Itera sobre cada elemento del array `expensive` utilizando un bucle `for...of`.
for (const iterator of expensive) {
  // Suma cada elemento `iterator` al acumulador `sum`.
  sum += iterator;
}

console.log(sum); // 52
```

---

## ***Explicación Mejorada***

1. **Array de Números:** *`expensive` es un array que contiene los números `[32, 20]`, que representan precios.*

2. **Bucle `for...of`:** *Se utiliza un bucle `for...of` para iterar sobre cada elemento del array `expensive`. En cada iteración, `iterator` toma el valor del elemento actual del array.*

3. **Acumulador `sum`:** *`sum` es una variable que se inicializa en `0` y se utiliza para acumular la suma de los elementos del array.*

4. **Suma de Elementos:** *Dentro del bucle `for...of`, `sum += iterator` suma el valor del elemento actual (`iterator`) al acumulador `sum`.*

5. **Resultado Final:** *Después de completar todas las iteraciones del bucle `for...of`, `sum` contiene la suma total de todos los elementos del array `expensive`, que es `52`.*

6. **Impresión del Resultado:** *Finalmente, se imprime `sum`, que es `52`, la suma total de los elementos `[32, 20]`.*

- *Este código utiliza un enfoque moderno y conciso con el bucle `for...of` para calcular la suma de los elementos en el array `expensive`, manteniendo la estructura original proporcionada.*
