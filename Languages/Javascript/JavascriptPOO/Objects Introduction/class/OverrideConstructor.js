// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Es posible sobrescribir el comportamiento predeterminado del constructor
class MyClassTwo {
  // El constructor recibe dos parámetros: 'value1' y 'value2'
  constructor(value1, value2) {
    // En lugar de crear una instancia de la clase, el constructor devuelve un objeto personalizado
    return {
      property1: value1,  // 'property1' es asignada con el valor de 'value1'
      property2: value2,  // 'property2' es asignada con el valor de 'value2'
      location: "London",  // 'location' es una propiedad adicional con valor fijo "London"
    };
  }
}

// Al crear una nueva instancia de MyClassTwo con los valores "foo" y "bar"
let myClassTwo = new MyClassTwo("foo", "bar");

// 'myClassTwo' ahora es un objeto con las propiedades definidas en el constructor
console.log(myClassTwo);  // { property1: 'foo', property2: 'bar', location: 'London' }
