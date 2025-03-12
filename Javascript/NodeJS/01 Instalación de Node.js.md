<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación de Node.js en Linux Ubuntu LTS***

**Para instalar Node.js en Ubuntu LTS, puedes seguir estos pasos:**

1. **Usando NodeSource Repositorio:**
   - **Puedes usar el repositorio de NodeSource para obtener una versión actualizada de Node.js. Aquí te muestro cómo:**

   ```bash
   # Instalar curl si no está instalado
   sudo apt install curl

   # Descargar e instalar NodeSource PPA
   curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

   # Instalar Node.js y npm
   sudo apt install -y nodejs
   ```

   ```bash
   # installs nvm (Node Version Manager)
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

   # download and install Node.js (you may need to restart the terminal)
   nvm install 20

   # verifies the right Node.js version is in the environment
   node -v # should print `v20.15.0`

   # verifies the right NPM version is in the environment
   npm -v # should print `10.7.0`
   ```

   *Este método instala la versión `LTS (Long Term Support)` más reciente de Node.js disponible en NodeSource para tu distribución de Ubuntu.*

2. **Verificar la instalación:**
   **Puedes verificar que Node.js y npm se han instalado correctamente ejecutando:**

   ```bash
   node --version
   npm --version
   ```

   **Esto debería mostrar las versiones instaladas de Node.js y npm.**

## ***Gestores de Versiones de Node.js***

- **Los gestores de versiones de Node.js te permiten instalar y cambiar entre múltiples versiones de Node.js en tu sistema. Aquí te presento tres opciones populares:**

### ***Node Version Manager (NVM)***

**Node Version Manager (NVM)** *es una herramienta para gestionar múltiples versiones de Node.js y npm. Permite instalar versiones específicas de Node.js y cambiar entre ellas según sea necesario.*

- **Enlace:** *[NVM GitHub](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm")*
- **Instalación:**
  **Para instalar NVM, puedes usar el script de instalación automática proporcionado en el repositorio de GitHub:**

  ```bash
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
  ```

- **Uso:**
  - *Después de la instalación, puedes instalar versiones específicas de Node.js usando `nvm install <version>` y cambiar entre ellas con `nvm use <version>`.*

#### ***Fast Node Manager (FNM) (Recomendada)***

**Fast Node Manager (FNM)** *es otro gestor de versiones de Node.js que se enfoca en ser rápido y fácil de usar.*

- **Enlace:** *[FNM GitHub](https://github.com/Schniz/fnm "https://github.com/Schniz/fnm")*
- **Instalación:**
  **Puedes instalar FNM utilizando el siguiente comando:**

  ```bash
  # Instalar rust
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

  # Instalar fnm
  curl -fsSL https://fnm.vercel.app/install | bash
  ```

- **Uso:**
  - *Después de la instalación, puedes instalar y cambiar entre versiones de Node.js utilizando comandos similares a NVM (`fnm install <version>`, `fnm use <version>`).*

#### ***N (Node.js Version Management)***

**N** *es un gestor de versiones de Node.js que se centra en ser simple y eficiente.*

- **Enlace:** [N GitHub](https://github.com/tj/n "https://github.com/tj/n")
- **Instalación:**
  **Para instalar N, puedes ejecutar los siguientes comandos:**

  ```bash
  curl -L https://git.io/n-install | bash
  ```

- **Uso:**
  *Después de la instalación, puedes instalar versiones de Node.js con `n <version>` y cambiar entre ellas con `n use <version>`.*

### ***Resumen***

- *Utilizando cualquiera de estos gestores de versiones, puedes manejar fácilmente múltiples versiones de Node.js en tu sistema Linux Ubuntu, lo que es útil para trabajar en proyectos que requieren versiones específicas de Node.js o para probar compatibilidad con diferentes versiones de bibliotecas y frameworks. Cada gestor tiene sus características únicas, pero todos te permiten controlar las versiones de Node.js de manera flexible según tus necesidades de desarrollo.*
