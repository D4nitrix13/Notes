// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// fichero con extensión .mjs

// Uso de Promesas con módulos nativos en Node.js

// Nota: En versiones anteriores de Node.js, las funciones de los módulos nativos
// no retornaban promesas de forma nativa, por lo que era común usar 'promisify' del módulo 'util'.

// const { promisify } = require('node:util');
// const readFilePromise = promisify(fs.readFile);

// Con el uso de promesas, podemos manejar el código asincrónico de manera más eficiente.

// Sin embargo, el siguiente enfoque no es válido en CommonJS porque async/await no es soportado directamente:

/*
const fs = require('node:fs/promises');

console.log('Leyendo el primer fichero...');
const text = fs.readFile('./fichero.txt', 'utf-8');
console.log('primer texto:', text);

console.log('--> Hacer cosas mientras lee el fichero...');

console.log('Leyendo el segundo fichero...');
const secondText = fs.readFile('./fichero2.txt', 'utf-8');
console.log('segundo texto:', text);
*/

// En módulos ECMAScript (ESM), el uso de async/await es completamente soportado.
// Importamos la función readFile del módulo 'fs/promises' para manejar operaciones de ficheros de manera asincrónica.

import { readFile } from 'node:fs/promises'

console.log('Leyendo el primer fichero...')
const text = await readFile('./fichero.txt', 'utf-8')
console.log('primer texto:', text)

console.log('--> Hacer cosas mientras lee el fichero...')

console.log('Leyendo el segundo fichero...')
const secondText = await readFile('./fichero2.txt', 'utf-8')
console.log('segundo texto:', secondText)

/*
Comentarios adicionales:
1. El uso de `await` permite que el código se detenga en esa línea hasta que la promesa se resuelva,
   haciendo que el código se ejecute de manera secuencial en lugar de paralela.

2. Esto es útil para leer ficheros en un orden específico sin bloquear el hilo principal,
   permitiendo que otras operaciones se ejecuten mientras se espera la lectura de los ficheros.

3. Es importante recordar que el uso de `await` sólo es válido dentro de funciones `async` o en
   módulos ECMAScript (ESM) directamente.
*/
