// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// La asociación es la relación entre dos objetos
// Cada objeto es independiente del otro
// Por lo tanto, un objeto puede existir sin el otro

class Person {
  constructor(name, surname) {
    this.name = name;
    this.surname = surname;
    this.parent = null; // Propiedad opcional que indica el padre de la persona
  }
}

const johnSmith = new Person("John", "Smith"); // Creación de un objeto 'johnSmith'
const fredSmith = new Person("Fred", "Smith"); // Creación de un objeto 'fredSmith'
fredSmith.parent = johnSmith; // Asignación de 'johnSmith' como el padre de 'fredSmith'
