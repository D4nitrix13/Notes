// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Podemos cambiar la estructura de un objeto después de su creación
function Person(name, surname) {
  this.name = name;
  this.surname = surname;
}

const john = new Person("John", "Smith");
const mario = new Person("Mario", "Rossi");

john.greets = function () { // Añadimos un método solo al objeto `john`
  return `Hello ${this.name} ${this.surname}!`;
};

// Pero, para cambiar la estructura de todos los objetos
// creados por un constructor

Person.prototype.greets = function () { // Añadimos un método al prototipo de `Person`
  return `Hello I'am ${this.name} ${this.surname}!`;
};

mario.greets() // Llama al método desde el prototipo
