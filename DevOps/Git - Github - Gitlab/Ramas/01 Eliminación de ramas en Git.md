<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Eliminación de ramas en Git"***

> *La eliminación de ramas en Git es una operación común para limpiar el historial del repositorio después de que una rama ya no sea necesaria. Aquí tienes algunos métodos para eliminar ramas en Git:*

---

## ***Eliminar una rama local:***

1. ***Eliminar una rama que ya se ha fusionado:***

   **Si has terminado de trabajar en una rama y ya has fusionado sus cambios en otra rama (por ejemplo, `main`), puedes eliminarla de la siguiente manera:**

   ```bash
   git branch -d <nombre_rama>
   ```

   **Por ejemplo, para eliminar una rama llamada `mi-rama`:**

   ```bash
   git branch -d mi-rama
   ```

   *El flag `-d` es para "delete" (eliminar) y Git solo permitirá eliminar la rama si todos sus cambios ya están fusionados en otra rama.*

2. ***Eliminar una rama aunque no esté fusionada:***

   **Si deseas eliminar una rama sin importar si sus cambios están fusionados o no, puedes utilizar:**

   ```bash
   git branch -D <nombre_rama>
   ```

   **Por ejemplo:**

   ```bash
   git branch -D mi-rama
   ```

   *La opción `-D` fuerza la eliminación de la rama, incluso si hay cambios que no se han fusionado.*

---

### ***Eliminar una rama remota:***

1. ***Eliminar una rama remota:***

   *Si deseas eliminar una rama en el repositorio remoto, puedes utilizar:*

   ```bash
   git push <repositorio_remoto> --delete <nombre_rama>
   ```

   **Por ejemplo, para eliminar una rama llamada `mi-rama` en el repositorio remoto `origin`:**

   ```bash
   git push origin --delete mi-rama
   ```

   *Esto eliminará la rama del repositorio remoto y la próxima vez que alguien obtenga cambios del repositorio remoto, esa rama ya no estará presente.*

*Recuerda tener cuidado al eliminar ramas, especialmente las que no están fusionadas. Asegúrate de que estás eliminando la rama correcta y de que ya no necesitas sus cambios antes de ejecutar el comando de eliminación.*
