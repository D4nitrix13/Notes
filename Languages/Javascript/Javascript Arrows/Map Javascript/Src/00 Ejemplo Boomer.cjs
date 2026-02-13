// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$']

const prices = []

for (let index = 0; index < dollars.length; index++) {
  prices[index] = Number(dollars[index].slice(0, dollars[index].length - 1))
}

console.log(prices) // [ 32, 15, 12, 17, 20 ]
