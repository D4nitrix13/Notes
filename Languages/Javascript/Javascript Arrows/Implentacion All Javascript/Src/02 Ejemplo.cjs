// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$']

let sum = 0

// Implementación de funciones en cadena linealmente
// sum = dollars.map(dollar => Number(dollar.slice(0, dollar.length - 1))).filter(dollar => dollar >= 20).reduce((acum, price) => acum + price, 0)

// Implementación de funciones en cadena de múltiples líneas
sum = dollars
  .map(dollar => Number(dollar.slice(0, dollar.length - 1)))
  .filter(dollar => dollar >= 20)
  .reduce((acum, price) => acum + price, 0)

console.log(sum) // Output: 52
