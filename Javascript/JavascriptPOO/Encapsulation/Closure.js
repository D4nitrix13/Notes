// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo: danielperezdev@proton.me

// El enfoque basado en convenciones permite acceder a la propiedad de todos modos
// por lo que, para solucionar esto, el enfoque consiste en no usar propiedades para miembros internos
// sino variables en el constructor

function TheatreSeats() {
  const seats = []; // Declaramos seats como una variable privada

  this.placePerson = function (person) {
    seats.push(person); // Agrega una persona al arreglo seats
  };
}

// Alcance y cierre
// const greeting = "Hola mundo";

// function greets(person) {
//   const fullName = person.name + " " + person.surname;

//   function displayGreeting() {
//     console.log(greeting + " " + fullName);
//   }

//   displayGreeting();
// }

// greets({ name: "Ryan", surname: "Ray" });

// En JavaScript, podemos acceder al alcance exterior incluso cuando la función que lo creó
// ya ha terminado
const greeting = "Buenos días";
let displayGreeting;

function greets(person) {
  const fullName = person.name + " " + person.surname;

  return function () {
    console.log(greeting + " " + fullName);
  };
}

displayGreeting = greets({ name: "Ryan", surname: "Ray" });
displayGreeting();
