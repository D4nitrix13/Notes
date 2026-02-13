// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// module.cjs
// Patrón de diseño de módulos en Node.js
/*
Este patrón de diseño permite separar nuestro código en diferentes ficheros,
lo que facilita la importación y exportación de funcionalidades para reutilizar el código.
*/

// Definición de funciones
function suma(a, b) {
  return a + b
}

function restar(a, b) {
  return a - b
}

function multiplicacion(a, b) {
  return a * b
}

// Exportación de las funciones definidas
// Método recomendado: Exportar múltiples funciones en un solo objeto
module.exports = {
  suma,
  restar,
  multiplicacion
}

/*
Métodos de exportación:

1. Primer método (no recomendado):
   Este método permite exportar solo una función o un valor,
   lo que limita la capacidad de reutilización del módulo.

   module.exports = suma;

2. Segundo método:
   Se exporta un objeto que contiene funciones nombradas, lo que es más flexible
   y permite importar múltiples funciones desde un único módulo.

   module.exports = {
       suma: function suma(a, b) {
           return a + b;
       },
       restar: function restar(a, b) {
           return a - b;
       },
       multiplicacion: function multiplicacion(a, b) {
           return a * b;
       }
   };

3. Método recomendado (último método):
   Exportar directamente las referencias de las funciones utilizando la sintaxis abreviada de ES6,
   que es más concisa y clara.

   module.exports = {
       suma,
       restar,
       multiplicacion
   };
*/
