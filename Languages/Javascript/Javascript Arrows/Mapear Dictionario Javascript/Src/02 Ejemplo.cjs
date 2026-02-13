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
