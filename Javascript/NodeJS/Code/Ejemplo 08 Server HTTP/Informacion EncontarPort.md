<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***EncontrarPort***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importamos el módulo net de Node.js, que nos permite trabajar con sockets y redes
const net = require('node:net');

// Función asincrónica para encontrar un puerto disponible
function findAvailablePort(desiredPort) {
  return new Promise((resolve, reject) => {
    // Creamos un servidor net
    const server = net.createServer();

    // Intentamos escuchar en el puerto deseado
    server.listen(desiredPort, () => {
      // Cuando el servidor está escuchando, obtenemos el puerto asignado
      const { port } = server.address();
      
      // Cerramos el servidor para liberar el puerto
      server.close(() => {
        // Resolvemos la promesa con el puerto disponible
        resolve(port);
      });
    });

    // Manejamos errores de servidor
    server.on('error', (err) => {
      // Si el puerto está en uso (EADDRINUSE), intentamos encontrar el próximo puerto disponible recursivamente
      if (err.code === 'EADDRINUSE') {
        findAvailablePort(0).then(port => resolve(port)); // Llamada recursiva para encontrar el próximo puerto disponible
      } else {
        // Si hay otro tipo de error, rechazamos la promesa
        reject(err);
      }
    });
  });
}

// Exportamos la función para ser utilizada en otros módulos
module.exports = { findAvailablePort };
```

## ***Explicación del Código con Comentarios***

1. **Importación del Módulo `net`:**

   ```javascript
   const net = require('node:net');
   ```

   - *Importamos el módulo `net` de Node.js, que proporciona funcionalidades para trabajar con redes y sockets.*

2. **Función `findAvailablePort`:**

   ```javascript
   function findAvailablePort(desiredPort) {
     return new Promise((resolve, reject) => {
       // Creación de un servidor net
       const server = net.createServer();
   
       // Intento de escuchar en el puerto deseado
       server.listen(desiredPort, () => {
         // Cuando el servidor está escuchando, obtenemos el puerto asignado
         const { port } = server.address();
         
         // Cerramos el servidor para liberar el puerto
         server.close(() => {
           // Resolvemos la promesa con el puerto disponible
           resolve(port);
         });
       });
   
       // Manejo de errores del servidor
       server.on('error', (err) => {
         // Si el puerto está en uso (EADDRINUSE), intentamos encontrar el próximo puerto disponible recursivamente
         if (err.code === 'EADDRINUSE') {
           findAvailablePort(0).then(port => resolve(port)); // Llamada recursiva para encontrar el próximo puerto disponible
         } else {
           // Si hay otro tipo de error, rechazamos la promesa
           reject(err);
         }
       });
     });
   }
   ```

   - *`findAvailablePort`: Función asíncrona que devuelve una promesa.*
   - *Dentro de la promesa, creamos un servidor net con `net.createServer()`.*
   - *Intentamos escuchar en el puerto `desiredPort`.*
   - *Cuando el servidor está escuchando (`server.listen`), obtenemos el puerto asignado usando `server.address()`.*
   - *Cerramos el servidor para liberar el puerto con `server.close()`.*
   - *Resolvemos la promesa con el puerto disponible usando `resolve(port)`.*
   - *Manejamos errores con `server.on('error')`: Si el error es `EADDRINUSE` (puerto en uso), llamamos recursivamente `findAvailablePort(0)` para encontrar el próximo puerto disponible.*
   - *Otros errores son rechazados con `reject(err)`.*

3. **Exportación de la Función:**

   ```javascript
   module.exports = { findAvailablePort };
   ```

   - *Exportamos la función `findAvailablePort` para que pueda ser utilizada en otros módulos.*

- *Este código permite encontrar de manera eficiente un puerto disponible para iniciar un servidor, manejando correctamente los casos donde el puerto deseado está ocupado.*
