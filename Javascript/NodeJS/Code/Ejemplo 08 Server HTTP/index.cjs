// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importamos el módulo http de Node.js
const http = require('node:http')

// Ejemplo de cómo ejecutar con un puerto específico desde la línea de comandos: PORT=5000 node index.cjs

// Importamos una función para encontrar un puerto disponible
const { findAvailablePort } = require('./EncontrarPort.cjs')

// Imprimimos las variables de entorno actuales
console.log(process.env)

// Definimos el puerto deseado para el servidor, por defecto 3000 si no se especifica PORT
const desiredPort = process.env.PORT ?? 3000

// Creamos un servidor HTTP que responde con "Hola mundo"
const server = http.createServer((req, res) => {
  console.log('Petición recibida')
  res.end('Hola mundo')
})

// Encontramos un puerto disponible y luego escuchamos en ese puerto
findAvailablePort(desiredPort).then(port => {
  // Iniciamos el servidor en el puerto encontrado
  server.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`)
  })
})
