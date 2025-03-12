<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Ramas en Git***

> [!IMPORTANT]
> *Las **ramas** en Git son una forma efectiva de aislar el trabajo en características, experimentos o cualquier otra segregación de tareas en tu código. Aquí te presento algunos comandos esenciales y avanzados relacionados con las ramas en Git.*

---

## ***Comandos básicos***

- *`git branch`: Este comando lista todas las ramas en tu repositorio.*

```bash
git branch
```

- *`git branch <nombre>`: Este comando crea una nueva rama con el nombre `<nombre>`.*

```bash
git branch nueva-rama
```

- *`git checkout <nombre>`: Este comando cambia a la rama `<nombre>`.*

```bash
git checkout nueva-rama
```

- *`git branch -d <nombre>`: Este comando elimina la rama `<nombre>`.*

```bash
git branch -d nueva-rama
```

- *`git branch -D <nombre>`: Este comando elimina la rama `<nombre>` incluso si no ha sido fusionada con su rama ascendente. Ten cuidado al usar esta opción, ya que puedes perder cambios en la rama que estás eliminando.*

```bash
git branch -D nueva-rama
```

---

## ***Comandos avanzados***

- *`git branch -m <nombre>`: Este comando renombra la rama actual a `<nombre>`.*

```bash
git branch -m nuevo-nombre
```

- *`git checkout -b <nombre>`: Este comando crea una nueva rama con el nombre `<nombre>` y cambia a ella en un solo paso.*

```bash
git checkout -b nueva-rama
```

- *`git branch -v`: Este comando muestra la última confirmación en cada rama.*

```bash
git branch -v
```

- *`git branch --verbose`: Este comando muestra la última confirmación en cada rama.*

```bash
git branch --verbose
```

- *`git branch --merged`: Este comando lista las ramas que han sido fusionadas a la rama actual.*

```bash
git branch --merged
```

- *`git branch --no-merged`: Este comando lista las ramas que no han sido fusionadas a la rama actual.*

```bash
git branch --no-merged
```

**Usar kebab-case al nombrar ramas en Git es una práctica recomendada por varias razones:**

1. **Legibilidad:** *El kebab-case utiliza guiones para separar palabras en lugar de espacios o camelCase. Esto hace que los nombres de las ramas sean más legibles y fáciles de entender, especialmente cuando se muestran en interfaces de línea de comandos o herramientas de control de versiones.*

2. **Consistencia:** *Al seguir una convención de nomenclatura consistente, como el kebab-case, se facilita la identificación y la asociación de las ramas con las funcionalidades o tareas que representan. Esto ayuda a mantener un flujo de trabajo organizado y coherente en el equipo.*

3. **Compatibilidad:** *Algunas herramientas y sistemas operativos pueden tener restricciones o problemas al manejar espacios o caracteres especiales en los nombres de las ramas. El kebab-case evita estos problemas al utilizar solo caracteres alfanuméricos y guiones.*

4. **Facilita la URL y la referencia en código:** *Al utilizar kebab-case, los nombres de las ramas pueden incorporarse fácilmente en URLs o referencias en el código fuente sin necesidad de escapar caracteres especiales o realizar ajustes adicionales.*

**Ejemplos de nombres de ramas en kebab-case:**

- *`feature/add-login-page`*

- *`bugfix/fix-database-connection`*

- *`hotfix/update-readme`*

- *`refactor/update-user-interface`*

*Estos nombres de ramas son descriptivos, fáciles de entender y siguen la convención de kebab-case, lo que los hace ideales para mantener un historial de cambios claro y organizado en un repositorio Git.*
