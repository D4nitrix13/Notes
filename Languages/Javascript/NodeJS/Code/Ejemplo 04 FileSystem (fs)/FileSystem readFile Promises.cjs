// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Esto sólo en los módulos nativos
// que no tienen promesas nativas

// const { promisify } = require('node:util')
// const readFilePromise = promisify(fs.readFile)

// Las promesas es codigo asincrono

const fs = require('node:fs/promises')

console.log('Leyendo el primer fichero...')
fs.readFile('./fichero.txt', 'utf-8')
  .then(text => {
    console.log('primer texto:', text)
  })

console.log('--> Hacer cosas mientras lee el fichero...')

console.log('Leyendo el segundo fichero...')
fs.readFile('./fichero2.txt', 'utf-8')
  .then(text => {
    console.log('segundo texto:', text)
  })
