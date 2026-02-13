// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20]

const expensive = []
let i = 0

for (let index = 0; index < prices.length; index++) {
  if (prices[index] >= 20) {
    expensive[i] = prices[index]
    i++
  }
}

console.log(expensive) // [ 32, 20 ]
