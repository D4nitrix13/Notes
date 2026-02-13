// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

import pluginJs from "@eslint/js";
import tseslint from "@typescript-eslint/eslint-plugin";
import tsparser from "@typescript-eslint/parser";
import globals from "globals";

export default [
  {
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"],
    languageOptions: {
      globals: { ...globals.browser, ...globals.node },
      parser: tsparser, // Asegúrate de que el parser esté importado correctamente
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: "module",
        ecmaFeatures: {
          jsx: true, // Habilitar JSX si se usa React
        },
      },
    },
    rules: {
      // Reglas generales
      semi: ["error", "never"],
      quotes: ["error", "single"],
      "no-console": "warn", // Advertir sobre el uso de console.log
      "no-unused-vars": "warn", // Advertir sobre variables no utilizadas
      eqeqeq: ["error", "always"], // Usar siempre === y !==
      curly: ["error", "all"], // Obligatorio el uso de llaves
      indent: ["error", 2], // Indentación de 2 espacios
      "max-len": ["error", { code: 80 }], // Longitud máxima de línea
      "prefer-const": "warn", // Usar const en lugar de let si la variable no se reasigna

      // Reglas de TypeScript
      "@typescript-eslint/no-explicit-any": "warn", // Advertir sobre el uso de 'any'
      "@typescript-eslint/explicit-module-boundary-types": "warn", // Advertir si las funciones no tienen tipos de retorno explícitos
      "@typescript-eslint/no-unused-vars": "warn", // Advertir sobre variables no utilizadas en TypeScript
      "@typescript-eslint/consistent-type-definitions": ["error", "interface"], // Usar 'interface' en lugar de 'type' cuando sea posible

      // Reglas adicionales
      "jsx-quotes": ["error", "prefer-single"], // Usar comillas simples en JSX
      "react/jsx-filename-extension": [
        "warn",
        { extensions: [".jsx", ".tsx"] },
      ], // Permitir JSX en ficheros .jsx y .tsx
      "react/react-in-jsx-scope": "off", // No es necesario importar React en componentes funcionales
      "react/prop-types": "off", // Desactivar la validación de PropTypes si se usa TypeScript

      // Reglas de accesibilidad
      "jsx-a11y/alt-text": "warn", // Requiere texto alternativo para las imágenes
      "jsx-a11y/anchor-is-valid": "warn", // Asegurarse de que los enlaces son válidos
      "jsx-a11y/no-noninteractive-element-interactions": "warn", // Prevenir interacciones en elementos no interactivos

      // Reglas de formato
      "object-curly-spacing": ["error", "always"], // Espaciado en llaves de objetos
      "array-bracket-spacing": ["error", "never"], // Sin espacios en los corchetes de arreglos

      // Otras reglas útiles
      "no-duplicate-imports": "error", // Prohibir importaciones duplicadas
      "prefer-template": "warn", // Usar plantillas en lugar de concatenaciones
      "no-magic-numbers": [
        "warn",
        { ignore: [0, 1], ignoreArrayIndexes: true }, // Evitar números mágicos
      ],
    },
    plugins: {
      eslint: pluginJs,
      typescript: tseslint,
      react: "eslint-plugin-react",
      "jsx-a11y": "eslint-plugin-jsx-a11y",
      import: "eslint-plugin-import", // Para manejar las importaciones
    },
    settings: {
      react: {
        version: "detect", // Detecta automáticamente la versión de React
      },
      "import/resolver": {
        typescript: {}, // Permitir la resolución de módulos TypeScript
      },
    },
  },
];
