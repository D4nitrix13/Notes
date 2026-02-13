<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git clone"***

- *El comando `git clone` se utiliza para clonar un repositorio Git existente desde un repositorio remoto (por lo general, en un servidor como GitHub, GitLab o Bitbucket) y crear una copia local del mismo en tu máquina. Aquí tienes cómo usar `git clone`:*

```bash
git clone <URL Del Repository> [<directory Destino Optional>]
```

- *`<URL Del Repository>` es la URL del repositorio remoto que deseas clonar. Puedes obtener esta URL desde la página del repositorio en la plataforma de alojamiento (por ejemplo, GitHub).*

- *`[<directory Destino Optional>]` es opcional y especifica el directorio donde se clonará el repositorio. Si no se proporciona, se creará un nuevo directorio con el nombre del repositorio.*

**Ejemplo:**

```bash
git clone https://github.com/usuario/proyecto.git
```

- **Esto clonará el repositorio `proyecto` del usuario `usuario` en GitHub y creará un nuevo directorio llamado `proyecto` en tu directorio actual.**

```bash
git clone https://github.com/usuario/proyecto.git mi_proyecto
```

```bash
git clone https://github.com/usuario/proyecto.git ../mi_proyecto
```

*Esto clonará el repositorio `proyecto` en un nuevo directorio llamado `mi_proyecto` en tu directorio actual.*

- **Una vez que hayas clonado el repositorio, tendrás una copia local completa del repositorio remoto en tu máquina, incluyendo todas las ramas y el historial de cambios. Puedes trabajar en este repositorio localmente y utilizar comandos como `git add`, `git commit`, `git push`, etc., para interactuar con el repositorio remoto.**

> *El comando `git clone` se utiliza para crear una copia local de un repositorio remoto. Existen varias opciones interesantes que puedes usar con `git clone` para ajustar el proceso de clonación según tus necesidades.*

---

## ***Opciones de `git clone`***

1. **`--branch <nombre_rama>` o `-b <nombre_rama>`**
   - **Función:** *Clona una rama específica en lugar de la rama por defecto (generalmente `master` o `main`).*
   - **Uso:** *Esto es útil si solo te interesa una rama específica y no necesitas clonar todo el historial de otras ramas.*
   - **Ejemplo:**

     ```bash
     git clone --branch feature-branch https://github.com/user/repo.git
     ```

2. **`--depth <n>`**
   - **Función:** *Clona solo los últimos `n` commits del repositorio, creando una clonación superficial (Valor mínimo: 1).*
   - **Uso:** *Esto es útil para reducir el tiempo de clonación y el espacio en disco si solo necesitas los últimos cambios.*
   - **Ejemplo:**

     ```bash
     git clone --depth 1 https://github.com/user/repo.git
     ```

3. **`--single-branch`**
   - **Función:** *Clona solo la rama actual, en lugar de todas las ramas.*
   - **Uso:** *Se usa en combinación con `--branch` para clonar solo una rama específica sin todo el historial de ramas.*
   - **Ejemplo:**

     ```bash
     git clone --branch feature-branch --single-branch https://github.com/user/repo.git
     ```

4. **`--recurse-submodules`**
   - **Función:** *Clona también los submódulos del repositorio.*
   - **Uso:** *Es útil si el repositorio contiene submódulos que también quieres clonar.*
   - **Ejemplo:**

     ```bash
     git clone --recurse-submodules https://github.com/user/repo.git
     ```

5. **`--shallow-submodules`**
   - **Función:** *Clona submódulos de manera superficial (es decir, solo con un historial limitado).*
   - **Uso:** *Para reducir el tamaño de la clonación cuando los submódulos tienen un historial grande.*
   - **Ejemplo:**

     ```bash
     git clone --shallow-submodules https://github.com/user/repo.git
     ```

6. **`--mirror`**
   - **Función:** *Clona el repositorio incluyendo todos los refs, tags y ramas remotas. Es una clonación más completa comparada con la clonación estándar.*
   - **Uso:** *Ideal para hacer una copia exacta del repositorio, incluyendo toda su configuración remota.*
   - **Ejemplo:**

     ```bash
     git clone --mirror https://github.com/user/repo.git
     ```

7. **`--bare`**
   - **Función:** *Crea un repositorio "bare", es decir, sin un directorio de trabajo. El repositorio solo contiene los datos del repositorio y no los ficheros de trabajo.*
   - **Uso:** *Se utiliza a menudo para configurar repositorios de servidor.*
   - **Ejemplo:**

     ```bash
     git clone --bare https://github.com/user/repo.git
     ```

8. **`--config <key=value>`**
   - **Función:** *Establece una configuración específica durante la clonación.*
   - **Uso:** *Para configurar opciones adicionales en el momento de la clonación.*
   - **Ejemplo:**

     ```bash
     git clone --config user.name="Daniel Perez" https://github.com/user/repo.git
     ```

9. **`--no-checkout`**
   - **Función:** *Clona el repositorio sin hacer checkout del código, es decir, no coloca los ficheros en el directorio de trabajo.*
   - **Uso:** *Útil si solo necesitas los datos del repositorio pero no los ficheros en tu sistema de ficheros.*
   - **Ejemplo:**

     ```bash
     git clone --no-checkout https://github.com/user/repo.git
     ```

*Estas opciones te permiten personalizar la clonación según tus necesidades y el contexto del proyecto. Puedes combinar varias opciones según lo que quieras lograr con la clonación del repositorio.*
