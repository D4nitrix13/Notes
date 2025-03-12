// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const path = require('node:path')

// Muestra el separador de ruta específico del sistema (por ejemplo, '/' en Unix y '\' en Windows)
console.log(path.sep) // Salida: '/' en Unix, '\' en Windows

// Unir rutas de manera segura independientemente del sistema operativo
// Aquí estamos creando una ruta 'Desktop/Directory/test.txt' o 'Desktop\Directory\test.txt'
const filePath = path.join('Desktop', 'Directory', 'test.txt')
console.log(filePath) // Salida: 'Desktop/Directory/test.txt' o 'Desktop\Directory\test.txt'

// Obtener el nombre base del fichero (sin la ruta)
// Aquí obtendremos 'password.txt' de la ruta completa
const base = path.basename('/tmp/DirectorySecret/password.txt')
console.log(base) // Salida: 'password.txt'

// Obtener el nombre del fichero sin la extensión especificada
// Aquí obtendremos 'password' de 'password.txt'
const filename = path.basename('/tmp/DirectorySecret/password.txt', '.txt')
console.log(filename) // Salida: 'password'

// Obtener la extensión del fichero
// Aquí obtendremos '.py' de 'My.super.code.py'
const extension = path.extname('My.super.code.py')
console.log(extension) // Salida: '.py'
