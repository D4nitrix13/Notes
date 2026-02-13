// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo: danielperezdev@proton.me

// La herencia permite que nuevos objetos adquieran propiedades de objetos existentes

// Esto nos permite evitar repetir código, por ejemplo, si tenemos una clase 'Programmer' y una clase 'Person'

// Podríamos evitar repetir el nombre y el apellido

// function Person () {
//   this.name = ""
//   this.surname = ""
// }

// function Programmer() {
//   this.language = ""
// }

// Heredar propiedades de Person como 'name' y 'surname'
// Programmer.prototype = new Person()

// Crear un nuevo programador
// const programmer = new Programmer()

// programmer.name = "Ryan"
// programmer.surname = "Ray"
// programmer.language = "Python"
// programmer

// Y con clases

class Person {
  constructor(name, surname) {
    this.name = name;
    this.surname = surname;
  }
}

const person = new Person("Ryan", "Ray");

class Programmer extends Person {
  constructor(language) {
    super(); // Llamada al constructor de la clase base 'Person'
    this.language = language;
  }
}

const programmer = new Programmer();
programmer.name = "Ryan";
programmer.surname = "Ray";
programmer.language = "Python";
console.log(programmer)

// https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/Inheritance
