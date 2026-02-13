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
const updatedPrices = []
const updatedPricesSumDiez = []

// Iterar sobre `prices` para crear `updatedPrices`
for (const iterator of prices) {
  // const obj = { price: iterator, currency: '$' }
  // updatedPrices.push(obj)
  updatedPrices.push({ price: iterator, currency: '$' })
}

// Iterar sobre `prices` para crear `updatedPricesSumDiez` con precios aumentados en 10 unidades
for (const iterator of prices) {
  // const obj = { price: iterator + 10, currency: '$' }
  // updatedPrices.push(obj)
  updatedPricesSumDiez.push({ price: iterator + 10, currency: '$' })
}

console.log(updatedPrices)
console.log(updatedPricesSumDiez)
```

---

## ***Explicación Mejorada***

1. **Array `prices`:** *`prices` es un array que contiene precios como números enteros.*

2. **Array `updatedPrices`:** *`updatedPrices` se inicializa como un array vacío donde se almacenarán los objetos `{ price: number, currency: string }` creados en el primer bucle `for`.*

3. **Bucle `for` para `updatedPrices`:**
   - *Utilizamos un bucle `for...of` para iterar sobre `prices`.*
   - *Creamos un objeto con la estructura `{ price: iterator, currency: '$' }` para cada elemento de `prices`.*
   - *Agregamos cada objeto creado a `updatedPrices` usando `updatedPrices.push()`.*

4. **Array `updatedPricesSumDiez`:** *`updatedPricesSumDiez` se inicializa como un array vacío donde se almacenarán los objetos `{ price: number, currency: string }` con precios aumentados en 10 unidades, creados en el segundo bucle `for`.*

5. **Bucle `for` para `updatedPricesSumDiez`:**
   - *Utilizamos otro bucle `for...of` para iterar sobre `prices` nuevamente.*
   - *Aumentamos el valor de cada precio en 10 unidades (`iterator + 10`) dentro de la definición del objeto.*
   - *Creamos un objeto con la estructura `{ price: iterator + 10, currency: '$' }` para cada elemento de `prices` con el precio modificado.*
   - *Agregamos cada objeto creado a `updatedPricesSumDiez` usando `updatedPricesSumDiez.push()`.*

6. **Impresión de Resultados:** *Imprimimos los arrays `updatedPrices` y `updatedPricesSumDiez` para verificar los resultados obtenidos después de los bucles `for`.*

- *Este código es claro y utiliza bucles `for...of` para demostrar cómo crear y modificar arrays de objetos de manera explícita y directa en JavaScript.*
