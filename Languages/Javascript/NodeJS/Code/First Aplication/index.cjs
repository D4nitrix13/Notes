// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importamos el módulo 'fs/promises' para trabajar con el sistema de ficheros usando Promesas
const fs = require('node:fs/promises')

// Utilizamos 'fs.readdir' para leer el contenido del directorio actual ('.')
// Este método devuelve una Promesa, por lo que usamos '.then' y '.catch' para manejar el resultado y los errores
fs.readdir('.')
  .then(files => {
    // 'files' es un array con los nombres de los ficheros y directorios en el directorio actual
    // Usamos 'forEach' para iterar sobre cada fichero/directorio y lo imprimimos en la consola
    files.forEach(file => {
      console.log(file)
    })
  })
  .catch(err => {
    // Si ocurre un error al leer el directorio, se captura en este bloque '.catch'
    // Verificamos si 'err' existe y, si es así, imprimimos un mensaje de error en la consola
    if (err) {
      console.error('Error al leer el directorio:', err)
    }
  })

// Forma con callbacks
// Importamos el módulo 'fs' para trabajar con el sistema de ficheros usando callbacks
// const fs = require('node:fs')

// Usamos 'fs.readdir' para leer el contenido del directorio actual ('./')
// Este método toma un callback que maneja el error (si ocurre) y el resultado
// fs.readdir("./", (err, files) => {
//     // Si ocurre un error, 'err' contendrá la información sobre el error
//     if (err) {
//         // Imprimimos un mensaje de error en la consola
//         console.error("Error al leer el directorio:", err);
//     }
//     // 'files' es un array con los nombres de los ficheros y directorios en el directorio actual
//     // Usamos 'forEach' para iterar sobre cada fichero/directorio y lo imprimimos en la consola
//     files.forEach(file => {
//         console.log(file);
//     });
// })
