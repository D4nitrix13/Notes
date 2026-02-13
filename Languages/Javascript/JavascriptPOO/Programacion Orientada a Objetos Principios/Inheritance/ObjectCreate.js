// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo: danielperezdev@proton.me

const userProtos = {
  getAge: function () {
    return this.age;
  },
  displayName: function () {
    return this.firstName + " " + this.lastName;
  },
};

const Daniel = Object.create(userProtos, {
  firstName: { value: "Daniel" },
  lastName: { value: "Perez" },
  age: { value: 30 },
});

Daniel.displayName();
Daniel.getAge();
