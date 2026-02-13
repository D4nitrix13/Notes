// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Se puede usar el constructor Object para crear objetos genéricos
let personA = new Object();  // Usamos el constructor Object para crear un objeto vacío
personA.name = "Ryan";  // Asignamos la propiedad 'name' al objeto
personA.surname = "Ray";  // Asignamos la propiedad 'surname' al objeto

// Es equivalente a crear el objeto usando notación literal
// El siguiente código crea el mismo objeto 'personA' con la notación literal
const personB = { name: "Ryan", surname: "Ray" };

// Verificamos si el objeto creado con notación literal tiene como constructor a 'Object'
const person = {};  // Objeto creado con notación literal
console.log(person.constructor == Object);  // true, porque el constructor es 'Object'

// El constructor Object también puede generar objetos a partir de cualquier expresión de JavaScript

// Ejemplo de crear un objeto a partir de un número
let number = new Object(12);  // Crea un objeto con el valor 12
console.log(number);  // Muestra el objeto: Number { 12 }

// Ejemplo de crear un objeto con el resultado de una operación
let anotherNumber = new Object(3 * 2);  // Crea un objeto con el valor 6 (resultado de la multiplicación)
console.log(anotherNumber);  // Muestra el objeto: Number { 6 }

// Ejemplo de crear un objeto con una cadena de texto
let string = new Object("test");  // Crea un objeto con el valor "test"
console.log(string);  // Muestra el objeto: String { "test" }

// Ejemplo de crear un objeto con propiedades definidas en el constructor
let john = new Object({ name: "John", surname: "Smith" });  // Crea un objeto con las propiedades proporcionadas
console.log(john);  // Muestra el objeto: Object { name: "John", surname: "Smith" }
