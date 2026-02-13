<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación de Oh-My-Tmux***

**Indices:**

- [***Instalación de Oh-My-Tmux***](#instalación-de-oh-my-tmux)
- [***Prerrequisitos***](#prerrequisitos)
  - [***Paso 1: Clonar el repositorio***](#paso-1-clonar-el-repositorio)
    - [***Paso 2: Enlazar el fichero de configuración***](#paso-2-enlazar-el-fichero-de-configuración)
      - [***Paso 3: Copiar el fichero local de configuración***](#paso-3-copiar-el-fichero-local-de-configuración)
      - [***Uso***](#uso)

> *Oh-My-Tmux es un marco de configuración para tmux que mejora su interfaz y usabilidad. Sigue estos pasos para instalarlo:*

---

# ***Prerrequisitos***

> *Antes de instalar Oh-My-Tmux, necesitas tener tmux instalado en tu sistema. Aquí te mostramos cómo hacerlo en Debian/Ubuntu y MacOS:*

```bash
# Debian/Ubuntu
sudo apt-get -y install tmux
```

```bash
# Arch Linux
sudo pacman -Syu --noconfirm tmux
```

```bash
# MacOS
brew install tmux
```

***Instalación***

---

## ***Paso 1: Clonar el repositorio***

**Clona el repositorio de Oh-My-Tmux en tu directorio de inicio con el siguiente comando:**

```bash
cd ~/
```

```bash
git clone https://github.com/gpakosz/.tmux.git --depth=1
```

### ***Paso 2: Enlazar el fichero de configuración***

> *Enlaza el fichero de configuración de tmux proporcionado por Oh-My-Tmux:*

```bash
ln -sf .tmux/.tmux.conf
```

```bash
ln -s -f .tmux/.tmux.conf
```

```bash
ln --symbolic --force .tmux/.tmux.conf
```

```bash
ln -s --force .tmux/.tmux.conf
```

```bash
ln --symbolic -f .tmux/.tmux.conf
```

- *El comando `ln -s -f` se utiliza para crear un enlace simbólico a un fichero o directorio. La opción `-s` significa "simbólico" y `-f` significa "forzar". En su forma no abreviada, el comando sería `ln --symbolic --force`.*

- *El comando `ln -s -f .tmux/.tmux.conf` crea un enlace simbólico en el directorio actual que apunta al fichero `.tmux.conf` en el directorio `.tmux`. Si ya existe un fichero llamado `.tmux.conf` en el directorio actual, la opción `--force` hace que `ln` lo sobrescriba.*

---

#### ***Paso 3: Copiar el fichero local de configuración***

> *Copia el fichero `.tmux.conf.local` en tu directorio de inicio o `/home`. Este fichero te permite personalizar tu configuración de tmux:*

```bash
cp .tmux/.tmux.conf.local .
```

```bash
cp ./.tmux/.tmux.conf.local ./
```

```bash
cp ~/.tmux/.tmux.conf.local ~/
```

---

#### ***Uso***

- *Inicia una nueva sesión de tmux y deberías ver la nueva configuración. Si ya tienes una sesión de tmux abierta, puedes recargar la configuración con el siguiente comando:*

```bash
tmux source-file ~/.tmux.conf
```
