// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// La composición es un tipo fuerte de agregación.
// Cada componente no tiene vida independiente sin su propietario

const person = {
  name: "Ryan",
  surname: "Ray",
  // Este objeto depende de su propietario, si la persona es eliminada, también se elimina este objeto
  address: {
    street: "123 Baker Street",
    city: "London",
    country: "United Kingdom",
  },
};
