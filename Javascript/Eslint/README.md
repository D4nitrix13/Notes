<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Fichero `eslint.config.mjs`:***

```javascript
// Importación de plugins necesarios para ESLint
import tseslint from '@typescript-eslint/eslint-plugin'; // Plugin para reglas específicas de TypeScript
import tsparser from '@typescript-eslint/parser'; // Parser para TypeScript
import eslintPluginImport from 'eslint-plugin-import'; // Plugin para manejar importaciones
import eslintPluginJsxA11y from 'eslint-plugin-jsx-a11y'; // Plugin para reglas de accesibilidad en JSX
import eslintPluginReact from 'eslint-plugin-react'; // Plugin para reglas específicas de React
import globals from 'globals'; // Importa un objeto que contiene las variables globales de diferentes entornos (navegador, Node.js, etc.)

// Exportación de la configuración de ESLint
export default [
  {
    // Especifica los ficheros que esta configuración de ESLint aplicará
    files: ['**/*.{js,mjs,cjs,ts,jsx,tsx}'], // Incluye ficheros JavaScript y TypeScript
    languageOptions: {
      // Configura las opciones del lenguaje
      globals: { ...globals.browser, ...globals.node }, // Expande las variables globales de navegador y Node.js
      parser: tsparser, // Establece el parser a usar (en este caso, TypeScript)
      parserOptions: {
        ecmaVersion: 2020, // Especifica la versión de ECMAScript a usar
        sourceType: 'module', // Indica que el código es un módulo ECMAScript
        ecmaFeatures: {
          jsx: true, // Habilitar soporte para JSX (necesario para proyectos de React)
        },
      },
    },
    plugins: {
      // Aquí se registran los plugins
      '@typescript-eslint': tseslint, // Plugin de ESLint para TypeScript
      'import': eslintPluginImport, // Plugin para reglas relacionadas con las importaciones
      'jsx-a11y': eslintPluginJsxA11y, // Plugin para reglas de accesibilidad en JSX
      'react': eslintPluginReact, // Plugin para reglas específicas de React
    },
    rules: {
      // Aquí se definen las reglas de linting
      // Reglas generales
      semi: ['error', 'never'], // No permitir punto y coma al final de las líneas
      quotes: ['error', 'single'], // Usar comillas simples
      'no-console': 'warn', // Advertir sobre el uso de console.log
      'no-unused-vars': 'warn', // Advertir sobre variables no utilizadas
      eqeqeq: ['error', 'always'], // Forzar el uso de === en lugar de ==
      curly: ['error', 'all'], // Forzar el uso de llaves en todas las estructuras de control
      indent: ['error', 2], // Usar dos espacios para la indentación
      'max-len': ['error', { code: 80 }], // Longitud máxima de línea de 80 caracteres
      'prefer-const': 'warn', // Advertir cuando se pueda usar 'const' en lugar de 'let'

      // Reglas de TypeScript
      '@typescript-eslint/array-type': 'error', // Exigir un tipo de array explícito
      '@typescript-eslint/no-explicit-any': ['warn', { ignoreRestArgs: true }], // Advertir sobre el uso de 'any', excepto en argumentos rest
      '@typescript-eslint/explicit-module-boundary-types': 'warn', // Advertir si las funciones no tienen tipos de retorno explícitos
      '@typescript-eslint/no-unused-vars': 'warn', // Advertir sobre variables no utilizadas (para TypeScript)
      '@typescript-eslint/consistent-type-definitions': ['error', 'interface'], // Preferir 'interface' sobre 'type' para definiciones de tipo

      // Reglas adicionales
      'jsx-quotes': ['error', 'prefer-single'], // Usar comillas simples en atributos de JSX
      'react/jsx-filename-extension': ['warn', { extensions: ['.jsx', '.tsx'] }], // Advertir si los ficheros de React no tienen las extensiones correctas
      'react/react-in-jsx-scope': 'off', // Permitir el uso de JSX sin importar React en el alcance
      'react/prop-types': 'off', // Desactivar la validación de tipos de props (ya que se usa TypeScript)

      // Reglas de accesibilidad
      'jsx-a11y/alt-text': 'warn', // Advertir sobre la falta de texto alternativo en imágenes
      'jsx-a11y/anchor-is-valid': 'warn', // Advertir sobre enlaces que no son válidos
      'jsx-a11y/no-noninteractive-element-interactions': 'warn', // Advertir sobre interacciones en elementos no interactivos

      // Reglas de formato
      'object-curly-spacing': ['error', 'always'], // Exigir espacios dentro de llaves en objetos
      'array-bracket-spacing': ['error', 'never'], // No permitir espacios dentro de corchetes de arrays

      // Otras reglas útiles
      'no-duplicate-imports': 'error', // Prohibir importaciones duplicadas
      'prefer-template': 'warn', // Advertir sobre el uso de concatenación en lugar de plantillas literales
      'no-magic-numbers': [
        'warn',
        { ignore: [0, 1], ignoreArrayIndexes: true }, // Advertir sobre números "mágicos" en el código, excepto para 0 y 1
      ],
    },
    settings: {
      react: {
        version: 'detect', // Detectar automáticamente la versión de React
      },
      'import/resolver': {
        typescript: {}, // Configurar el resolver de importaciones para TypeScript
      },
    },
  },
];
```

---

## ***Resumen de las secciones***

1. **Dependencias:** *Se comentan las instrucciones para instalar las dependencias necesarias para ESLint, tanto para npm como para pnpm.*

2. **Importaciones:** *Se importan los plugins y configuraciones necesarias para ESLint.*

3. **Exportación de configuración:** *Se exporta la configuración de ESLint, especificando qué ficheros se deben analizar, qué reglas aplicar, y configuraciones específicas.*

4. **Reglas:** *Se definen las reglas que guiarán el análisis de linting, clasificadas en generales, específicas para TypeScript, adicionales, de accesibilidad y de formato.*

5. **Ajustes adicionales:** *Se configuran ajustes específicos para React y el resolver de importaciones para TypeScript.*
