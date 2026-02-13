// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs')

console.log('Leyendo el primer fichero...')

// Operación asíncrona para leer el contenido del primer fichero './fichero.txt'
fs.readFile('./fichero.txt', 'utf-8', (err, text) => {
  // Callback: una función que se ejecuta después de que se completa una tarea asíncrona
  // 'err' es el posible error que ocurrió durante la operación
  // 'text' es el contenido del fichero leído, en formato UTF-8
  if (err) {
    console.error('Error al leer el primer fichero:', err)
    return
  }
  console.log('Primer texto:', text)
})

console.log('--> Haciendo cosas mientras lee el fichero...')

console.log('Leyendo el segundo fichero...')
// Operación asíncrona para leer el contenido del segundo fichero './fichero2.txt'
fs.readFile('./fichero2.txt', 'utf-8', (err, text) => {
  // Callback: una función que se ejecuta después de que se completa una tarea asíncrona
  // 'err' es el posible error que ocurrió durante la operación
  // 'text' es el contenido del fichero leído, en formato UTF-8
  if (err) {
    console.error('Error al leer el segundo fichero:', err)
    return
  }
  console.log('Segundo texto:', text)
})

/*
Lo bueno de esto es que no sabes qué tarea terminará primero.
Salida esperada podría ser en cualquier orden:
node "fs readFile Asyncrono.cjs"
Leyendo el primer fichero...
--> Haciendo cosas mientras lee el fichero...
Leyendo el segundo fichero...
Primer texto: Hola Mundo

Segundo texto:
Nombre: Daniel
Apellido: Perez
Edad: 18 años
Profesión: Programador

o también podría ser:

node "fs readFile Asyncrono.cjs"
Leyendo el primer fichero...
--> Haciendo cosas mientras lee el fichero...
Leyendo el segundo fichero...
Segundo texto:
Nombre: Daniel
Apellido: Perez
Edad: 18 años
Profesión: Programador

Primer texto: Hola Mundo
*/
