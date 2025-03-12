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
