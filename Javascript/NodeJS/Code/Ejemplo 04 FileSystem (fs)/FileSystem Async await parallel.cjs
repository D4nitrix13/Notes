// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Fichero con extensión .cjs

// Importamos la función `readFile` del módulo 'fs/promises' de Node.js.
// Este módulo nos permite trabajar con el sistema de ficheros de manera asincrónica usando Promesas.
const { readFile } = require('node:fs/promises')

// Explicación de los conceptos:
// Asincrónico Secuencial: Operaciones asincrónicas que se ejecutan una tras otra, esperando a que cada una termine antes de empezar la siguiente.
// Asincrónico Paralelo: Operaciones asincrónicas que se ejecutan al mismo tiempo, sin esperar a que las demás terminen.
// Sincrónico: Operaciones que se ejecutan una tras otra de manera secuencial, bloqueando el flujo de ejecución hasta que cada una termine.

// Aquí utilizamos `Promise.all` para ejecutar las operaciones de lectura de ficheros de manera asincrónica en paralelo.
// Esto significa que ambas operaciones de lectura comenzarán al mismo tiempo, y el código no esperará a que termine la primera operación para comenzar la segunda.
Promise.all([
  readFile('./fichero.txt', 'utf-8'),
  readFile('./fichero2.txt', 'utf-8')
])
  // Cuando ambas promesas se resuelvan, entraremos en este bloque `.then`.
  // Desestructuramos el resultado en `text` y `secondText`, correspondientes a los contenidos de los dos ficheros.
  .then(([text, secondText]) => {
    console.log('Primer texto:', text) // Imprimimos el contenido del primer fichero.
    console.log('Segundo texto:', secondText) // Imprimimos el contenido del segundo fichero.
  })
  // Si alguna de las promesas falla, entramos en el bloque `.catch` para manejar el error.
  .catch((err) => {
    console.error('Error al leer los ficheros:', err) // Imprimimos el error en caso de que ocurra.
  })
