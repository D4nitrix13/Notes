<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```javascript
const dollars = ['32$', '15$', '12$', '17$', '20$'];

let prices = [];

for (let index = 0; index < dollars.length; index++) {
  prices[index] = Number(dollars[index].slice(0, dollars[index].length - 1));
}

console.log(prices); // [ 32, 15, 12, 17, 20 ]
```

---

## ***Explicación***

1. **Array de Dólares:** *`dollars` es un array que contiene cadenas con un signo `$` al final.*

2. **Iteración con `for`:** *Se utiliza un bucle `for` clásico para recorrer cada elemento del array `dollars`.*

3. **Conversión de Cadena a Número:** *Dentro del bucle, `Number(dollars[index].slice(0, dollars[index].length - 1))` se utiliza para eliminar el último carácter (`$`) de cada cadena y convertir la cadena resultante en un número.*

4. **Almacenamiento en `prices`:** *Los números convertidos se almacenan en el array `prices`.*

5. **Impresión del Resultado:** *Se imprime el array `prices`, que contiene los números enteros correspondientes a las cantidades de dólares sin el signo `$`.*

- *Este método es más manual y explícito en comparación con el uso de funciones modernas como `map` y funciones flecha, típicas de los enfoques más contemporáneos en JavaScript.*
