// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Esta es una representación literal de un objeto: { }
console.log({})

// Un objeto es un contenedor de valores combinados para formar una sola estructura de datos.

// Los objetos tienen propiedades y métodos.

// Las propiedades son datos
const person = {
  name: "John", // propiedad
  surname: "Carter",
};

// Los métodos son simplemente propiedades cuyo valor es una función

const person2 = {
  name: "Ryan",
  lastname: "Ray",
  sayHello: function () { // método sayHello
    return "Hello I'am Ryan";
  }
};

// Un objeto es una *lista* de pares clave-valor
const user = {
  username: "Daniel", // clave: valor
  email: "Daniel@gmail.com",
  password: "somepassword",
  age: 100,
  hobbies: ["read", "programming", "run"] // las propiedades también pueden ser arreglos u otros objetos
};

console.log(user);

// Y como cualquier lista, puede estar vacía
const emptyObject = {};
