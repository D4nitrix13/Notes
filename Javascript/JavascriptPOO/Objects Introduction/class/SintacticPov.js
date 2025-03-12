// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Una clase es una colección de métodos agrupados por un nombre
// Uno de los métodos de una clase es el constructor, que se ejecuta cuando creamos una instancia de la clase
class myClass {
  // El constructor es un método especial que se llama automáticamente al crear una instancia de la clase
  // Aquí definimos tres propiedades: 'property1', 'property2' y 'property3'
  constructor(value1, value2) {
    this.property1 = value1;  // Asigna 'value1' a la propiedad 'property1'
    this.property2 = value2;  // Asigna 'value2' a la propiedad 'property2'
    this.property3 = "";      // Inicializa 'property3' con un valor vacío
  }

  // Los métodos son funciones definidas dentro de la clase
  method1() {
    // Método vacío (puede tener alguna funcionalidad)
  }

  method2() {
    // Otro método vacío (puede tener alguna funcionalidad)
  }
}

// Al acceder al prototipo de la clase 'myClass', podemos ver los métodos que se heredan de la clase
myClass.prototype; // Objeto que contiene los métodos definidos en la clase, como 'method1' y 'method2'
