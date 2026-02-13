<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***¿Qué es un linter?***

- *Un linter es una herramienta de análisis estático que ayuda a encontrar errores, inconsistencias y problemas de estilo en el código fuente de un programa. Su objetivo principal es mejorar la calidad del código al identificar y corregir posibles problemas antes de que el código sea ejecutado. ESLint es un linter específicamente diseñado para JavaScript, altamente configurable y ampliamente utilizado en la comunidad de desarrollo.*

## ***Instalación de ESLint***

**Para instalar ESLint en tu proyecto de JavaScript, sigue estos pasos:**

```bash
npm install eslint -D
```

- *Esto instalará ESLint como una dependencia de desarrollo (`-D` o `--save-dev`), lo cual es típico ya que ESLint se usa principalmente durante el desarrollo para mejorar la calidad del código.*

### ***Inicialización de ESLint***

*Después de instalar ESLint, puedes inicializar la configuración del proyecto utilizando uno de estos comandos:*

```bash
npx eslint --init
```

**o:**

```bash
./node_modules/.bin/eslint --init
```

- *Estos comandos te guiarán a través de un proceso interactivo para configurar ESLint según las necesidades específicas de tu proyecto. Te hará preguntas sobre cómo deseas utilizar ESLint, qué tipo de módulos y frameworks usas, si utilizas TypeScript, entre otras configuraciones.*

### ***Ejemplo de Inicialización de ESLint***

```plaintext
✔ How would you like to use ESLint? · problems
✔ What type of modules does your project use? · commonjs
✔ Which framework does your project use? · none
✔ Does your project use TypeScript? · javascript
✔ Where does your code run? · node
```

- *Después de seleccionar las opciones adecuadas para tu proyecto, ESLint te informará sobre las dependencias adicionales que necesitas instalar y te permitirá hacerlo automáticamente si así lo deseas.*

### ***Comandos de ESLint***

**Una vez configurado, aquí tienes algunos comandos útiles para usar ESLint:**

- **Verificar el código:**

  ```bash
  npx eslint .
  ```

  - *Este comando ejecuta ESLint para analizar tu código y mostrar cualquier problema encontrado sin realizar cambios.*

- **Corregir automáticamente problemas simples:**

  ```bash
  npx eslint --fix .
  ```

  - *Este comando intentará corregir automáticamente los problemas que ESLint puede resolver según las reglas configuradas.*

### ***Fichero `eslint.config.mjs`***

- **El fichero `eslint.config.mjs` contiene la configuración de ESLint para tu proyecto. Aquí un ejemplo de configuración básica:**

```javascript
import pluginJs from '@eslint/js';
import globals from 'globals';

export default [
  {
    files: ['**/*.js'],
    languageOptions: { sourceType: 'commonjs' }
  },
  {
    languageOptions: { globals: globals.browser }
  },
  pluginJs.configs.recommended,

  {
    rules: {
      'semi': ['error', 'always'], // Asegura que todos los puntos y comas estén presentes
      'prefer-const': 'error', // Prefiere el uso de 'const' en lugar de 'let' cuando sea posible
      'no-extra-semi': 'error', // Prohíbe los puntos y comas adicionales
      'comma-dangle': ['error', 'never'], // No permite comas colgantes al final de los objetos
      'indent': ['error', 2], // Define la indentación de 2 espacios
      'quotes': ['error', 'single'], // Requiere el uso de comillas simples para las cadenas
      'no-console': 'warn', // Advierte sobre el uso de console.log y otras funciones de consola
      'no-unused-vars': 'warn' // Advierte sobre variables declaradas pero no utilizadas
    }
  }
];
```

### ***Significado en el `package.json`***

- *Dentro de tu `package.json`, los scripts definidos pueden ejecutar diferentes tareas, incluyendo el uso de ESLint:*

```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "lint": "eslint --fix ."
},
```

- **`test`:** *Un script predeterminado que generalmente se usa para ejecutar pruebas unitarias. En este caso, simplemente imprime un mensaje de error porque no hay pruebas especificadas.*
- **`lint`:** *Un script personalizado que ejecuta ESLint con la opción `--fix`, intentando corregir automáticamente problemas de estilo en tu código.*

### ***Documentación Oficial***

**Aquí están los enlaces a la documentación oficial de ESLint, donde puedes encontrar más detalles sobre cómo configurar y usar ESLint:**

- *[Configuración de ESLint](https://eslint.org/docs/latest/user-guide/configuring/ "https://eslint.org/docs/latest/user-guide/configuring/")*
- *[Interfaz de línea de comandos de ESLint](https://eslint.org/docs/latest/user-guide/command-line-interface/ "https://eslint.org/docs/latest/user-guide/command-line-interface/")*

### ***Comandos Adicionales***

**Algunos comandos adicionales que podrían ser útiles:**

- **Verificar solo ficheros específicos:**

  ```bash
  npx eslint fichero.js
  ```

  - *Esto analizará solo el fichero `fichero.js` en lugar de todo el proyecto.*

- **Verificar ficheros y mostrar solo errores (sin advertencias):**

  ```bash
  npx eslint --quiet .
  ```

  - *Esto oculta advertencias y solo muestra errores al verificar todo el proyecto.*

*Con estos comandos y configuraciones, podrás utilizar ESLint eficazmente para mejorar la calidad y consistencia de tu código JavaScript.*

> [!CAUTION]
> **Recordar Reiniciar Vscode por si la extension Eslint no reconoce el ficheoro de configuracion**
