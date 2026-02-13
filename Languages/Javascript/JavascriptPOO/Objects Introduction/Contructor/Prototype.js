// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Este es un constructor de objetos que acepta parámetros para inicializar las propiedades
function Person(name, surname) {
  this.name = name;  // Asigna el parámetro 'name' a la propiedad 'name' del objeto
  this.surname = surname;  // Asigna el parámetro 'surname' a la propiedad 'surname' del objeto
  this.address = "";  // Inicializa la propiedad 'address' con una cadena vacía
  this.email = "";  // Inicializa la propiedad 'email' con una cadena vacía
}

// Usamos el prototipo para agregar un método a todas las instancias creadas por el constructor 'Person'
Person.prototype.displayFullName = function () {
  return this.name + " " + this.surname;  // Devuelve el nombre completo concatenando 'name' y 'surname'
};

// Creamos dos instancias de la función constructora 'Person'
const jamesWilson = new Person("James", "Wilson");  // Crea un objeto Person con 'James' y 'Wilson'
const gregoryHouse = new Person("Gregory", "House");  // Crea un objeto Person con 'Gregory' y 'House'

// Llamamos al método 'displayFullName' para obtener el nombre completo de ambas personas
console.log(jamesWilson.displayFullName());  // Muestra: 'James Wilson'
console.log(gregoryHouse.displayFullName());  // Muestra: 'Gregory House'

// Podemos acceder al prototipo de 'Person' y ver qué métodos están disponibles
console.log(Person.prototype);  // Muestra el objeto prototipo de 'Person', que incluye el método 'displayFullName'
