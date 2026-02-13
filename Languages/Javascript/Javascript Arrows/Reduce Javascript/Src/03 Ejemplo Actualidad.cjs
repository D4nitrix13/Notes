// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20]

// Utiliza reduce para sumar todos los elementos del array `expensive`.
// El segundo argumento de `reduce`, `0`, es el valor inicial del acumulador `acum`.
const sum = expensive.reduce((acum, price) => acum + price, 0)

console.log(sum) // 52
