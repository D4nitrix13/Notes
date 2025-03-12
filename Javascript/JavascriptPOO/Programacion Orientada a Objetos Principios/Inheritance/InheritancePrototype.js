// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo: danielperezdev@proton.me

function User(name, lastname, age) {
  this.name = name;
  this.lastname = lastname;
  this.age = age;
}

User.prototype.displayName = function () {
  return this.name + " " + this.lastname;
};

function Programmer(language, name, lastname, age) {
  // User.call(this, "Ryan", "Ray", "Python");
  User.call(this, name, lastname, age);
  this.language = language;
}


Programmer.prototype = Object.create(User.prototype);

Programmer.prototype.constructor // User
Programmer.prototype.constructor = Programmer;
Programmer.prototype.constructor

const Daniel = new User("Daniel", "Perez", 30);

const ryanProgrammer = new Programmer("Python");
ryanProgrammer.name = "Ryan";
ryanProgrammer.lastname = "Ray";
ryanProgrammer.age = "30";

ryanProgrammer.displayName();
