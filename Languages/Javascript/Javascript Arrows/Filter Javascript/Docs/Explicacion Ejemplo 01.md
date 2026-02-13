<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 01***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20];

// Usar un bucle for...of con una condición para filtrar los precios
const expensive = [];
for (const price of prices) {
  if (price >= 20) {
    expensive.push(price);
  }
}

console.log(expensive); // [ 32, 20 ]
```

---

## ***Explicación***

1. **Array de Precios:** *`prices` es un array que contiene números enteros representando precios.*

2. **Array Resultante `expensive`:** *`expensive` es un array vacío inicialmente, que se llenará con los precios que cumplan con la condición especificada.*

3. **Bucle `for...of`:** *Se utiliza un bucle `for...of`, que es una característica moderna de JavaScript que simplifica la iteración sobre elementos de un array.*

4. **Condición `if`:** *Dentro del bucle, se evalúa si el precio (`price`) actual es mayor o igual a `20`.*

5. **Método `push`:** *Si la condición se cumple, se añade el precio al array `expensive` utilizando el método `push`.*

6. **Impresión del Resultado:** *Se imprime el array `expensive`, que contiene los precios que son mayores o iguales a `20`.*

- *Este enfoque es más conciso y utiliza características modernas de JavaScript como `for...of` y métodos de arrays como `push`, haciendo el código más legible y fácil de entender en comparación con los enfoques más tradicionales.*
