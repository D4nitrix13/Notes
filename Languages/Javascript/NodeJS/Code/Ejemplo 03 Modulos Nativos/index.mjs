// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// index.mjs
// Uso del módulo 'os' para obtener información del sistema operativo en Node.js
// Importación del módulo 'os'. Nota: El uso de 'node:os' se recomienda si estás trabajando en un entorno que requiere la especificación del namespace.

// Importación del módulo 'os' para obtener información del sistema operativo
import { arch, cpus, freemem, loadavg, platform, release, totalmem, uptime } from 'node:os'

// Imprime información del sistema operativo
console.log('Información del sistema operativo')

// Imprime el nombre del sistema operativo
console.log('Nombre del sistema operativo:', platform())

// Imprime la versión del sistema operativo
console.log('Versión del sistema operativo:', release())

// Imprime la arquitectura del sistema operativo
console.log('Arquitectura del sistema operativo:', arch())

// Imprime la memoria libre del sistema en MB
console.log('Memoria libre:', (freemem() / 1024 / 1024).toFixed(2), 'MB')

// Imprime la memoria total del sistema en MB
console.log('Memoria total:', (totalmem() / 1024 / 1024).toFixed(2), 'MB')

// Imprime el número de hilos (CPUs disponibles)
console.log('Número de hilos (CPUs disponibles):', cpus().length)

// Imprime la carga promedio del sistema
console.log('Carga promedio:', loadavg())

// Imprime el tiempo de actividad del sistema en horas
console.log('Tiempo de actividad del sistema:', (uptime() / 3600).toFixed(2), 'horas')
