<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git stash"***

> *El comando `git stash` se utiliza en Git para almacenar temporalmente cambios locales que no están listos para ser confirmados aún. Esto es útil cuando estás trabajando en una rama pero necesitas cambiar rápidamente a otra rama o estado, y quieres guardar temporalmente tus cambios sin realizar un commit.*

**Aquí hay algunos usos comunes del comando `git stash`:**

1. **Guardar cambios locales en un stash:** *Puedes guardar los cambios locales en un stash utilizando:*

   ```bash
   git stash
   ```

   *Esto guardará todos los cambios que no estén preparados para ser confirmados en un stash. Los cambios serán eliminados del área de preparación (staging area) y del directorio de trabajo.*

2. **Listar stashes:** *Puedes listar todos los stashes guardados utilizando:*

   ```bash
   git stash list
   ```

   *Esto mostrará una lista de todos los stashes guardados, junto con un identificador único para cada uno.*

3. **Aplicar un stash:** *Puedes aplicar un stash guardado a tu rama actual utilizando:*

   ```bash
   git stash apply
   ```

   *Esto aplicará el stash más reciente a tu rama actual. Si tienes múltiples stashes y quieres aplicar uno específico, puedes usar:*

   ```bash
   git stash apply stash@{n}
   ```

   *Donde `n` es el número del stash que deseas aplicar.*

4. **Eliminar un stash:** *Puedes eliminar un stash guardado utilizando:*

   ```bash
   git stash drop
   ```

   *Esto eliminará el stash más reciente. Al igual que con `git stash apply`, si deseas eliminar un stash específico, puedes usar:*

   ```bash
   git stash drop stash@{n}
   ```

5. **Aplicar y eliminar un stash:** *Puedes aplicar y eliminar un stash en una sola operación utilizando:*

   ```bash
   git stash pop
   ```

   *Esto aplicará el stash más reciente a tu rama actual y luego lo eliminará de la lista de stashes.*

- **El comando `git stash` es útil para guardar temporalmente cambios locales mientras trabajas en diferentes tareas o ramas en tu repositorio. Te permite mantener un historial limpio y organizado mientras trabajas en múltiples cosas al mismo tiempo.**

*Aquí tienes algunos ejemplos de cómo usar el comando `git stash` en diferentes situaciones:*

---

## ***Ejemplo 1: Guardar cambios antes de cambiar de rama***

> *Supongamos que estás trabajando en una rama `feature` y tienes algunos cambios que aún no quieres confirmar. Sin embargo, necesitas cambiar a la rama `main` para revisar algo rápidamente. En este caso, puedes guardar tus cambios en un stash antes de cambiar de rama:*

```bash
# Guardar los cambios en un stash
git stash
```

```bash
# Cambiar a la rama main
git checkout main
```

*Una vez que hayas terminado de revisar en la rama `main`, puedes regresar a tu rama `feature` y aplicar el stash:*

```bash
# Regresar a la rama feature
git checkout feature
```

```bash
# Aplicar el stash guardado
git stash apply
```

---

### ***Ejemplo 2: Guardar cambios antes de hacer un pull***

> *Supongamos que estás trabajando en una rama local y deseas actualizar tu rama con los cambios del repositorio remoto. Antes de hacer un `git pull`, decides guardar tus cambios locales en un stash para evitar conflictos:*

```bash
# Guardar los cambios en un stash
git stash
```

```bash
# Actualizar la rama local con los cambios del repositorio remoto
git pull origin mi-rama
```

*Una vez que hayas realizado el `git pull`, puedes aplicar tus cambios guardados:*

```bash
# Aplicar el stash guardado
git stash apply
```

---

### ***Ejemplo 3: Guardar cambios antes de hacer un reset***

> *Supongamos que has realizado algunos cambios en tu directorio de trabajo y deseas volver al estado anterior. En lugar de descartar tus cambios con un `git reset --hard`, prefieres guardarlos en un stash por si los necesitas más tarde:*

```bash
# Guardar los cambios en un stash
git stash
```

```bash
# Reiniciar el directorio de trabajo al estado anterior
git reset --hard HEAD
```

**Luego, si decides que necesitas los cambios nuevamente, puedes aplicar el stash:**

```bash
# Aplicar el stash guardado
git stash apply
```

**Estos son solo algunos ejemplos de cómo puedes utilizar `git stash` para guardar temporalmente tus cambios mientras trabajas en Git. Es una herramienta muy útil para manejar situaciones donde necesitas cambiar de contexto rápidamente o donde deseas guardar tus cambios localmente antes de realizar ciertas operaciones.**
