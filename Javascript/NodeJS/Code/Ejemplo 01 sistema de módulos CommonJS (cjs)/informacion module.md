# Fichero `module.cjs`

```javascript
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
    return a + b;
}

function restar(a, b) {
    return a - b;
}

function multiplicacion(a, b) {
    return a * b;
}

// Exportación de las funciones definidas
// Método recomendado: Exportar múltiples funciones en un solo objeto
module.exports = {
    suma,
    restar,
    multiplicacion
};

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
```

## ***Explicación Detallada***

1. **Definición de Funciones:**
   - *`suma(a, b)`: Devuelve la suma de `a` y `b`.*
   - *`restar(a, b)`: Devuelve la resta de `b` desde `a`.*
   - *`multiplicacion(a, b)`: Devuelve el producto de `a` y `b`.*

2. **Exportación de Módulos:**
   - *La exportación de un solo valor o función (`module.exports = suma`) no es recomendada porque limita la reutilización del módulo.*
   - *Exportar un objeto que contiene funciones nombradas (`module.exports = { suma: function suma(a, b) { ... }, ... }`) es más flexible.*
   - *La forma más recomendada es usar la sintaxis abreviada de ES6 (`module.exports = { suma, restar, multiplicacion }`), que es más concisa y clara.*

### ***Beneficios del Patrón de Diseño de Módulos***

- ***Organización del Código:** Separa las funcionalidades en diferentes ficheros, lo que facilita la lectura y el mantenimiento.*
- ***Reutilización del Código:** Permite importar y reutilizar funciones en diferentes partes de la aplicación.*
- ***Encapsulamiento:** Mantiene las dependencias y el código relacionados juntos, reduciendo el riesgo de conflictos de nombres y mejorando la modularidad del código.*

*Este formato proporciona una mejor organización, explicación y claridad sobre cómo funcionan los módulos y las diferentes formas de exportarlos en `Node.js`.*
