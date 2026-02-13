<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Diferencia entre operaciones sincrónicas y el concepto de ejecución secuencial en Node.js:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs');

// Lectura sincrónica del primer fichero './fichero.txt'
console.log('Leyendo el primer fichero...');
const text = fs.readFileSync('./fichero.txt', 'utf-8');
console.log('Primer texto:', text);

// El Syncrono es como secuencial
console.log('--> Haciendo cosas mientras lee el fichero...');

// Lectura sincrónica del segundo fichero './fichero2.txt'
console.log('Leyendo el segundo fichero...');
const secondText = fs.readFileSync('./fichero2.txt', 'utf-8');
console.log('Segundo texto:', secondText);
```

## ***Explicación y Comentarios***

1. **Uso de `require('node:fs')`:**
   - **`const fs = require('node:fs');`:** *Importa el módulo `'fs'` de Node.js para realizar operaciones de sistema de ficheros. Usar `'node:'` antes del módulo nativo se recomienda a partir de `Node.js 16`.*

2. **Operaciones Sincrónicas (`fs.readFileSync()`):**
   - **`fs.readFileSync('./fichero.txt', 'utf-8')`:** *`fs.readFileSync()` es una función sincrónica que bloquea la ejecución del código hasta que se completa la lectura del fichero especificado (`'./fichero.txt'` en este caso). Devuelve el contenido del fichero como una cadena de texto en formato `UTF-8` `utf-8` es lo mismo que `utf8`.*

3. **Secuencialidad en Operaciones Sincrónicas:**
   - **Comentario:** *`// El Syncrono es como secuencial`. En Node.js, las operaciones sincrónicas se ejecutan de manera secuencial, lo que significa que el código espera a que cada operación se complete antes de continuar con la siguiente. Esto es útil cuando necesitas que las operaciones se realicen en un orden específico y de manera predecible.*

4. **Manejo de Múltiples Lecturas Sincrónicas:**
   - **Explicación:** *El ejemplo demuestra cómo puedes leer múltiples ficheros de manera sincrónica usando `fs.readFileSync()`. Cada lectura bloquea la ejecución del código hasta que se obtiene el resultado.*

5. **Uso de `console.log()` para Verificar la Secuencia:**
   - **Comentarios en `console.log()`:** *Los comentarios dentro de `console.log()` indican qué operación se está realizando (`'Leyendo el primer fichero...'`, `'Leyendo el segundo fichero...'`) y muestran el contenido de los ficheros leídos después de cada operación.*

### ***Importancia de las Operaciones Sincrónicas***

- **Control Secuencial:** *Las operaciones sincrónicas son útiles cuando se necesita controlar el orden de ejecución de las operaciones y cuando las operaciones dependen unas de otras.*
  
- **Simplicidad de Código:** *Las operaciones sincrónicas a menudo simplifican el código al evitar el uso de callbacks, promesas o async/await para manejar resultados y errores.*

### ***Consideraciones Finales***

- **Impacto en el Rendimiento:** *El uso excesivo de operaciones sincrónicas puede bloquear la ejecución del programa, especialmente en entornos donde se deben manejar múltiples solicitudes concurrentes.*
