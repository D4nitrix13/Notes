<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Descargar Comprimido***

*Este markdown proporciona una serie de comandos de terminal para descargar, descomprimir, compilar e instalar un programa llamado `srlua` en sistemas basados en Linux.*

## ***Paso 1: Descargar el Fichero Comprimido***

*Para descargar el fichero comprimido que contiene el programa `srlua`, ejecuta el siguiente comando en tu terminal:*

```bash
wget https://web.tecgraf.puc-rio.br/~lhf/ftp/lua/ar/srlua-102.tar.gz
```

### ***Paso 2: Descomprimir el Fichero***

*Descomprime el fichero descargado con el siguiente comando:*

```bash
tar -xzvf srlua-102.tar.gz
```

### ***Paso 3: Navegar al Directorio***

*Dirígete al directorio recién creado con el siguiente comando:*

```bash
cd srlua-102/
```

### ***Paso 4: Verificar el Contenido del Directorio***

*Muestra el contenido del directorio actual con el siguiente comando:*

```bash
ls
```

### ***Paso 5: Buscar Intérpretes de Lua***

*Busca intérpretes de Lua disponibles en tu sistema con el siguiente comando:*

```bash
find /usr/lib/x86_64-linux-gnu/ -name "liblua*.so"
```

### ***Paso 6: Compilar srlua***

*Compila el programa `srlua` con el siguiente comando:*

```bash
gcc -std=c99 -Wall -Wextra -Wfatal-errors -O2 -o srlua srlua.c -I/usr/include/lua5.2 -L/usr/lib/x86_64-linux-gnu/ -llua5.2 -lm -ldl -Wl,-E
```

### ***Paso 7: Compilar srglue***

*Compila el programa `srglue` con el siguiente comando:*

```bash
gcc -std=c99 -Wall -Wextra -Wfatal-errors -O2 -o srglue srglue.c
```

### ***Paso 8: Instalar Paquete Necesario***

*Instala el paquete de desarrollo de Lua 5.2 con el siguiente comando:*

```bash
sudo apt-get install liblua5.2-dev
```

### ***Paso 9: Verificar el Nuevo Contenido del Directorio***

*Muestra el contenido actualizado del directorio con el siguiente comando:*

```bash
ls
```

### ***Paso 10: Ejecutar el Binario***

*Ejecuta el binario `srglue` seguido de los ficheros de entrada y salida con el siguiente comando:*

```bash
./srglue srlua ../index.lua ../main
```

### ***Paso 11: Agregar al PATH***

*Para agregar los programas `srlua` y `srglue` al PATH del sistema, ejecuta el siguiente comando con `sudo`:*

```bash
sudo make install
```

*Después de ejecutar este comando, podrás ejecutar `srlua` y `srglue` desde cualquier ubicación en tu sistema.*

```bash
srglue srlua ./index.lua ./main
```

---

> [!NOTE]
> *Esta documentación proporciona instrucciones claras y detalladas para descargar, compilar e instalar el programa `srlua` en sistemas basados en Linux. Cada paso está explicado y acompañado de los comandos necesarios para realizar la tarea correspondiente.*
