// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// mientras que las propiedades representan datos, los métodos representan acciones
function showFullName() {
  return "John Smith";
}

const john = {};
john.showFullName = showFullName; // Asignamos una función a un objeto como método

// Podemos asignar un método dentro de su representación literal

const Daniel = {
  name: "Daniel",
  surname: "Carter",
  showFullName: function () { // Método en representación literal
    return "Daniel Carter";
  },
};

// Y en ECMASCRIPT 2015, podemos asignar un método de esta manera también
const ryan = {
  name: "Ryan",
  surname: "Ray",
  showFullName() { // Método usando sintaxis abreviada (ES6+)
    return "Ryan Ray";
  },
};

// El último método siempre muestra el mismo nombre; para evitarlo, podemos usar la palabra clave `this`
ryan.name = "Benjamin"; // Cambiamos la propiedad name
ryan.showFullName = function () {
  return this.name + " " + this.surname; // Usamos `this` para acceder a las propiedades del objeto actual
};
