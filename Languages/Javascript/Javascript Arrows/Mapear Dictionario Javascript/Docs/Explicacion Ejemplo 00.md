<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20]
const updatedPrices = []
const updatedPricesSumDiez = []

// Recorremos el array `prices` con un bucle `for` clásico para crear `updatedPrices`
for (let index = 0; index < prices.length; index++) {
  // const obj = { price: prices[index], currency: '$' }
  // updatedPrices.push(obj)
  // Creamos un objeto con la estructura { price: number, currency: string } y lo agregamos a `updatedPrices`
  updatedPrices.push({ price: prices[index], currency: '$' })
}

// Recorremos el array `prices` nuevamente con un bucle `for` clásico para crear `updatedPricesSumDiez`
for (let index = 0; index < prices.length; index++) {
  // const obj = { price: prices[index] += 10, currency: '$' }
  // updatedPrices.push(obj)

  // Aumentamos el precio en 10 unidades y creamos un objeto con la estructura { price: number, currency: string } para `updatedPricesSumDiez`
  updatedPricesSumDiez.push({ price: prices[index] + 10, currency: '$' })
}

console.log(updatedPrices) // [{ price: 32, currency: '$' }, { price: 15, currency: '$' }, { price: 12, currency: '$' }, { price: 17, currency: '$' }, { price: 20, currency: '$' }]
console.log(updatedPricesSumDiez) // [{ price: 42, currency: '$' }, { price: 25, currency: '$' }, { price: 22, currency: '$' }, { price: 27, currency: '$' }, { price: 30, currency: '$' }]
```

---

## ***Explicación Mejorada***

1. **Array `prices`:** *`prices` es un array que contiene precios como números enteros.*

2. **Array `updatedPrices`:** *`updatedPrices` se inicializa como un array vacío donde se almacenarán los objetos `{ price: number, currency: string }` creados en el primer bucle `for`.*

3. **Bucle `for` para `updatedPrices`:**
   - *Utilizamos un bucle `for` clásico para iterar sobre `prices`.*
   - *Creamos un objeto con la estructura `{ price: prices[index], currency: '$' }` para cada elemento de `prices`.*
   - *Agregamos cada objeto creado a `updatedPrices` usando `updatedPrices.push()`.*

4. **Array `updatedPricesSumDiez`:** *`updatedPricesSumDiez` se inicializa como un array vacío donde se almacenarán los objetos `{ price: number, currency: string }` con precios aumentados en 10 unidades, creados en el segundo bucle `for`.*

5. **Bucle `for` para `updatedPricesSumDiez`:**
   - *Utilizamos otro bucle `for` clásico para iterar sobre `prices` nuevamente.*
   - *Aumentamos el valor de cada precio en 10 unidades (`prices[index] + 10`) dentro de la definición del objeto.*
   - *Creamos un objeto con la estructura `{ price: prices[index] + 10, currency: '$' }` para cada elemento de `prices` con el precio modificado.*
   - *Agregamos cada objeto creado a `updatedPricesSumDiez` usando `updatedPricesSumDiez.push()`.*

6. **Impresión de Resultados:** *Imprimimos los arrays `updatedPrices` y `updatedPricesSumDiez` para verificar los resultados obtenidos después de los bucles `for`.*

- *Este código es claro y utiliza bucles `for` clásicos para demostrar cómo crear y modificar arrays de objetos de manera explícita y directa en JavaScript.*
