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
