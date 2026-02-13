// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importamos el módulo net de Node.js, que nos permite trabajar con sockets y redes
const net = require('node:net')

// Función asincrónica para encontrar un puerto disponible
function findAvailablePort(desiredPort) {
  return new Promise((resolve, reject) => {
    // Creamos un servidor net
    const server = net.createServer()

    // Intentamos escuchar en el puerto deseado
    server.listen(desiredPort, () => {
      // Cuando el servidor está escuchando, obtenemos el puerto asignado
      const { port } = server.address()

      // Cerramos el servidor para liberar el puerto
      server.close(() => {
        // Resolvemos la promesa con el puerto disponible
        resolve(port)
      })
    })

    // Manejamos errores de servidor
    server.on('error', (err) => {
      // Si el puerto está en uso (EADDRINUSE), intentamos encontrar el próximo puerto disponible recursivamente
      if (err.code === 'EADDRINUSE') {
        findAvailablePort(0).then(port => resolve(port)) // Llamada recursiva para encontrar el próximo puerto disponible
      } else {
        // Si hay otro tipo de error, rechazamos la promesa
        reject(err)
      }
    })
  })
}

// Exportamos la función para ser utilizada en otros módulos
module.exports = { findAvailablePort }
