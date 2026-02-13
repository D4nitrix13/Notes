<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# Gestor de Paquetes de Lua: Instalación con Gestor de Paquetes APT

*Este markdown proporciona instrucciones para instalar el gestor de paquetes de Lua y el framework de desarrollo Love2D en sistemas basados en Debian/Ubuntu utilizando el gestor de paquetes APT.*

## Paso 1: Instalar LuaRocks

*Para instalar `LuaRocks`, el gestor de paquetes de Lua, ejecuta el siguiente comando en tu terminal:*

```bash
sudo apt-get install luarocks
```

### Paso 2: Agregar el Repositorio de Love2D

*`Love2D` es un framework de desarrollo de juegos en Lua. Agrega el repositorio PPA de 'Love2D' ejecutando el siguiente comando:*

```bash
sudo add-apt-repository ppa:bartbes/love-stable
```

### Paso 3: Instalar Love2D

*Luego de agregar el repositorio, puedes instalar 'Love2D' con el siguiente comando:*

```bash
sudo apt-get install love
```

### Paso 4: Ejecutar una Aplicación Love2D

*Una vez instalado 'Love2D', puedes ejecutar una aplicación 'Love2D' (generalmente una directorio que contiene el código del juego) con el siguiente comando:*

```bash
love ./
```

*Este comando ejecutará la aplicación Love2D en la directorio actual.*

---

> [!NOTE]
> *Esta documentación proporciona instrucciones claras y concisas para instalar LuaRocks y Love2D utilizando el gestor de paquetes APT en sistemas basados en Debian/Ubuntu. Cada paso está detalladamente explicado junto con los comandos necesarios.*
