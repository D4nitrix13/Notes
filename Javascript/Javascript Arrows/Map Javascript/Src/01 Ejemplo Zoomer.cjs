// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$']

const prices = []

for (const item of dollars) {
  prices.push(Number(item.slice(0, item.length - 1)))
}

console.log(prices) // [ 32, 15, 12, 17, 20 ]
