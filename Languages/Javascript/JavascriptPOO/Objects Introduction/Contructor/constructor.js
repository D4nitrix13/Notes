// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Este constructor acepta parámetros
function Person(name, surname) {
  this.name = name; // Asigna el parámetro `name` al objeto
  this.surname = surname; // Asigna el parámetro `surname` al objeto
  this.address = ""; // Inicializa la propiedad `address` como una cadena vacía
  this.email = ""; // Inicializa la propiedad `email` como una cadena vacía
  this.displayFullName = function () { // Define un método para mostrar el nombre completo
    return this.name + " " + this.surname; // Devuelve el nombre completo (name + surname)
  };
}

const jamesWilson = new Person("James", "Wilson"); // Crea un nuevo objeto Person con nombre "James" y apellido "Wilson"
const gregoryHouse = new Person("Gregory", "House"); // Crea un nuevo objeto Person con nombre "Gregory" y apellido "House"

jamesWilson // Muestra el objeto jamesWilson
gregoryHouse // Muestra el objeto gregoryHouse
