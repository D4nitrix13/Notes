<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 01***

```javascript
const dollars = ['32$', '15$', '12$', '17$', '20$'];

let prices = [];

for (const item of dollars) {
  prices.push(Number(item.slice(0, item.length - 1)));
}

console.log(prices); // [ 32, 15, 12, 17, 20 ]
```

---

## ***Explicación***

1. **Array de Dólares:** *`dollars` es un array que contiene cadenas con un signo `$` al final.*

2. **Iteración con `for...of`:** *Se utiliza un bucle `for...of`, que es una característica moderna de JavaScript que simplifica la iteración sobre elementos de un array.*

3. **Conversión de Cadena a Número:** *Dentro del bucle, `Number(item.slice(0, item.length - 1))` se utiliza para eliminar el último carácter (`$`) de cada cadena y convertir la cadena resultante en un número.*

4. **Almacenamiento en `prices`:** *Los números convertidos se añaden al array `prices` utilizando el método `push`.*

5. **Impresión del Resultado:** *Se imprime el array `prices`, que contiene los números enteros correspondientes a las cantidades de dólares sin el signo `$`.*

- *Este enfoque es más conciso y utiliza características modernas de JavaScript como `for...of` y métodos de arrays como `push`, haciendo el código más legible y fácil de entender.*
