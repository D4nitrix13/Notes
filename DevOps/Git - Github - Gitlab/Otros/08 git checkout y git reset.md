<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git checkout" y "git reset"***

*`git checkout`, `git reset` y `git diff` son comandos fundamentales en Git, un sistema de control de versiones distribuido ampliamente utilizado para el desarrollo de software. Aquí tienes una explicación de cada uno, junto con su sintaxis típica en formato Markdown (`.md`):*

---

## ***`git checkout`***

> *El comando `git checkout` se utiliza principalmente para cambiar entre ramas, deshacer cambios locales o incluso para restaurar ficheros específicos a un estado anterior.*

```bash
git checkout <nombre_rama>       # Cambiar a una rama específica
git checkout -b <nueva_rama>    # Crear y cambiar a una nueva rama
git checkout -- <fichero>       # Descartar cambios en un fichero específico
git checkout <commit> -- <fichero>  # Restaurar un fichero específico desde un commit
git checkout <commit>            # Mover HEAD a un commit específico (modo detached HEAD)
```

```bash
git checkout -b <nueva_rama>    # Crear y cambiar a una nueva rama
```

```bash
git checkout -- <fichero>       # Descartar cambios en un fichero específico
```

```bash
git checkout <commit> -- <fichero>  # Restaurar un fichero específico desde un commit
```

```bash
git checkout <commit>            # Mover HEAD a un commit específico (modo detached HEAD)
```

- *Los guiones dobles (`--`) en la sintaxis de `git checkout -- <fichero>` indican que lo que sigue a ellos no es una opción de línea de comandos, sino que es un argumento que se debe tratar como tal. Esto es especialmente útil cuando el nombre del fichero puede ser interpretado incorrectamente como una opción por Git.*

- *Por ejemplo, si tienes un fichero fichero `master` en tu repositorio y ejecutas `git checkout master`, Git podría interpretarlo como un intento de cambiar a la rama `master`. Sin embargo, si en realidad deseas deshacer los cambios en un fichero fichero `master`, deberías usar `git checkout -- master`.*

- *Entonces, en resumen, los guiones dobles (`--`) indican que no hay más opciones de línea de comandos después de ellos, lo que ayuda a evitar confusiones y asegura que cualquier texto que siga se interprete correctamente como un argumento.*

---

### ***`git reset`***

> *El comando `git reset` se usa para deshacer cambios en el árbol de trabajo y en el índice (staging area), pero no en el historial de confirmaciones (commits). Puede utilizarse para mover HEAD y la rama actual a un commit específico.*

---

#### ***Sintaxis en Markdown***

```bash
git reset --soft <commit>    # Deshacer commits manteniendo los cambios en el área de preparación
```

```bash
git reset --mixed <commit>   # Deshacer commits y deshacer los cambios en el área de preparación
```

```bash
git reset --hard <commit>    # Deshacer commits y deshacer los cambios en el área de preparación y en el árbol de trabajo
```

> *Estos comandos son esenciales para trabajar eficientemente con Git y para gestionar el historial de cambios en un proyecto de desarrollo de software.*
