// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// * Caso 1: Función Flecha sin Paréntesis

const prices = [32, 15, 12, 17, 20]

/**
 * Filtra los precios que son mayores o iguales a 20.
 * Utiliza el método `filter` de arrays para crear un nuevo array con los precios filtrados.
 *
 * @param {number} dollar - El precio a evaluar.
 * @returns {boolean} `true` si el precio es mayor o igual a 20, `false` si no lo es.
 */
const expensive = prices.filter(dollar => {
  // Devuelve `true` si el precio es mayor o igual a 20, `false` si no lo es.
  if (dollar >= 20) {
    return true
  } else {
    return false
  }
})

console.log('Sin paréntesis:', expensive) // [ 32, 20 ]

// * Caso 2: Función Flecha con Paréntesis

// const prices = [32, 15, 12, 17, 20];

// /**
//  * Filtra los precios que son mayores o iguales a 20.
//  * Utiliza el método `filter` de arrays para crear un nuevo array con los precios filtrados.
//  *
//  * @param {number} dollar - El precio a evaluar.
//  * @returns {boolean} `true` si el precio es mayor o igual a 20, `false` si no lo es.
//  */
// const expensive = prices.filter((dollar) => {
//   // Devuelve `true` si el precio es mayor o igual a 20, `false` si no lo es.
//   if (dollar >= 20) {
//     return true;
//   } else {
//     return false;
//   }
// });

// console.log("Con paréntesis:", expensive); // [ 32, 20 ]
