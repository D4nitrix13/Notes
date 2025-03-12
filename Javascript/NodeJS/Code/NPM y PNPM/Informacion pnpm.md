<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación de pnpm***

**Para instalar pnpm, puedes utilizar npm (Node Package Manager):**

```bash
npm install -g pnpm
```

- *Esto instalará pnpm globalmente en tu sistema, lo que te permitirá usarlo desde cualquier directorio en la línea de comandos.*

## ***Comandos Básicos de pnpm***

### ***Inicialización de un Proyecto***

**Para iniciar un nuevo proyecto con pnpm:**

```bash
pnpm init
```

- **Este comando te guiará para crear un fichero `package.json` similar a npm.**

#### ***Instalación de Dependencias***

- **Para instalar dependencias con pnpm:**

```bash
pnpm install <paquete>
```

**Por ejemplo:**

```bash
pnpm install lodash
```

#### ***Desinstalación de Dependencias***

**Para desinstalar dependencias con pnpm:**

```bash
pnpm uninstall <paquete>
```

**Por ejemplo:**

```bash
pnpm uninstall lodash
```

#### ***Actualización de Dependencias***

**Para actualizar dependencias con pnpm:**

```bash
pnpm update <paquete>
```

**Por ejemplo:**

```bash
pnpm update lodash
```

#### ***Ejecución de Scripts***

**Para ejecutar scripts definidos en `package.json` con pnpm:**

```bash
pnpm run <script>
```

**Por ejemplo, si tienes un script `test`:**

```bash
pnpm run test
```

#### ***Ver más Información***

- *Para obtener más información sobre pnpm y sus comandos, puedes consultar la documentación oficial en [pnpm.io](https://pnpm.io/ "https://pnpm.io/").*

### ***Ejemplo de Uso Completo***

**Un ejemplo completo de cómo trabajar con pnpm sería:**

1. **Inicialización del Proyecto:**

   ```bash
   pnpm init
   ```

2. **Instalación de Dependencias:**

   ```bash
   pnpm install lodash
   ```

3. **Actualización de Dependencias:**

   ```bash
   pnpm update lodash
   ```

4. **Ejecución de Scripts:**

   ```bash
   pnpm run test
   ```

5. **Desinstalación de Dependencias:**

   ```bash
   pnpm uninstall lodash
   ```

- *Con estos comandos básicos, puedes gestionar eficientemente las dependencias de tu proyecto utilizando pnpm.*
