<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***`Fichero.mjs` utiliza ECMAScript Modules (ESM) para importar el módulo `os` en Node.js y luego imprime información del sistema operativo.***

## ***Comentarios Iniciales***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 
```

- *Estos comentarios proporcionan información sobre el autor del código, su perfil de GitHub y su correo electrónico de contacto.*

## ***Código en fichero.mjs***

```javascript
// fichero.mjs
// Uso del módulo 'os' para obtener información del sistema operativo en Node.js
// Importación del módulo 'os'. Nota: El uso de 'node:os' se recomienda si estás trabajando en un entorno que requiere la especificación del namespace.

// Importación del módulo 'os' para obtener información del sistema operativo
import os from 'node:os';

// Imprime información del sistema operativo
console.log("Información del sistema operativo");

// Imprime el nombre del sistema operativo
console.log("Nombre del sistema operativo:", os.platform());

// Imprime la versión del sistema operativo
console.log("Versión del sistema operativo:", os.release());

// Imprime la arquitectura del sistema operativo
console.log("Arquitectura del sistema operativo:", os.arch());

// Imprime la memoria libre del sistema en MB
console.log("Memoria libre:", (os.freemem() / 1024 / 1024).toFixed(2), "MB");

// Imprime la memoria total del sistema en MB
console.log("Memoria total:", (os.totalmem() / 1024 / 1024).toFixed(2), "MB");

// Imprime el número de hilos (CPUs disponibles)
console.log("Número de hilos (CPUs disponibles):", os.cpus().length);

// Imprime la carga promedio del sistema
console.log("Carga promedio:", os.loadavg());

// Imprime el tiempo de actividad del sistema en horas
console.log("Tiempo de actividad del sistema:", (os.uptime() / 3600).toFixed(2), "horas");
```

### ***Explicación del Código***

1. **Importación del Módulo 'os':**
   - *`import os from 'node:os';`: Importa el módulo `os` usando la sintaxis de ECMAScript Modules. En este caso, se utiliza `'node:os'` para especificar el namespace del módulo, lo cual es necesario en ciertos entornos de desarrollo.*

2. **Impresión de Información del Sistema Operativo:**
   - *`os.platform()`: Devuelve el nombre del sistema operativo.*
   - *`os.release()`: Devuelve la versión del sistema operativo.*
   - *`os.arch()`: Devuelve la arquitectura del sistema operativo.*
   - *`os.freemem()`: Devuelve la cantidad de memoria libre en bytes.*
   - *`os.totalmem()`: Devuelve la cantidad total de memoria en bytes.*
   - *`os.cpus().length`: Devuelve el número de hilos (CPUs) disponibles en el sistema.*
   - *`os.loadavg()`: Devuelve un array con la carga promedio del sistema.*
   - *`os.uptime()`: Devuelve el tiempo de actividad del sistema en segundos.*

3. **Conversión de Bytes a MB:**
   - *`(os.freemem() / 1024 / 1024).toFixed(2)`: Convierte la memoria libre del sistema de bytes a megabytes (MB), redondeando a dos decimales.*
   - *`(os.totalmem() / 1024 / 1024).toFixed(2)`: Convierte la memoria total del sistema de bytes a megabytes (MB), también redondeando a dos decimales.*

### ***Notas Adicionales***

- ***Uso de ECMAScript Modules (ESM):** Permite una forma moderna y más estructurada de importar y exportar módulos en JavaScript, mejorando la modularidad y la claridad del código.*
  
- ***Especificación de 'node:os':** Específicamente en entornos como VS Code, la especificación del namespace `'node:os'` puede ser necesaria para evitar conflictos de importación y asegurar que se esté utilizando el módulo correcto.*

- *Este código proporciona una manera eficiente y moderna de obtener y mostrar información crucial del sistema operativo utilizando Node.js y ECMAScript Modules.*
