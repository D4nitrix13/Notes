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
