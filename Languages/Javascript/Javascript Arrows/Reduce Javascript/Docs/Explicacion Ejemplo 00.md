<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20];
let sum = 0;

// Itera sobre el array `expensive` y suma todos los elementos.
for (let index = 0; index < expensive.length; index++) {
  sum += expensive[index];
}

console.log(sum); // 52
```

---

## ***Explicación***

1. **Array de Números:** *`expensive` es un array que contiene los números `[32, 20]`, que representan precios.*

2. **Bucle `for`:** *Se utiliza un bucle `for` para iterar sobre cada elemento del array `expensive`.*

3. **Acumulador `sum`:** *`sum` es una variable que se inicializa en `0` y se utiliza para acumular la suma de los elementos del array.*

4. **Iteración:** *El bucle `for` recorre cada elemento del array `expensive` utilizando `index` como índice de posición.*

5. **Suma de Elementos:** *En cada iteración del bucle, `sum += expensive[index]` suma el valor del elemento actual (`expensive[index]`) al acumulador `sum`.*

6. **Resultado Final:** *Después de completar todas las iteraciones del bucle `for`, `sum` contiene la suma total de todos los elementos del array `expensive`.*

7. **Impresión del Resultado:** *Finalmente, se imprime `sum`, que es `52`, la suma total de los elementos `[32, 20]`.*

- *Este código sigue el enfoque tradicional utilizando un bucle `for` para sumar los elementos del array `expensive`, sin cambiar la estructura original proporcionada.*
