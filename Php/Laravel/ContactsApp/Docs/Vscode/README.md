<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **`.vscode/` — ¿Qué es?**

*Es un directorio especial donde Visual Studio Code guarda configuraciones **específicas del proyecto** (no globales). Esto te permite:*

* *Definir qué extensiones instalar automáticamente*
* *Ajustar configuración del editor solo para este workspace*
* *Automatizar tareas (como levantar servicios Docker)*

---

## **`extensions.json` – Recomendaciones de extensiones**

```json
{
 // See https://go.microsoft.com/fwlink/?LinkId=827846 to learn about workspace recommendations.
 // Extension identifier format: ${publisher}.${name}. Example: vscode.csharp
 // List of extensions which should be recommended for users of this workspace.
 "recommendations": [
  // Php Laravel
  "bmewburn.vscode-intelephense-client",
  "ironGeek.vscode-env",
  "shufo.vscode-blade-formatter",
  "austenc.laravel-blade-spacer",
  "amiralizadeh9480.laravel-extra-intellisense",
  "cjhowe7.laravel-blade",
  "cweijan.vscode-mysql-client2",
  "MehediDracula.php-constructor",
  "xdebug.php-debug",
  "neilbrayfield.php-docblocker",
  "MehediDracula.php-namespace-resolver",
  "formulahendry.auto-close-tag",
  "formulahendry.auto-rename-tag",
  "christian-kohler.path-intellisense",
  "Zignd.html-css-class-completion"
  // Typescript Express
  // "YoavBls.pretty-ts-errors",
  // "MylesMurphy.prettify-ts",
  // Rust Axum
  // "rust-lang.rust-analyzer"
 ],
 // List of extensions recommended by VS Code that should not be recommended for users of this workspace.
 "unwantedRecommendations": []
}
```

### **¿Para qué sirve?**

*Este archivo **recomienda extensiones** a cualquier persona que abra el proyecto con VSCode. VSCode mostrará un aviso del tipo:*

> *“Este proyecto recomienda algunas extensiones. ¿Quieres instalarlas?”*

**Esto es útil para mantener consistencia en el equipo.**

### **Explicación de extensiones destacadas**

| **Extensión**                                   | **Propósito**                                     |
| ----------------------------------------------- | ------------------------------------------------- |
| *`bmewburn.vscode-intelephense-client`*         | *Autocompletado e inteligencia para PHP*          |
| *`shufo.vscode-blade-formatter`*                | *Formateador para Blade*                          |
| *`amiralizadeh9480.laravel-extra-intellisense`* | *Reconoce rutas, helpers y modelos de Laravel*    |
| *`cweijan.vscode-mysql-client2`*                | *Cliente SQL visual integrado en VSCode*          |
| *`xdebug.php-debug`*                            | *Soporte de depuración con Xdebug*                |
| *`formulahendry.auto-close-tag`*                | *Cierra automáticamente etiquetas HTML/Blade*     |
| *`Zignd.html-css-class-completion`*             | *Autocompletado de clases CSS/Bootstrap/Tailwind* |

---

## **`settings.json` – Ajustes del editor para este proyecto**

```json
{
  "window.zoomLevel": 1,
  "editor.fontSize": 16,
  "editor.lineHeight": 2
}
```

* **¿Para qué sirve?**

*Personaliza la apariencia y comportamiento del editor **solo dentro de este proyecto**.*

### **Explicación**

| **Opción**            | **Valor** | **Explicación**                                               |
| --------------------- | --------- | ------------------------------------------------------------- |
| *`window.zoomLevel`*  | *`1`*     | *Aumenta el zoom general de la interfaz VSCode (fuente y UI)* |
| *`editor.fontSize`*   | *`16`*    | *Fuente del código en el editor*                              |
| *`editor.lineHeight`* | *`2`*     | *Altura de línea; útil para mejorar legibilidad*              |

---

## **`tasks.json` – Tareas automatizadas**

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start Services",
      "type": "shell",
      "command": "/bin/bash",
      "args": [
        "-c",
        "docker compose --project-name contacts-application --project-directory . -f docker-compose.yaml up -d"
      ],
      "runOptions": {
        "runOn": "folderOpen"
      }
    }
  ],
  ...
}
```

* **¿Para qué sirve?**

*Permite definir tareas personalizadas que puedes ejecutar desde **`Ctrl+Shift+P` → “Run Task”** o automáticamente.*

* **Explicación**

| **Campo**            | **Valor**            | **Significado**                                        |
| -------------------- | -------------------- | ------------------------------------------------------ |
| *`label`*            | *`"Start Services"`* | *Nombre visible en VSCode*                             |
| *`type`*             | *`"shell"`*          | *Ejecuta comando en una terminal shell*                |
| *`command`*          | *`"/bin/bash"`*      | *Interprete de comandos*                               |
| *`args`*             | *`["-c", "..."]`*    | *Argumentos para bash: ejecuta el comando como string* |
| *`runOptions.runOn`* | *`"folderOpen"`*     | *Corre la tarea automáticamente al abrir el proyecto*  |
| *`isBackground`*     | *`true`*             | *La tarea queda corriendo en segundo plano*            |
| *`presentation`*     | *{...}*              | *Controla cómo se muestra la terminal de la tarea*     |

### **Resultado**

**Cada vez que abres el proyecto en VSCode, se ejecutará automáticamente:**

```bash
docker compose --project-name contacts-application --project-directory . -f docker-compose.yaml up -d
```

*Y levantará todos tus contenedores sin que tengas que hacerlo manualmente.*
