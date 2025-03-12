// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// index.cjs
// Este fichero utiliza el sistema de módulos CommonJS (cjs) para importar y utilizar módulos.

// Importación de funciones desde el módulo 'module.cjs'.
// La variable que contiene las funciones importadas puede tener cualquier nombre,
// pero es recomendable utilizar un nombre descriptivo relacionado con el módulo.

const { suma, restar, multiplicacion } = require('./module.cjs')

// Uso de las funciones importadas
console.log('Suma (2 + 3):', suma(2, 3)) // Imprime el resultado de la suma de 2 y 3
console.log('Resta (2 - 3):', restar(2, 3)) // Imprime el resultado de la resta de 2 y 3
console.log('Multiplicación (2 * 3):', multiplicacion(2, 3)) // Imprime el resultado de la multiplicación de 2 y 3

// Notas sobre los sistemas de módulos en Node.js:
// - Los ficheros con extensión .js usan por defecto el sistema de módulos CommonJS.
// - Los ficheros con extensión .mjs usan el sistema de módulos ECMAScript (ES Module).
// - Los ficheros con extensión .cjs usan explícitamente el sistema de módulos CommonJS.
