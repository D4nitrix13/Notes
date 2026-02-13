// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// El objeto 'process' en Node.js es una instancia de EventEmitter que proporciona información y control sobre el proceso de Node.js que se está ejecutando actualmente.
// 'globalThis' es una referencia global al objeto global en cualquier entorno (node, navegador, etc.)
console.log(globalThis.process)

// 'process.argv' es una propiedad que contiene un array de los argumentos de línea de comandos pasados cuando se inició el proceso de Node.js.
// Los primeros dos elementos son:
// 1. La ruta del ejecutable de Node.js.
// 2. La ruta del fichero JavaScript que se está ejecutando.
// Los siguientes elementos son los argumentos adicionales proporcionados.
console.log(process.argv)
/*
Si ejecutamos este script con la línea de comandos:
node process.cjs Daniel Perez Morales 18 Programador Batman
La salida sería:
[
  '/home/d4nitrix13/.fnm/node-versions/v20.15.0/installation/bin/node', // Ruta del ejecutable de Node.js
  '/home/d4nitrix13/Desktop/NodeJs/Code/Ejemplo 06 Process/process.cjs', // Ruta del fichero que se está ejecutando
  'Daniel', // Argumentos adicionales
  'Perez',
  'Morales',
  '18',
  'Programador',
  'Batman'
]
*/

// 'process.exit(código)' se utiliza para finalizar el proceso de Node.js inmediatamente.
// Un código de salida de 0 indica una salida exitosa, mientras que cualquier otro código indica un error.
// process.exit(0)

// Podemos controlar eventos del proceso usando 'process.on(evento, callback)'.
// El evento 'exit' se emite cuando el proceso está a punto de terminar.
// Aquí, podemos realizar tareas de limpieza, como cerrar conexiones de bases de datos o liberar recursos.
// process.on("exit", () => {
//     // Realizar tareas de limpieza
// })

// 'process.cwd()' devuelve el directorio de trabajo actual desde el cual se inició el proceso de Node.js.
console.log(process.cwd())

// 'process.env' es un objeto que contiene las variables de entorno del sistema.
// Podemos establecer variables de entorno al iniciar el proceso, por ejemplo: NAME=Daniel node process.cjs
// Aquí, accedemos a la variable de entorno NAME.
console.log(process.env.NAME)
