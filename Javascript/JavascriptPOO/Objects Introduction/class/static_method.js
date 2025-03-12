// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Definimos la clase base 'User', que tiene un constructor que recibe 'name' y 'lastname' como parámetros
class User {
  constructor(name, lastname) {
    this.name = name;        // Asigna 'name' a la propiedad 'name'
    this.lastname = lastname; // Asigna 'lastname' a la propiedad 'lastname'
  }
}

// Definimos una clase 'Programmer' que extiende de la clase 'User'
// Esto significa que 'Programmer' hereda todas las propiedades y métodos de 'User'
class Programmer extends User {
  constructor(language, name, lastname) {
    super();                   // Llama al constructor de la clase 'User' para inicializar las propiedades heredadas
    this.language = language;  // Asigna 'language' a la propiedad 'language'
    this.name = name;          // Sobrescribe 'name' con el valor proporcionado
    this.lastname = lastname;  // Sobrescribe 'lastname' con el valor proporcionado
  }
}

// Creamos una nueva instancia de 'Programmer' pasando los valores de 'language', 'name', y 'lastname'
const joe = new Programmer("Javascript", "Joe", "Doe");

// Mostramos el objeto creado
joe; // { name: "Joe", lastname: "Doe", language: "Javascript" }
