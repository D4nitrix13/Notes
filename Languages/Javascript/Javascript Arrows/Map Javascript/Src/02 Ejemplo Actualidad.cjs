// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$']

let prices = []

// Usar map con una arrow function para convertir las cadenas de dólares a números
prices = dollars.map(dollar => Number(dollar.slice(0, dollar.length - 1)))

console.log(prices) // [ 32, 15, 12, 17, 20 ]
