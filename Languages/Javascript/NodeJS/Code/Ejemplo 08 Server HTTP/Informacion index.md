<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Index***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importamos el módulo http de Node.js
const http = require('node:http');

// Ejemplo de cómo ejecutar con un puerto específico desde la línea de comandos: PORT=5000 node index.cjs

// Importamos una función para encontrar un puerto disponible
const { findAvailablePort } = require('./EncontrarPort.cjs');

// Imprimimos las variables de entorno actuales
console.log(process.env);

// Definimos el puerto deseado para el servidor, por defecto 3000 si no se especifica PORT
const desiredPort = process.env.PORT ?? 3000;

// Creamos un servidor HTTP que responde con "Hola mundo"
const server = http.createServer((req, res) => {
  console.log('Petición recibida');
  res.end('Hola mundo');
});

// Encontramos un puerto disponible y luego escuchamos en ese puerto
findAvailablePort(desiredPort).then(port => {
  // Iniciamos el servidor en el puerto encontrado
  server.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
  });
});
```

## ***Explicación del Código***

1. **Comentarios Claros:**
   - *Cada sección del código está comentada para explicar qué hace y por qué es importante.*
   - *Los comentarios ayudan a entender las operaciones que realiza cada parte del código.*

2. **Uso de Variables de Entorno:**
   - *Utilizamos `process.env.PORT ?? 3000` para determinar el puerto en el que se ejecutará el servidor. Si no se especifica un puerto a través de `PORT`, el servidor utilizará el puerto 3000 por defecto.*

3. **Creación del Servidor HTTP:**
   - *Creamos un servidor HTTP utilizando `http.createServer()` que responde con "Hola mundo" a cada solicitud (`req`) y finaliza la respuesta (`res.end()`).*

4. **Gestión de Puerto Disponible:**
   - *Utilizamos `findAvailablePort(desiredPort)` para encontrar un puerto disponible antes de iniciar el servidor. Esto asegura que no haya conflictos de puerto si el puerto deseado está ocupado.*

5. **Inicio del Servidor:**
   - *Una vez encontrado un puerto disponible, llamamos a `server.listen(port)` para iniciar el servidor en ese puerto específico.*
   - *Se imprime en la consola la URL del servidor para facilitar el acceso (`http://localhost:${port}`).*

- *Este código ahora está estructurado de manera clara con comentarios informativos, lo que facilita la comprensión de su funcionamiento y propósito.*
