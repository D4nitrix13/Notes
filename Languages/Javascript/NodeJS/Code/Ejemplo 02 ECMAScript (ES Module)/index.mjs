// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// index.mjs
// Forma recomendada de utilizar módulos con ECMAScript Modules (ESM)

// Importación de funciones desde el módulo 'module.mjs'.
// Utilizamos la sintaxis de importación de ESM para traer las funciones necesarias.

import { multiplicacion, restar, suma } from './module.mjs'

// Uso de las funciones importadas
console.log('Suma (2 + 3):', suma(2, 3)) // Imprime el resultado de la suma de 2 y 3
console.log('Resta (2 - 3):', restar(2, 3)) // Imprime el resultado de la resta de 2 y 3
console.log('Multiplicación (2 * 3):', multiplicacion(2, 3)) // Imprime el resultado de la multiplicación de 2 y 3
