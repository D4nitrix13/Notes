// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Definimos una clase Person con un constructor que recibe 'name' y 'surname' como parámetros
class Person {
  constructor(name, surname) {
    this.name = name;  // Asigna el valor de 'name' a la propiedad 'name'
    this.surname = surname;  // Asigna el valor de 'surname' a la propiedad 'surname'
  }
}

// Creamos una instancia de la clase Person pasando los valores "Ryan" y "Ray"
const ryanRay = new Person("Ryan", "Ray");

// La siguiente línea causaría un error porque las clases no se pueden invocar como funciones normales:
// const person = Person('personName', 'personSurname'); // ERROR: no se puede invocar la clase de esta manera

// La definición de la clase 'Person' es equivalente a esta función constructora:
function Person() {
  "use strict";  // Modo estricto para evitar errores en el uso de 'this'
  this.name = name;  // Asigna el valor del parámetro 'name' a la propiedad 'name'
  this.surname = surname;  // Asigna el valor del parámetro 'surname' a la propiedad 'surname'
}

// Para comprobar que las clases en JavaScript son solo una "azúcar sintáctica" (syntactic sugar),
// podemos comprobar que la clase 'Person' es en realidad una función
typeof Person;  // "function"  -- las clases son internamente funciones constructoras

// Ahora definimos una clase 'PersonTwo' de la misma manera que en el ejemplo anterior,
// pero usando la expresión de clase en lugar de la declaración de clase.
let PersonTwo = class {
  constructor(name, surname) {
    this.name = name;  // Asigna 'name' a la propiedad 'name'
    this.surname = surname;  // Asigna 'surname' a la propiedad 'surname'
  }
};

// Creamos una nueva instancia de la clase 'PersonTwo'
let john = new PersonTwo("John", "Carter");
