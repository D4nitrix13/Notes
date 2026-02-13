<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***`jsconfig.json`***

---

## ***Estructura del Fichero***

*El fichero `jsconfig.json` se utiliza en proyectos de JavaScript (o TypeScript) para definir configuraciones que afectan el comportamiento del compilador, especialmente en un entorno de desarrollo como Visual Studio Code. A continuación, se describen las diferentes secciones de la configuración:*

---

### ***1. compilerOptions***

*Esta sección contiene las opciones de configuración para el compilador. Estas opciones son similares a las que se pueden definir en un fichero `tsconfig.json` (usado para TypeScript), y son relevantes para la forma en que el código JavaScript se interpreta y se verifica.*

- **module:** *`"ESNext"`*
  - *Esta opción especifica el sistema de módulos que se utilizará en el proyecto. Al establecerlo como `ESNext`, se permite el uso de las últimas características de módulos de JavaScript, como `import` y `export`.*

- **moduleResolution:** *`"Bundler"`*
  - *Esto indica cómo el compilador debe resolver los módulos. Al configurarlo como `Bundler`, se utiliza un enfoque similar al de los empaquetadores como Webpack o Parcel, lo que es útil en aplicaciones modernas que utilizan herramientas de empaquetado.*

- **target:** *`"ES2022"`*
  - *Define la versión de ECMAScript a la que se debe compilar el código. `ES2022` permite utilizar las características más recientes de JavaScript, como mejoras en las funciones y otras características de ES2022.*

- **jsx:** *`"react"`*
  - *Especifica cómo se debe procesar el código JSX (JavaScript XML). Al configurarlo como `react`, se indica que el código JSX debe ser transformado en funciones de React.*

- **allowImportingTsExtensions:** *`true`*
  - *Esta opción permite importar ficheros TypeScript (con extensión `.ts` o `.tsx`) directamente desde ficheros JavaScript. Es útil en proyectos donde se combinan JavaScript y TypeScript.*

- **strictNullChecks:** *`true`*
  - *Activa la verificación estricta de null y undefined. Cuando está habilitado, el compilador exige que se manejen explícitamente los casos en que una variable puede ser null o undefined, lo que ayuda a evitar errores comunes.*

- **strictFunctionTypes:** *`true`*
  - *Esta opción mejora la verificación de tipos para funciones. Al activarla, se permite que el compilador realice una comprobación más rigurosa de los tipos de las funciones, lo que mejora la robustez del código.*

---

#### ***2. exclude***

**Esta sección se utiliza para especificar ficheros o directorios que el compilador debe ignorar. En tu configuración, se excluyen:**

- **"node_modules":** *Esto excluye la directorio `node_modules`, que contiene todas las dependencias instaladas del proyecto. Generalmente, no se quiere que el compilador analice o incluya estos ficheros, ya que son bibliotecas de terceros.*

- **"`/node_modules/*`":** *Esta es una forma adicional de asegurarse de que todas las directorios `node_modules` en cualquier subdirectorio también se excluyan del análisis. Aunque incluir solo `node_modules` ya es suficiente, esta línea es más explícita.*
