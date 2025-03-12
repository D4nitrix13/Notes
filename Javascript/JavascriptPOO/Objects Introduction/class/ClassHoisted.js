// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// A diferencia de las funciones, las clases no son "hoisted" (no se elevan)
// Esto significa que no podemos usarlas antes de su declaración

// Intentar usar una clase antes de que esté declarada genera un error
// const car = new Car(); // Error: Cannot access 'Car' before initialization

// Definimos la clase 'Car' después de intentar usarla
class Car {
  constructor() {
    // El constructor de la clase está vacío en este caso
  }
}

// Ahora que la clase 'Car' está declarada, podemos crear una nueva instancia
const car = new Car();  // Esto funciona correctamente

