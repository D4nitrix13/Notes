<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***GNU Make es una herramienta de construcción ampliamente utilizada en sistemas Unix y Linux. Su función principal es automatizar el proceso de compilación de programas y otros conjuntos de ficheros cuando se desarrollan proyectos de software. Aquí tienes información detallada sobre GNU Make:***

## ***Funciones Principales***

1. **Automatización de Tareas:** *Make simplifica y automatiza el proceso de compilación mediante reglas definidas en un fichero llamado `Makefile`.*

2. **Gestión de Dependencias:** *Determina automáticamente qué partes del proyecto necesitan ser reconstruidas según las modificaciones realizadas en los ficheros fuente.*

3. **Optimización de Tiempos de Compilación:** *Permite compilar solo los ficheros modificados y sus dependencias, lo que ahorra tiempo en comparación con compilar todo el proyecto desde cero.*

### ***Instalación en Ubuntu***

**En Ubuntu, puedes instalar GNU Make utilizando el gestor de paquetes `apt`:**

```bash
sudo apt update
sudo apt install -y make
```

**Esto instalará GNU Make y sus dependencias necesarias en tu sistema.**

### ***Instalación en Arch Linux***

**En Arch Linux, puedes instalar GNU Make utilizando `pacman`, el gestor de paquetes oficial:**

```bash
sudo pacman -Syu --noconfirm make
```

### ***Características***

- **Flexibilidad:** *Permite definir reglas personalizadas y secuencias de comandos para cualquier proceso de compilación.*
- **Portabilidad:** *Es compatible con una amplia variedad de sistemas Unix y Linux.*
- **Eficiencia:** *Ayuda a optimizar el flujo de trabajo al minimizar la compilación de ficheros no modificados.*
- **Ampliamente Utilizado:** *Es una herramienta estándar en el desarrollo de software y está bien soportada por la comunidad y la documentación.*

*GNU Make es esencial para proyectos de software que implican varios ficheros y dependencias, facilitando la gestión de compilación y asegurando un proceso más eficiente y controlado.*
