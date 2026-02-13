// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$']

let sum = 0

// Implementación manual de map, filter y reduce
for (let index = 0; index < dollars.length; index++) {
  // Implementación de map (extracción y conversión del número)
  const price = Number(dollars[index].slice(0, dollars[index].length - 1))

  // Implementación de filter (condición de filtro)
  if (price >= 20) {
    // Implementación de reduce (acumulación de valores)
    sum += price
  }
}

console.log(sum) // Output: 52
