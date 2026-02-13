// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20]
let sum = 0

// Itera sobre cada elemento del array `expensive` utilizando un bucle `for...of`.
for (const iterator of expensive) {
  // Suma cada elemento `iterator` al acumulador `sum`.
  sum += iterator
}

console.log(sum) // 52
