// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo: danielperezdev@proton.me

// Todas las propiedades y métodos son accesibles públicamente
// por lo que existen algunos enfoques para intentar solucionar este problema

// Enfoque basado en convenciones

// Podemos usar el símbolo de guion bajo para miembros internos
// esto es solo una convención; técnicamente, podemos acceder a las propiedades de todos modos

function TheatreSeats() {
  this._seats = []; // Convención: _seats indica que es un miembro interno
}

TheatreSeats.prototype.placePerson = function (person) {
  this._seats.push(person); // Agrega una persona a _seats
};

const theatreSeats = new TheatreSeats();
theatreSeats.placePerson({ name: "Ryan", surname: "Ray" });

theatreSeats;
