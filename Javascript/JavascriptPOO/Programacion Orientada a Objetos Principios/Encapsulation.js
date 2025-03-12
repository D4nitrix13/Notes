// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// La encapsulación consiste en ocultar la complejidad y agrupar la funcionalidad y las propiedades

const company = {
  name: "Daniel Perez",
  employees: [],
  sortEmployees: function () { },
};

// Cuando el comportamiento interno depende de propiedades públicas, frustramos el esfuerzo de ocultar los detalles internos

company.employees = "some random string"; // Se modifica directamente la propiedad employees, lo que puede causar errores

company.sortEmployees()

// Podríamos evitar el acceso directo a propiedades relevantes, reemplazándolas con métodos

function Company(name) {
  let employees = []; // Variable privada

  this.name = name;

  // Método para obtener empleados
  this.getEmployees = function () {
    return employees;
  };

  // Método para agregar empleados
  this.addEmployee = function (employee) {
    employees.push(employee);
  };

  // Método para ordenar empleados
  this.sortEmployees = function () { };
}

class Company2 {
  constructor(name) {
    this.name = name;
    this.employees = [];
  }

  // Método para obtener empleados
  getEmployees() {
    return this.employees;
  }

  // Método para agregar empleados
  addemployee(employee) {
    this.employees.push(employee);
  }

  // Método para ordenar empleados
  sortEmployees() { }
}

// Con este enfoque, necesitamos usar métodos para obtener y agregar empleados a la lista
const person = {
  name: "ryan",
  surname: "Ray",
  location: "London"
}

// Se crea una nueva instancia de Company2
const company2 = new Company2("D4nitrix13");

// Se agrega un empleado a la compañía
company2.addemployee(person);

// Se obtiene la lista de empleados
console.log(company2.getEmployees())
console.log(company2)
