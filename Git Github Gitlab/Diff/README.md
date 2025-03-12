<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git diff"***

> *El comando `git diff` se utiliza para ver las diferencias entre el árbol de trabajo y el área de preparación (staging area), entre el área de preparación y el último commit, o entre dos commits diferentes, entre otros usos.*

```bash
git diff                        # Ver diferencias entre el árbol de trabajo y el área de preparación
```

```bash
git diff --staged               # Ver diferencias entre el área de preparación y el último commit
```

```bash
git diff <commit1> <commit2>    # Ver diferencias entre dos commits específicos
```

```bash
git diff <rama1>..<rama2>       # Ver diferencias entre dos ramas
```

```bash
git diff <fichero>              # Ver diferencias en un fichero específico
```

- *En Git, los dos puntos (`..`) se utilizan para denotar un rango entre dos referencias de commit, como ramas o etiquetas. En el contexto de `git diff`, la sintaxis `git diff <rama1>..<rama2>` mostrará las diferencias entre los commits alcanzables desde `rama1` pero no desde `rama2`.*

**Por ejemplo:**

```bash
git diff master..develop
```

> *Este comando mostrará las diferencias entre el punto en el que divergieron las ramas `master` y `develop`.*
