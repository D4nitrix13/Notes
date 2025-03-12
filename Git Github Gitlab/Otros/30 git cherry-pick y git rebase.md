<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git cherry-pick" y "git rebase"***

## ***`git cherry-pick`***

> *El comando `git cherry-pick` se utiliza para aplicar los cambios introducidos por uno o más commits en una rama diferente. Esto es útil cuando quieres agregar cambios específicos de una rama a otra sin tener que fusionar toda la rama.*

**Ejemplo de uso:**

```bash
git cherry-pick <commit-hash>
```

*Esto aplicará los cambios del commit especificado en la rama actual.*

---

### ***`git rebase`***

> *El comando `git rebase` se utiliza para reorganizar la historia de confirmaciones cambiando la base de una rama. Puede ser útil para mantener una historia de confirmaciones limpia y lineal.*

**Ejemplo de uso:**

```bash
git rebase master
```

**Esto reorganizará la rama actual para que se base en la última confirmación en la rama `master`.**

---

#### ***Opciones de `git rebase`:***

- *`--continue`: Continúa el proceso de rebase después de resolver un conflicto de fusión.*

- *`--skip`: Salta el parche actual durante un rebase interactivo.*

- *`--abort`: Aborta la operación de rebase y restablece HEAD a la rama original.*

- *`--quit`: Aborta la operación de rebase pero no restablece HEAD a la rama original.*

- *`--edit-todo`: Permite editar la lista de tareas durante un rebase interactivo.*

- *`--show-current-patch`: Muestra el parche actual durante un rebase interactivo o cuando se detiene debido a conflictos.*

**Ejemplo al hacer git rebase -i `<commit>`**

```bash
pick 6f0eddc Implementar nueva funcionalidad A
pick 43539a2 Corregir error en funcionalidad B
pick b73205a Agregar documentación del proyecto
pick d689c4b Refactorizar código de funcionalidad C
pick 7ce4d17 Agregar Licencia del proyecto

# Rebase 454c793..7ce4d17 onto 454c793 (5 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
#         create a merge commit using the original merge commit's
#         message (or the oneline, if no original merge commit was
#         specified); use -c <commit> to reword the commit message
# u, update-ref <ref> = track a placeholder for the <ref> to be updated
#                       to this position in the new commits. The <ref> is
#                       updated at the end of the rebase
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
```

```bash
* d689c4b - Implementar nueva funcionalidad A
* 2a3f5d7 - Corregir error en funcionalidad B
* b73205a - Agregar documentación del proyecto
* e1f7a8c - Refactorizar código de funcionalidad C
* pick 7ce4d17 Agregar Licencia del proyecto
```

### ***Ejemplos Visuales:***

- *`pick <commit>`: Utiliza el commit especificado tal como está.*
  
  ```bash
  pick d689c4b
  ```

- *`reword <commit>`: Utiliza el commit especificado, pero permite editar el mensaje del commit antes de aplicarlo.*

  ```bash
  reword d689c4b
  ```

- *`edit <commit>`: Utiliza el commit especificado, pero detiene el proceso de rebase para que puedas hacer cambios adicionales antes de continuar.*

  ```bash
  edit d689c4b
  ```

- *`squash <commit>`: Utiliza el commit especificado y lo fusiona con el commit anterior en la lista.*

  ```bash
  squash d689c4b
  ```

- *`fixup [-C | -c] <commit>`: Similar a `squash`, pero descarta el mensaje de confirmación del commit fusionado.*

  ```bash
  fixup -c d689c4b
  ```

- *`exec <command>`: Ejecuta un comando de shell durante el proceso de rebase.*

  ```bash
  exec make test
  ```

- *`break`: Detiene el rebase en este punto, permitiendo que se reanude más tarde.*

  ```bash
  break
  ```

- *`drop <commit>`: Elimina el commit especificado de la historia.*

  ```bash
  drop d689c4b
  ```

- *`label <label>`: Etiqueta el commit actual con un nombre.*

  ```bash
  label my-label
  ```

- *`reset <label>`: Restablece HEAD al commit etiquetado.*

  ```bash
  reset my-label
  ```

- *`merge [-C <commit> | -c <commit>] <label> [# <oneline>]`: Crea un commit de fusión utilizando el mensaje del commit original.*

  ```bash
  merge -C d689c4b
  ```

- *`update-ref <ref>`: Actualiza una referencia a la posición actual en los nuevos commits.*

  ```bash
  update-ref HEAD
  ```
