<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Git y GitHub "flow"***

- *El "Git Flow" es un flujo de trabajo popular para el desarrollo de software con Git, diseñado para ser un marco flexible y robusto que facilite la colaboración en equipos de desarrollo. Aquí tienes una descripción general del Git Flow:*

1. **Ramas Principales:**

   - **`main`* (o `master`):** *Esta es la rama principal del repositorio, que refleja la producción estable del proyecto.*

   - **`develop`:** *Esta es la rama de desarrollo donde se integran todos los cambios que se realizan en el proyecto. Es una rama "inestable" donde se pueden probar nuevas características antes de ser fusionadas en la rama principal.*

2. **Ramas de Características:**

   - **`feature`:** *Las ramas de características se crean a partir de `develop` y se utilizan para implementar nuevas características o funcionalidades. Después de completar una característica, se fusiona de nuevo en `develop`.*

3. **Ramas de Lanzamiento:**

   - **`release`:** *Las ramas de lanzamiento se crean a partir de `develop` cuando el desarrollo en esa rama alcanza un punto en el que está lista para ser lanzada. Se pueden realizar pequeñas correcciones en esta rama, como correcciones de errores o ajustes de versión, antes de fusionarla en `main` y `develop`.*

4. **Ramas de Corrección de Errores:**

   - **`hotfix`:** *Las ramas de corrección de errores se crean a partir de `main` y se utilizan para solucionar rápidamente problemas críticos en producción. Una vez que se corrige el error, se fusiona tanto en `main` como en `develop`.*

- *El flujo de trabajo Git Flow facilita la colaboración en equipo y la gestión de versiones en proyectos de desarrollo de software. Sin embargo, es importante tener en cuenta que Git Flow puede ser un poco complejo y puede no ser adecuado para todos los proyectos. En los últimos años, han surgido otros enfoques de flujo de trabajo, como el "GitHub Flow" y el "GitLab Flow", que son más simplificados y se centran en un flujo de trabajo continuo y basado en la implementación continua (CI/CD). Estos enfoques pueden ser más adecuados para proyectos más ágiles y orientados al desarrollo web.*
