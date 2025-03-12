<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Ejemplo Gitflow***

- *Gitflow es un modelo de flujo de trabajo popular para el control de versiones con Git que define una estructura de ramificación y una serie de reglas para administrar el ciclo de vida del desarrollo de software. Aquí tienes un ejemplo básico de cómo se vería el flujo de trabajo Gitflow en un proyecto:*

---

## ***Ramas Principales:***

1. **`master`:** *La rama `master` contiene el código estable y listo para ser desplegado en producción. Los commits en esta rama representan versiones de lanzamiento.*

2. **`develop`:** *La rama `develop` es donde se integran todos los cambios de las diferentes funcionalidades del equipo. Esta rama siempre debe estar lista para ser desplegada en un entorno de pruebas.*

---

### ***Ramas de Funcionalidad:***

1. **`feature/<nombre>`:** *Las ramas `feature` se utilizan para desarrollar nuevas funcionalidades. Estas ramas se ramifican desde `develop` y se fusionan nuevamente en `develop` una vez que la funcionalidad está completa.*

   **Ejemplo:**

   ```bash
   git checkout develop
   git checkout -b feature/nueva-funcionalidad
   # Trabaja en la nueva funcionalidad y realiza commits
   git checkout develop
   git merge --no-ff feature/nueva-funcionalidad
   git branch -d feature/nueva-funcionalidad
   ```

---

### ***Ramas de Lanzamiento:***

1. **`release/<versión>`:** *Las ramas `release` se utilizan para preparar una nueva versión para el lanzamiento. Estas ramas se ramifican desde `develop` y se fusionan tanto en `develop` como en `master` una vez que la versión está lista para ser lanzada.*

   **Ejemplo:**

   ```bash
   git checkout develop
   ```

   ```bash
   git checkout -b release/1.0.0
   # Realiza pruebas, correcciones de errores y ajustes finales
   ```

   ```bash
   git checkout master
   ```

   ```bash
   git merge --no-ff release/1.0.0
   ```

   ```bash
   git tag -a 1.0.0 -m "Versión 1.0.0"
   ```

   ```bash
   git checkout develop
   ```

   ```bash
   git merge --no-ff release/1.0.0
   ```

   ```bash
   git branch -d release/1.0.0
   ```

---

### ***Ramas de Corrección de Errores (Hotfix):***

1. **`hotfix/<nombre>`:** *Las ramas `hotfix` se utilizan para corregir problemas críticos en producción. Estas ramas se ramifican desde `master`, se aplican los cambios necesarios y se fusionan tanto en `master` como en `develop`.*

   **Ejemplo:**

   ```bash
   git checkout master
   ```

   ```bash
   git checkout -b hotfix/fix-issue
   # Corrige el problema y realiza commits
   ```

   ```bash
   git checkout master
   ```

   ```bash
   git merge --no-ff hotfix/fix-issue
   ```

   ```bash
   git tag -a 1.0.1 -m "Versión 1.0.1"
   ```

   ```bash
   git checkout develop
   ```

   ```bash
   git merge --no-ff hotfix/fix-issue
   ```

   ```bash
   git branch -d hotfix/fix-issue
   ```

- *Este es solo un ejemplo básico de cómo se podría implementar el flujo de trabajo Gitflow en un proyecto. Es importante adaptar este modelo a las necesidades específicas y la estructura de tu equipo y proyecto.*
