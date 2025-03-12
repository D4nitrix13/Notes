// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

/**
 * Las funciones *map*, *filter* y *reduce* comparten la característica de recibir una función
 * como argumento, aplicando dicha función a cada elemento de la colección (array) y retornando
 * un nuevo valor basado en los resultados.
 *
 * Es crucial no usar paréntesis al pasar la función como argumento, ya que esto invocaría la
 * función inmediatamente en lugar de pasarla como una referencia.
 *
 * Ejemplo incorrecto:
 * apply(15, double()) // Error: La función se invoca inmediatamente y su resultado (undefined) se pasa a apply.
 *
 * Ejemplo correcto:
 * apply(15, double) // Correcto: La referencia a la función double se pasa a apply.
 */

/**
 * Aplica una función a un número y devuelve el resultado.
 *
 * @param {number} num - El número al que se aplicará la función.
 * @param {function} f - La función que se aplicará al número.
 * @returns {*} El resultado de aplicar la función al número.
 */
function apply(num, f) {
  return f(num)
}

/**
 * Duplica un número.
 *
 * @param {number} num - El número a duplicar.
 * @returns {number} El número duplicado.
 */
function double(num) {
  return 2 * num
}

// Ejemplo de uso de la función apply con la función double.
console.log(apply(15, double)) // 30
