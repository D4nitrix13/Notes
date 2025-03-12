<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20];

const expensive = [];
let i = 0;

for (let index = 0; index < prices.length; index++) {
  if (prices[index] >= 20) {
    expensive[i] = prices[index];
    i++;
  }
}

console.log(expensive); // [ 32, 20 ]
```

---

## ***Explicación***

1. **Array de Precios:** *`prices` es un array que contiene números enteros representando precios.*

2. **Array Resultante `expensive`:** *`expensive` es un array vacío inicialmente, que se llenará con los precios que cumplan con la condición especificada.*

3. **Bucle `for`:** *Se utiliza un bucle `for` clásico para recorrer cada elemento del array `prices`.*

4. **Condición `if`:** *Dentro del bucle, se evalúa si el precio en la posición actual (`prices[index]`) es mayor o igual a `20`.*

5. **Almacenamiento en `expensive`:** *Si la condición se cumple, se añade el precio al array `expensive` en la posición `i` y luego se incrementa `i`.*

6. **Impresión del Resultado:** *Se imprime el array `expensive`, que contiene los precios que son mayores o iguales a `20`.*

- *Este método es más manual y explícito en comparación con el uso de métodos modernos de arrays como `filter`, típicos de los enfoques más contemporáneos en JavaScript.*
