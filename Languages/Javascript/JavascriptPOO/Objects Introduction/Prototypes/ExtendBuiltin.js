// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Podemos extender la funcionalidad de los objetos integrados usando prototipos
String.prototype.padLeft = function (width, char = " ") {
  let result = this;
  /*
  En este contexto, this se refiere a la cadena de texto sobre la que se está invocando el método. Es decir, el valor de this es la cadena a la que le estamos agregando el relleno (por ejemplo, "hello").

  let result = this;: Esta línea inicializa una nueva variable llamada result y le asigna el valor de this, que es la cadena de texto original. Esto se hace porque más adelante, si es necesario agregar caracteres a la cadena, se modificará el valor de result y se retornará al final.
  */

  if (this.length < width) {
    result = new Array(width - this.length + 1).join(char) + this; // Agrega caracteres a la izquierda
  }

  /*
  if (this.length < width):

  this.length: this es la cadena sobre la que estamos trabajando, y this.length nos da la longitud de esa cadena. Por ejemplo, si this es "hello", entonces this.length sería 5.
  
  width: Este es el parámetro que le pasamos al método padLeft, y es el ancho deseado para la cadena resultante (por ejemplo, 12).
  
  Condición if: Si la longitud de la cadena es menor que el width deseado, se entra al bloque del if para agregar los caracteres necesarios a la izquierda de la cadena.

  result = new Array(width - this.length + 1).join(char) + this;:

  new Array(width - this.length + 1): Crea un nuevo arreglo con una longitud de width - this.length + 1. Esto se hace para calcular cuántos caracteres de relleno necesitamos agregar.
  
  Por ejemplo, si width es 12 y this.length es 5 (la longitud de "hello"), la longitud del arreglo será 12 - 5 + 1 = 8. Esto significa que necesitamos agregar 8 caracteres (de relleno).
  
  .join(char): join(char) convierte el arreglo en una cadena, uniendo los elementos del arreglo con el carácter char. El arreglo está vacío inicialmente, pero la cantidad de elementos en el arreglo es suficiente para generar una cadena con los caracteres de relleno.
  
  Si el carácter de relleno (char) es "x", entonces new Array(8).join("x") generaría una cadena "xxxxxxx".
  
  + this: Finalmente, se concatena la cadena original (this, que es "hello") al final de la cadena de relleno generada. Esto da como resultado una cadena de longitud width con el relleno añadido a la izquierda.

  Ejemplo: Si this es "hello", width es 12, y char es "x", después de esta línea result sería "xxxxxxxhello".
  */

  return result;
};

"hello".padLeft(12, "x"); // "xxxxxxxhello"

// Pero en JavaScript ya puedes usar padStart y padEnd
"hello".padEnd(12, "x"); // "helloxxxxxxx"
"hello".padStart(12, "x"); // "xxxxxxxhello"
