// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo: danielperezdev@proton.me

// Es la habilidad de manejar múltiples tipos de datos de manera uniforme

// Nos permite crear código más compacto

// Formas comunes de soportar el polimorfismo en lenguajes:
// Métodos que toman parámetros con diferentes tipos (sobrecarga)
// Gestión de tipos genéricos, no conocidos de antemano (polimorfismo paramétrico)
// Expresiones cuyo tipo puede ser representado por una clase y clases derivadas de ella (polimorfismo de subtipo) y polimorfismo de inclusión)

// x podría ser una cadena o un valor numérico
function countItems(x) {
  return x.toString().length;
}

countItems(3); // Devuelve 1
countItems("Hello World"); // Devuelve 11

function sum(x, y, z) {
  x = x ? x : 0;
  y = y ? y : 0;
  z = z ? z : 0;
  return x + y + z;
}

sum(1, 3, 6); // Devuelve 10
sum(10, 20); // Devuelve 30
sum(3); // Devuelve 3

function sum2(x = 0, y = 0, z = 0) {
  return x + y + z;
}

const sum3 = (x = 0, y = 0, z = 0) => x + y + z;

// JavaScript soporta el polimorfismo de una manera más directa que los lenguajes de tipo fuerte

/// Polimorfismo Paramétrico
// El polimorfismo paramétrico nos permite trabajar con parámetros de cualquier tipo

function Person(name, surname) {
  this.name = name;
  this.surname = surname;
}

function Programmer(language) {
  this.language = language;
}

Programmer.prototype = new Person();

function writeFullName(p) {
  return p.name + " " + p.surname;
}

const john = new Person("John", "Cartar");

const ryan = new Programmer("Python");
ryan.name = "Ryan";
ryan.surname = "Ray";

writeFullName(john); // Devuelve "John Cartar"
writeFullName(ryan); // Devuelve "Ryan Ray"
