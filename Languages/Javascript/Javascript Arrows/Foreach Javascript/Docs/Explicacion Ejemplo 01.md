<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 01***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20]

let sum = 0
const expensivePrices = []

// Calcular la suma total de los precios y filtrar los precios caros
prices.forEach(price => {
  sum += price // Sumar cada precio a la variable `sum`

  if (price >= 20) {
    expensivePrices.push(price) // Agregar precios caros al array `expensivePrices`
  }
})

console.log('Suma total de precios:', sum)
console.log('Precios mayores o iguales a 20:', expensivePrices)
```

## ***Explicación***

1. **Array de Precios:** *`prices` es un array que contiene números enteros representando precios.*

2. **Variables:** *Se inicializa una variable `sum` para almacenar la suma total de los precios y un array `expensivePrices` para almacenar los precios que son mayores o iguales a 20.*

3. **Método `forEach`:** *`forEach` es utilizado para iterar sobre cada elemento del array `prices`.*

4. **Operaciones dentro de `forEach`:**
   - `sum += price`: Se suma cada `price` al valor actual de `sum`, acumulando así la suma total de todos los precios.
   - `if (price >= 20) { ... }`: Se verifica si el precio actual es mayor o igual a 20. Si lo es, se añade al array `expensivePrices` utilizando `push`.

5. **Impresión de Resultados:** *Finalmente, se imprime la suma total de los precios y los precios que son mayores o iguales a 20 utilizando `console.log`.*

- *Este ejemplo muestra cómo `forEach` puede utilizarse para realizar operaciones complejas sobre un array, como calcular sumas o aplicar filtros, sin necesidad de crear un nuevo array como lo harías con `map`.*
