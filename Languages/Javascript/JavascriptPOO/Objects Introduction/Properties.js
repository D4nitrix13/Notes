// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

// Las comillas dobles son opcionales para las claves si son nombres válidos de variables
const john = {
  name: "John",  // 'name' es un nombre válido de variable
  surname: "Smith",  // 'surname' también es un nombre válido de variable
};

// Pero si el nombre de la propiedad no es un nombre válido de variable, 
// debemos usar comillas dobles alrededor de la clave
const joe = {
  "first-name": "joe",  // 'first-name' no es un nombre válido de variable, por lo que se usan comillas dobles
  "second-name": "Carter",  // Lo mismo aquí
};

// Objeto anidado, podemos asignar un objeto dentro de otro objeto
let ryan = {
  name: "Ryan",
  surname: "Ray",
  address: {  // 'address' es otro objeto anidado
    street: "13 duncannon Street",
    city: "London",
    country: "United Kingdom",
  },
};

// Para acceder a los valores de las propiedades, podemos usar notación de punto
let name = john.name;  // 'john' tiene la propiedad 'name', se puede acceder como 'john.name'

// O podemos usar notación de corchetes con cadenas
// Esto es necesario si el nombre de la propiedad no es un nombre válido de variable
let firstname = joe["first-name"];  // 'joe' tiene la propiedad 'first-name', se accede con 'joe["first-name"]'

// Si accedemos a una propiedad que no existe, obtenemos 'undefined'
let age = joe.age;  // Como 'joe' no tiene la propiedad 'age', esto devuelve 'undefined'

// Si asignamos un valor a una propiedad que aún no está definida, en realidad creamos esa propiedad
joe.age = 28;  // Ahora 'joe' tiene la propiedad 'age' con el valor 28

// Podemos comenzar con una definición básica y agregar más propiedades gradualmente
let newUser = {};  // Creamos un objeto vacío

newUser.name = "Greg";  // Agregamos una propiedad 'name'
newUser.surname = "House";  // Agregamos una propiedad 'surname'
newUser.address = {  // Agregamos una propiedad 'address', que es otro objeto
  street: "123 dunncannon street",
  city: "London",
  country: "United Kingdom",
};
newUser.age = 28;  // Agregamos una propiedad 'age'

// Además de crear propiedades dinámicamente, también podemos eliminarlas
delete newUser.age;  // Elimina la propiedad 'age' de 'newUser'
