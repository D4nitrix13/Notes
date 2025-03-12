// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

/**
 * A Person object
 * @type {{id: number, firstName: string, lastName: string, age: number}}
 */
const person = {
  id: 1,
  firstName: "Rayn",
  lastName: "Ray",
  age: 27,
};

/**
 * A Person object with optional id and age types
 * @type {{id: number | string, firstName: string, lastName: string, age: number | string}}
 */
const person2 = {
  id: 1,
  firstName: "Joe",
  lastName: "McMillan",
  age: "35",
};
