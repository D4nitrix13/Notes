<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20]

// Mapear cada precio a un objeto con la estructura { price: number, currency: string }
console.log(prices.map(price => ({ price, currency: '$' })))
/*
[
  { price: 32, currency: '$' },
  { price: 15, currency: '$' },
  { price: 12, currency: '$' },
  { price: 17, currency: '$' },
  { price: 20, currency: '$' }
] */

// Sumar 10 a cada precio y mapearlo a un nuevo array de objetos actualizados
const updatedPrices = prices.map(price => ({ price: price + 10, currency: '$' }))

console.log(updatedPrices)

```

---

## ***Explicación Mejorada***

1. **Array `prices`:** *`prices` es un array que contiene precios como números enteros.*

2. **Mapeo a un objeto `{ price, currency }`:**
   - *Utilizamos `prices.map()` para iterar sobre cada elemento `price` en el array `prices`.*
   - *Para cada `price`, creamos un objeto `{ price, currency: '$' }` usando una función flecha.*
   - *El resultado es un nuevo array de objetos donde cada objeto tiene la estructura `{ price: number, currency: string }`.*

3. **Impresión del primer mapeo:**
   - *Imprimimos el resultado del primer `map()` usando `console.log()` para mostrar cómo se transforman los precios en objetos con su respectiva moneda.*

4. **Mapeo y actualización de precios:**
   - *Utilizamos `prices.map()` nuevamente para iterar sobre cada `price`.*
   - *Esta vez, dentro de la función flecha, sumamos `10` a cada `price` antes de crear el objeto `{ price: price + 10, currency: '$' }`.*
   - *El resultado es un nuevo array `updatedPrices` donde cada precio ha sido aumentado en `10` unidades y tiene la misma estructura `{ price: number, currency: string }`.*

5. **Impresión del segundo mapeo:**
   - *Imprimimos el array `updatedPrices` usando `console.log()` para verificar los precios actualizados después de sumar `10` a cada uno.*

- *Este código demuestra cómo utilizar el método `map()` en JavaScript para transformar y actualizar elementos de un array de manera clara y eficiente, manteniendo la estructura y añadiendo comentarios que clarifican cada paso del proceso.*
