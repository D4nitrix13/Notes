// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

/**
 * Función que aplica una función dada a un número y devuelve el resultado.
 *
 * @param {number} num - El número al que se aplicará la función.
 * @param {function} f - La función que se aplicará al número.
 * @returns {*} El resultado de aplicar la función al número.
 */
function apply(num, f) {
  return f(num)
}

// Ejemplo de uso: Aplicar una arrow function de una línea que duplica el número 15.
console.log(apply(15, (num) => 2 * num))
