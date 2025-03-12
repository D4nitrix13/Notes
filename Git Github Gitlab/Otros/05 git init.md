<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***"git init"***

---

## ***Inicializar un repositorio***

> *Para crear un nuevo repositorio en tu directorio actual, puedes usar el comando `git init`.*

```bash
git init
```

```bash
git init .
```

```bash
git init ../repositorio
```

```bash
git init ./directorio/repositorio
```

---

## **Clonar un repositorio**

> *Si quieres trabajar con un repositorio que ya existe, puedes clonarlo con el comando `git clone`, seguido de la URL del repositorio.*

```bash
git clone https://github.com/usuario/repositorio.git
```

```bash
git clone git@github.com:usuario/repositorio.git
```

> [!IMPORTANT]
> *El comando `git init` se utiliza para crear un nuevo repositorio Git vacío o reinicializar un repositorio existente. Configura un nuevo repositorio en el directorio actual o establece un repositorio existente como un repositorio Git.*

---

## ***Opciones de `git init`***

1. **`--bare`**
   - **Función:** *Inicializa un repositorio bare, que es un repositorio sin un directorio de trabajo. Este tipo de repositorio solo contiene los datos del repositorio y es utilizado típicamente para servidores o como repositorio central.*
   - **Uso:** *Ideal para configuraciones de servidor o para mantener un repositorio de intercambio.*
   - **Ejemplo:**

     ```bash
     git init --bare /path/to/repo.git
     ```

2. **`--template=<directory>`**
   - **Función:** *Especifica un directorio de plantillas para usar durante la inicialización del repositorio. Esto permite preconfigurar el repositorio con hooks, configuraciones, y otros ficheros personalizados.*
   - **Uso:** *Útil para aplicar configuraciones predeterminadas a todos los nuevos repositorios.*
   - **Ejemplo:**

     ```bash
     git init --template=/path/to/template
     ```

3. **`--initial-branch=<branch>`**
   - **Función:** *Especifica el nombre de la rama inicial en lugar de la rama por defecto (`master` o `main`).*
   - **Uso:** *Útil para establecer una rama inicial diferente si tu flujo de trabajo utiliza una convención de nombres diferente.*
   - **Ejemplo:**

     ```bash
     git init --initial-branch=main
     ```

4. **`--separate-git-dir=<directory>`**
   - **Función:** *Configura un directorio separado para el almacenamiento de los ficheros de Git, manteniendo el repositorio en un directorio diferente al directorio de trabajo.*
   - **Uso:** *Para mantener el directorio de trabajo y el directorio Git separados.*
   - **Ejemplo:**

     ```bash
     git init --separate-git-dir=/path/to/git-dir
     ```

*Estas opciones te permiten personalizar cómo se inicializa el repositorio y ajustar su configuración para cumplir con tus necesidades específicas. `git init` es un comando fundamental para comenzar a usar Git en un nuevo proyecto o para configurar un repositorio existente.*
