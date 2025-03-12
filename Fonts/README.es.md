<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Dotfiles de Fuentes***

- *Este repositorio contiene mis configuraciones de fuentes para diferentes aplicaciones y entornos. Estos ficheros dotfiles me permiten mantener una consistencia en la apariencia tipográfica en todos mis sistemas y aplicaciones.*

## ***Uso***

1. *Clona este repositorio en tu máquina local.*
2. *Sigue las instrucciones específicas dentro de cada subdirectorio para instalar las fuentes en diferentes entornos.*
3. *Asegúrate de tener instaladas las dependencias necesarias para cada configuración de fuente.*

## ***Contribuciones***

> *¡Las contribuciones son bienvenidas! Si tienes sugerencias, correcciones o deseas agregar contenido adicional a esta guía, no dudes en abrir un problema o enviar una solicitud de extracción. Tu ayuda es fundamental para hacer de esta guía una referencia completa y actualizada para la comunidad de desarrollo.*

## ***Licencia***

> *Este repositorio se publica bajo la Licencia MIT. Siéntete libre de utilizar, modificar y distribuir el contenido de acuerdo con los términos de esta licencia.*

## ***Página de Fonts Recomendada***

- **Coding Fonts:** *[Página de Fonts Coding Fonts](https://coding-fonts.css-trickz.com/ "https://coding-fonts.css-trickz.com/")*

## ***Fuentes Específicas***

- **Tamago:** *[Página de Tamago](https://alenlobeiras.com/projects/tamago "https://alenlobeiras.com/projects/tamago")*

- **Zelda (para juegos):** *[Página de Zelda Font](https://www.fontspace.com/search?q=zelda "https://www.fontspace.com/search?q=zelda")*

## ***Comandos Útiles***

**Para instalar todas las fuentes TTF y OTF recomendadas que estan presentes en este repositorio en el directorio de fuentes del sistema (requiere permisos de administrador), ejecuta:**

```bash
cd ~/Descargas
# Agave
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Agave.zip"
# CascadiaCode
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/CascadiaCode.zip"
# DaddyTimeMono
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/DaddyTimeMono.zip"
# Hack
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip"
# Hurmit
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hermit.zip"
# Iosevka
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Iosevka.zip"
# JetBrains
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/JetBrainsMono.zip"
# Mononoki
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Mononoki.zip"
# UbuntuMono
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/UbuntuMono.zip"
# SpaceMono
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/SpaceMono.zip"
# VictorMono
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/VictorMono.zip"
# FiraCode
wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/FiraCode.zip"
unzip "*.zip" -d ~/Descargas
sudo mv ./*.ttf ./*.otf /usr/share/fonts/
rm *.zip
```

**Para listar todas las familias de fuentes disponibles en tu sistema, puedes usar el siguiente comando en la terminal:**

```bash
fc-list : family
```

**Para actualizar la caché de fuentes después de agregar nuevas fuentes al sistema, utiliza:**

```bash
fc-cache -fv
```

**Si deseas buscar específicamente las fuentes que contienen "Cascadia" en el nombre, puedes ejecutar (Esto aplica para cualquier fuente):**

```bash
fc-list | grep -iE "Cascadia" --color=auto
```
