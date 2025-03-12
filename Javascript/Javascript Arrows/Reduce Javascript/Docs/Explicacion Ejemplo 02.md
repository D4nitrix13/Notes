<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

---

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const expensive = [32, 20];

// Si usas ESLint con la regla `no-return-assign`, podría mostrar un error en la siguiente línea:
// const sum = expensive.reduce((acum, price) => acum += price);
// El mensaje de error sería: "Arrow function should not return assignment.eslintno-return-assign"

const sum = expensive.reduce((acum, price) => acum += price);

console.log(sum); // 52
```

---

## ***Explicación del Comentario***

1. **ESLint y Regla `no-return-assign`:** *ESLint es una herramienta de análisis estático de código para identificar problemas en el código JavaScript. La regla `no-return-assign` evita que las funciones flecha devuelvan expresiones de asignación directa como en `acum += price`.*

2. **Mensaje de Error:** *El mensaje de error "Arrow function should not return assignment.eslintno-return-assign" indica que la función flecha dentro de `reduce` está devolviendo una expresión de asignación directa, lo cual puede ser considerado una mala práctica según la configuración de ESLint.*

3. **Solución Propuesta:** *Para evitar este error con ESLint, podrías ajustar la expresión en la función flecha para usar una forma más explícita y sin asignaciones directas, aunque el código pueda ejecutarse correctamente.*
