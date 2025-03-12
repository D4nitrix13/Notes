// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Asyncrono vs Syncrono en Node.js

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs') // Se recomienda 'node:' antes del módulo nativo a partir de Node.js 16

// Operación sincrónica para obtener estadísticas del fichero './fichero.txt'
const statsSync = fs.statSync('./fichero.txt')

// Imprimir las estadísticas obtenidas de manera sincrónica
console.log('Operación sincrónica:')
console.log(
  statsSync.isFile(), // Verifica si 'fichero.txt' es un fichero
  statsSync.isDirectory(), // Verifica si 'fichero.txt' es un directorio
  statsSync.isSymbolicLink(), // Verifica si 'fichero.txt' es un enlace simbólico
  statsSync.size // Muestra el tamaño en bytes de 'fichero.txt'
)

// Operación asíncrona para obtener estadísticas del fichero './fichero.txt'
fs.stat('./fichero.txt', (err, statsAsync) => {
  if (err) {
    console.error('Error al obtener estadísticas asíncronas:', err)
    return
  }

  // Imprimir las estadísticas obtenidas de manera asíncrona
  console.log('\nOperación asíncrona:')
  console.log(
    statsAsync.isFile(), // Verifica si 'fichero.txt' es un fichero
    statsAsync.isDirectory(), // Verifica si 'fichero.txt' es un directorio
    statsAsync.isSymbolicLink(), // Verifica si 'fichero.txt' es un enlace simbólico
    statsAsync.size // Muestra el tamaño en bytes de 'fichero.txt'
  )
})
