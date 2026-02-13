<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Convertir el código de CommonJS a ECMAScript Modules (ESM) en Node.js `fichero.mjs`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// fichero.mjs
// Uso del módulo 'os' para obtener información del sistema operativo en Node.js
// Importación del módulo 'os'. Nota: El uso de 'node:os' se recomienda si estás trabajando en un entorno que requiere la especificación del namespace.

// Importación del módulo 'os' para obtener información del sistema operativo
import { platform, release, arch, freemem, totalmem, cpus, loadavg, uptime } from 'node:os';

// Imprime información del sistema operativo
console.log("Información del sistema operativo");

// Imprime el nombre del sistema operativo
console.log("Nombre del sistema operativo:", platform());

// Imprime la versión del sistema operativo
console.log("Versión del sistema operativo:", release());

// Imprime la arquitectura del sistema operativo
console.log("Arquitectura del sistema operativo:", arch());

// Imprime la memoria libre del sistema en MB
console.log("Memoria libre:", (freemem() / 1024 / 1024).toFixed(2), "MB");

// Imprime la memoria total del sistema en MB
console.log("Memoria total:", (totalmem() / 1024 / 1024).toFixed(2), "MB");

// Imprime el número de hilos (CPUs disponibles)
console.log("Número de hilos (CPUs disponibles):", cpus().length);

// Imprime la carga promedio del sistema
console.log("Carga promedio:", loadavg());

// Imprime el tiempo de actividad del sistema en horas
console.log("Tiempo de actividad del sistema:", (uptime() / 3600).toFixed(2), "horas");
```

## ***Explicación y Mejoras***

1. **Uso de ECMAScript Modules (ESM):**
   - *Se utiliza la sintaxis de importación de ESM (`import { ... } from 'node:os';`) para importar funciones específicas del módulo `os`.*
   - *Esto reemplaza el uso de `require('node:os')` en CommonJS, facilitando el manejo de dependencias y el uso de módulos en un entorno moderno.*

2. **Funciones Importadas del Módulo 'os':**
   - **`platform()`:** *Devuelve el nombre del sistema operativo.*
   - **`release()`:** *Devuelve la versión del sistema operativo.*
   - **`arch()`:** *Devuelve la arquitectura del sistema operativo.*
   - **`freemem()`:** *Devuelve la cantidad de memoria libre en bytes.*
   - **`totalmem()`:** *Devuelve la cantidad total de memoria en bytes.*
   - **`cpus()`:** *Devuelve un array con información sobre los núcleos (CPUs) del sistema.*
   - **`loadavg()`:** *Devuelve un array con la carga promedio del sistema.*
   - **`uptime()`:** *Devuelve el tiempo de actividad del sistema en segundos.*

3. **Conversión de Bytes a MB:**
   - *`(freemem() / 1024 / 1024).toFixed(2)`: Convierte la memoria libre del sistema de bytes a megabytes (MB), redondeando a dos decimales.*
   - *`(totalmem() / 1024 / 1024).toFixed(2)`: Convierte la memoria total del sistema de bytes a megabytes (MB), también redondeando a dos decimales.*

### ***Uso de `node:os` en VS Code***

- **Atajo en VS Code:** *Para convertir un módulo de CommonJS a ESM en VS Code, puedes usar el atajo `Ctrl + .` (Control + punto). Este atajo mostrará una lista de acciones rápidas, incluida la opción para convertir el `require` a una importación de módulo.*

*Este formato mejorado utiliza las capacidades de ECMAScript Modules para importar funciones específicas del módulo `os`, lo que mejora la claridad y la mantenibilidad del código en comparación con CommonJS.*
