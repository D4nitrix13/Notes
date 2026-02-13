// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20]

// Usar un bucle for...of con una condición para filtrar los precios
const expensive = []
for (const price of prices) {
  if (price >= 20) {
    expensive.push(price)
  }
}

console.log(expensive) // [ 32, 20 ]
