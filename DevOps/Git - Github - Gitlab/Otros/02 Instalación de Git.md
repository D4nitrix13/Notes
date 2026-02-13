<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación de Git***

---

## ***Instalación en Windows***

1. *Descarga el instalador de Git desde [la página oficial de Git](https://git-scm.com/download/win "https://git-scm.com/download/win").*

2. *Ejecuta el fichero descargado y sigue las instrucciones del instalador.*

```bash
# No hay comandos de terminal necesarios para la instalación en Windows
```

---

## ***Instalación en macOS***

1. *Abre la Terminal.*

2. *Si tienes instalado Homebrew, puedes instalar Git con el siguiente comando:*

```bash
brew install git
```

*Si no tienes Homebrew, puedes instalarlo con el siguiente comando:*

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## ***Instalación en Linux***

1. *Abre la Terminal.*

   1. `<kbd>`Ctrl</kbd>+`<kbd>`Alt</kbd>+`<kbd>`t</kbd>
2. *Instalacion en distribución de Linux Ubuntu.*

**Para distribuciones basadas en Debian (como Ubuntu y Arch Linux):**

```bash
# Debian
sudo apt-get install git
```

```bash
# Arch Linux
sudo pacman -Syu git
```

> **Nota:** *Es posible que necesites introducir tu contraseña para autorizar la instalación.*

---

## ***Verificación de la instalación***

*Para verificar que Git se ha instalado correctamente, se usa el siguiente comando:*

```bash
git --version
```

> *Este comando debería devolver la versión de Git que has instalado.*

---

## ***Enlaces útiles***

- [*Documentación oficial de Git*](https://git-scm.com/doc "https://git-scm.com/doc")
