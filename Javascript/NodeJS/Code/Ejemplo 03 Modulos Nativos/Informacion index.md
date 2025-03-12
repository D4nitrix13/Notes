<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// Uso del módulo 'os' para obtener información del sistema operativo en Node.js
// const os = require('os'); No recomendado
// Importación del módulo 'os'. Nota: El uso de 'node:os' se recomienda si estás trabajando en un entorno que requiere la especificación del namespace.

// Importación del módulo 'os' para obtener información del sistema operativo
const os = require('node:os');

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

## ***Explicación y Mejoras***

1. **Importación del Módulo 'os':**
   - *Se utiliza `const os = require('node:os');` para importar el módulo `os` en Node.js. Esta forma es adecuada si estás trabajando en un entorno que requiere especificar el namespace `node:` para el módulo `os`.*

2. **Información del Sistema Operativo:**
   - **`os.platform()`:** *Devuelve el nombre del sistema operativo.*
   - **`os.release()`:** *Devuelve la versión del sistema operativo.*
   - **`os.arch()`:** *Devuelve la arquitectura del sistema operativo.*

3. **Memoria del Sistema:**
   - **`os.freemem() / 1024 / 1024`:** *Calcula la memoria libre del sistema y la convierte de bytes a megabytes (MB), utilizando `toFixed(2)` para redondear a dos decimales.*
   - **`os.totalmem() / 1024 / 1024`:** *Calcula la memoria total del sistema y la convierte de bytes a megabytes (MB), también redondeando a dos decimales.*

4. **Número de Hilos (CPUs Disponibles):**
   - **`os.cpus().length`:** *Devuelve el número de CPUs disponibles en el sistema.*

5. **Carga Promedio del Sistema:**
   - **`os.loadavg()`:** *Devuelve un array con la carga promedio del sistema para los últimos 1, 5 y 15 minutos.*

6. **Tiempo de Actividad del Sistema:**
   - **`os.uptime() / 3600`:** *Devuelve el tiempo de actividad del sistema en segundos y lo convierte a horas utilizando `toFixed(2)` para mostrar dos decimales.*

### ***Conversión de Bytes a Otras Unidades***

- **Bytes a Kilobytes (KB):** *Dividiendo por `1024`.*
- **Kilobytes a Megabytes (MB):** *Dividiendo nuevamente por `1024`.*
- **Megabytes a Gigabytes (GB):** *Dividiendo nuevamente por `1024`.*
- **Gigabytes a Terabytes (TB):** *Dividiendo nuevamente por `1024`.*

- *Esta conversión se basa en el principio de que cada unidad es `1024` veces mayor que la unidad anterior en términos de bytes. Esto es útil para manejar tamaños de ficheros, uso de memoria y otros datos relacionados con la capacidad de almacenamiento en el sistema operativo.*
