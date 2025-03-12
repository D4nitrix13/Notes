<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Font Dotfiles***

- *This repository contains my font configurations for various applications and environments. These dotfiles allow me to maintain consistency in typographical appearance across all my systems and applications.*

---

## ***Usage***

1. *Clone this repository to your local machine.*
2. *Follow specific instructions within each subdirectory to install fonts in different environments.*
3. *Ensure you have installed necessary dependencies for each font configuration.*

---

## ***Contributions***

> *Contributions are welcome! If you have suggestions, corrections, or wish to add additional content to this guide, feel free to open an issue or pull request. Your help is crucial in making this guide a comprehensive and up-to-date reference for the development community.*

---

## ***License***

> *This repository is published under the MIT License. Feel free to use, modify, and distribute the content according to the terms of this license.*

---

## ***Recommended Fonts Page***

- **Coding Fonts:** *[Coding Fonts Page](https://coding-fonts.css-trickz.com/ "https://coding-fonts.css-trickz.com/")*

---

## ***Specific Fonts***

- **Tamago:** *[Tamago Page](https://alenlobeiras.com/projects/tamago "https://alenlobeiras.com/projects/tamago")*

- **Zelda (for games):** *[Zelda Font Page](https://www.fontspace.com/search?q=zelda "https://www.fontspace.com/search?q=zelda")*

---

## ***Useful Commands***

**To install all the recommended TTF and OTF fonts that are present in this repository into the system font directory (requires administrator permissions), run:**

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

**To list all font families available on your system, use the following command in the terminal:**

```bash
fc-list : family
```

**To update the font cache after adding new fonts to the system, use:**

```bash
fc-cache -fv
```

**If you want to specifically search for fonts containing "Cascadia" in the name, you can run (this applies to any font):**

```bash
fc-list | grep -iE "Cascadia" --color=auto
```
