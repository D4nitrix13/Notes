// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20]

// Si usas ESLint con la regla `no-return-assign`, podría mostrar un error en la siguiente línea:
// const sum = expensive.reduce((acum, price) => acum += price);
// El mensaje de error sería: "Arrow function should not return assignment.eslintno-return-assign"

const sum = expensive.reduce((acum, price) => acum += price)

console.log(sum) // 52
