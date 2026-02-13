// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Ejemplo básico de uso de `console` en Node.js

// Imprime un saludo en la consola
console.log('Saludo')

// Imprime un mensaje informativo en la consola
console.info('Mensaje')

// Imprime un mensaje de error en la consola
console.error('Mensaje Error')

// Intento de acceder al objeto `window`, que no está definido en Node.js
// Esto causará un error porque `window` es específico de los navegadores web
// Node.js utiliza `global` o `globalThis` en lugar de `window`

/*
El siguiente bloque de código está comentado porque causará un error si se ejecuta:
    ReferenceError: window is not defined
Esto sucede porque `window` es un objeto global en el entorno del navegador, pero no en Node.js.
*/

// console.log(window)

// Para demostrar que `window` no está definido en Node.js, imprimimos su tipo
// Debería ser 'undefined'
console.log(typeof window) // 'undefined'

// `globalThis` es una variable global que se refiere al contexto global en cualquier entorno

/*
En el navegador, `globalThis` apunta a `window`.
En Node.js, `globalThis` apunta a `global`.
De hecho, `console.log()` es una propiedad de `globalThis`.
*/

// Imprime el objeto `globalThis`, mostrando todas las propiedades globales disponibles en Node.js
globalThis.console.log(globalThis)
