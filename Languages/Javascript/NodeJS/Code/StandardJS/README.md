<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Standard***

- ***Standard** es un conjunto de reglas de estilo y prácticas recomendadas para JavaScript. Se enfoca en la consistencia y la legibilidad del código, promoviendo un estilo de codificación claro y uniforme en proyectos JavaScript. A diferencia de ESLint, que permite una configuración altamente personalizada, Standard sigue un enfoque de "opinión sobre configuración" (convention over configuration), lo que significa que no requiere configuración y se espera que los desarrolladores adopten sus reglas de estilo tal como están definidas.*

## ***Características de Standard***

- **Sin configuración:** *No requiere configuración explícita. Utiliza un conjunto predefinido de reglas de estilo que se aplican de manera uniforme.*
- **Formato automático:** *Estándar incluye herramientas para formatear automáticamente el código según sus reglas, lo que fomenta la consistencia en todo el proyecto.*
- **Enfoque en la simplicidad:** *Se centra en reglas simples y directas que mejoran la legibilidad del código sin necesidad de ajustes complejos.*

### ***Instalación de Standard***

**Para instalar Standard en tu proyecto, puedes usar npm:**

```bash
npm install standard --save-dev
```

- *Esto instalará Standard como una dependencia de desarrollo (`--save-dev` o `-D`), lo que significa que solo se utilizará en entornos de desarrollo y no en producción.*

### ***Uso de Standard***

**Una vez instalado, puedes usar Standard de varias formas:**

- **Verificar el código:**

  ```bash
  npx standard
  ```

  - *Este comando ejecutará Standard para verificar si tu código cumple con las reglas de estilo definidas. Mostrará una lista de problemas encontrados si el código no cumple con las reglas.*

- **Corregir automáticamente problemas:**

  ```bash
  npx standard --fix
  ```

  - *Este comando intentará corregir automáticamente los problemas de estilo que pueda resolver según las reglas de Standard. Es similar a `eslint --fix`, pero adaptado a las reglas específicas de Standard.*

### ***Configuración en `package.json`***

- *Para configurar ESLint para que use las reglas de Standard, puedes definir lo siguiente en tu `package.json` bajo `eslintConfig`:*

```json
"eslintConfig": {
  "extends": "./node_modules/standard/eslintrc.json"
}
```

- *Esto indica a ESLint que extienda las reglas definidas en el fichero `eslintrc.json` de Standard que se encuentra en la ubicación especificada. De esta manera, puedes usar Standard para aplicar sus reglas de estilo directamente a través de ESLint.*

### ***Documentación Adicional***

- **Para obtener más información sobre Standard y cómo usarlo, puedes consultar su documentación oficial:**

- *[Sitio web de Standard](https://standardjs.com/ "https://standardjs.com/")*
- *[Repositorio de Standard en GitHub](https://github.com/standard/standard "https://github.com/standard/standard")*

- *Standard es una opción popular entre los desarrolladores que prefieren un enfoque simple y directo para mantener la consistencia del código JavaScript sin tener que personalizar extensivamente las reglas de estilo.*

### ***Configuración en el fichero `settings.json` de VS Code***

**Para integrar ESLint con VS Code y configurar el comportamiento del editor, puedes agregar las siguientes configuraciones en tu fichero `settings.json` de VS Code:**

```json
{
  "[javascript]": {
    "editor.defaultFormatter": "dbaeumer.vscode-eslint"
  },
  "eslint.format.enable": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  },
  "files.autoSave": "afterDelay",
  "editor.formatOnSave": true
}
```

### ***Explicación de las configuraciones en `settings.json`***

- **`[javascript]`:**
  - **`"editor.defaultFormatter"`:** *Define el formateador por defecto para ficheros JavaScript. En este caso, se utiliza `dbaeumer.vscode-eslint`, lo que indica que ESLint se utilizará para formatear el código automáticamente.*

- **`eslint.format.enable`:**
  - *Habilita el formateo del código utilizando ESLint en VS Code.*

- **`editor.codeActionsOnSave`:**
  - **`"source.fixAll"`:** *Configura VS Code para que aplique automáticamente todas las correcciones disponibles al guardar (`explicit` indica que las acciones deben ser explícitamente activadas).*
  - **`"source.organizeImports"`:** *Organiza automáticamente las importaciones al guardar el fichero.*

- **`files.autoSave`:**
  - **`"afterDelay"`:** *Guarda automáticamente los cambios después de un breve retraso.*

- **`editor.formatOnSave`:**
  - *Habilita el formateo automático del código al guardar el fichero en VS Code.*

### ***Funcionalidad de las configuraciones***

- *Estas configuraciones mejoran significativamente el flujo de trabajo de desarrollo al automatizar el formateo del código y la corrección de errores según las reglas de estilo definidas por ESLint y StandardJS. Esto asegura que el código mantenga una consistencia y calidad alta, facilitando así la colaboración y mantenimiento del proyecto.*

> [!CAUTION]
> **Recordar Reiniciar Vscode por si la extension Eslint no reconoce el ficheoro de configuracion**
