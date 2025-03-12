// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

/*
Modo estricto ("use strict";): 
Cuando se activa el modo estricto, se restringen ciertas características problemáticas de JavaScript. 
Una de las diferencias importantes es que, en el modo estricto, 
el valor de this dentro de una función que no es llamada con new se establece en undefined,
n lugar de apuntar al objeto global (como ocurriría en modo no estricto). 
Esto evita que se asignen accidentalmente propiedades al objeto global.
Sin new: Si ejecutas Person() sin la palabra clave new, se produce un error.
En el modo estricto, el valor de this sería undefined, lo que causaría que las asignaciones no pudieran realizarse correctamente.

*/
function Person() {
  "use strict"; // Activando el modo estricto
  this.name = "";
  this.surname = "";
  this.address = "";
  this.email = "";
  this.displayFullName = function () {
    return this.name + " " + this.surname;
  };
}

// Crear un objeto con `new`
const person = new Person();
person; // Object { name: "", surname: "", address: "", email: "", displayFullName: function() {...} }

const mankind = {
  Person: function (name, lastname) {
    "use strict";
    this.name = name;
    this.lastname = lastname;
  },
};

// Usar `new` para crear un objeto correctamente
const joe = new mankind.Person("Joe", "Smith");
joe; // { name: "Joe", lastname: "Smith" }
