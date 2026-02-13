// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs')

// Lectura sincrónica del primer fichero './fichero.txt'
console.log('Leyendo el primer fichero...')
const text = fs.readFileSync('./fichero.txt', 'utf-8')
console.log('Primer texto:', text)

// El Syncrono es como secuencial
console.log('--> Haciendo cosas mientras lee el fichero...')

// Lectura sincrónica del segundo fichero './fichero2.txt'
console.log('Leyendo el segundo fichero...')
const secondText = fs.readFileSync('./fichero2.txt', 'utf-8')
console.log('Segundo texto:', secondText)
