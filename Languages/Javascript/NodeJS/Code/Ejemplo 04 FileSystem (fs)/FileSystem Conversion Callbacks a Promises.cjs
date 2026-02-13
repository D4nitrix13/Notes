// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Esto sólo en los módulos nativos
// que no tienen promesas nativas

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs')

// Importación del módulo 'util' para promisificar funciones
const { promisify } = require('node:util')

// Promisificar la función fs.readFile
const readFilePromise = promisify(fs.readFile)

console.log('Leyendo el primer fichero...')

// Utilizando la función promisificada para leer el primer fichero './fichero.txt'
readFilePromise('./fichero.txt', 'utf-8')
  .then((text) => {
    console.log('Primer texto:', text)
  })
  .catch((err) => {
    console.error('Error al leer el primer fichero:', err)
  })

console.log('--> Haciendo cosas mientras lee el fichero...')

console.log('Leyendo el segundo fichero...')

// Utilizando la función promisificada para leer el segundo fichero './fichero2.txt'
readFilePromise('./fichero2.txt', 'utf-8')
  .then((text) => {
    console.log('Segundo texto:', text)
  })
  .catch((err) => {
    console.error('Error al leer el segundo fichero:', err)
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
