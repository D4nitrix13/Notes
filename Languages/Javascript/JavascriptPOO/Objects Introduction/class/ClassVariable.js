// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Definimos una clase utilizando una expresión de clase (asignada a una constante)
const Person = class {
  // Constructor que recibe dos parámetros: 'name' y 'lastname'
  constructor(name, lastname) {
    this.name = name;  // Asigna el valor del parámetro 'name' a la propiedad 'name'
    this.lastname = lastname;  // Asigna el valor del parámetro 'lastname' a la propiedad 'lastname'
  }
};

// Creamos una nueva instancia de la clase Person, pasando "joe" y "doe" como parámetros
const person = new Person("joe", "doe");  // Crea un objeto con 'name' = "joe" y 'lastname' = "doe"
