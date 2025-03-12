<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***requirements.txt***

- *En Python3, el fichero `requirements.txt` es un estándar de la comunidad para gestionar las dependencias de un proyecto. Este fichero se utiliza para listar todas las bibliotecas y paquetes que son necesarios para ejecutar el proyecto, junto con sus versiones específicas. A continuación, se detalla la función y uso del fichero `requirements.txt`, así como la sintaxis válida con ejemplos.*

## ***¿Qué es `requirements.txt`?***

- *`requirements.txt` es un fichero de texto que contiene una lista de los paquetes de Python que tu proyecto necesita para funcionar correctamente. Este fichero permite que cualquier persona que trabaje en tu proyecto pueda instalar todas las dependencias de manera consistente y sencilla.*

### ***¿Para qué sirve `requirements.txt`?***

1. **Reproducibilidad:** *Permite que otros desarrolladores instalen exactamente las mismas versiones de las bibliotecas que usas, asegurando que el entorno de desarrollo sea idéntico en todas las máquinas.*

2. **Automatización:** *Facilita la instalación de todas las dependencias con un solo comando, lo que es útil para la automatización en procesos de integración continua y despliegue.*

3. **Mantenimiento:** *Ayuda a mantener un registro de las versiones de las bibliotecas utilizadas en el proyecto, facilitando la actualización y gestión de dependencias.*

### ***Casos de Uso***

1. **Configuración del Entorno de Desarrollo:** *Cuando un nuevo desarrollador clona tu repositorio, puede instalar todas las dependencias necesarias ejecutando `pip install -r requirements.txt`.*

2. **Despliegue de Aplicaciones:** *En entornos de producción, puedes usar `requirements.txt` para asegurar que el entorno de despliegue tenga las mismas versiones de bibliotecas que el entorno de desarrollo.*

3. **Documentación:** *Proporciona un registro claro y accesible de las dependencias del proyecto, lo que facilita la comprensión del stack tecnológico.*

### ***Sintaxis y Ejemplos***

- *La sintaxis de `requirements.txt` es bastante simple. Cada línea debe contener el nombre del paquete seguido de un símbolo de igualdad (`==`) y la versión específica del paquete. Aquí tienes ejemplos de cómo se puede estructurar un fichero `requirements.txt`:*

```txt
colored==2.2.4
mypy==1.10.0
pyinstaller==6.6.0
prettytable==3.10.2
toml==0.10.2
```

- **`colored==2.2.4`:** *Instala la versión `2.2.4` del paquete `colored`. Este paquete se usa para añadir color a las salidas de texto en la terminal.*
  
- **`mypy==1.10.0`:** *Instala la versión `1.10.0` del paquete `mypy`, una herramienta de comprobación de tipos estáticos para Python.*

- **`pyinstaller==6.6.0`:** *Instala la versión `6.6.0` del paquete `pyinstaller`, que se utiliza para convertir scripts Python en ejecutables independientes.*

- **`prettytable==3.10.2`:** *Instala la versión `3.10.2` del paquete `prettytable`, que se utiliza para generar tablas con formato bonito en texto plano.*

- **`toml==0.10.2`:** *Instala la versión `0.10.2` del paquete `toml`, que es una biblioteca para manejar ficheros TOML, un formato de fichero de configuración.*

### ***Cómo Crear un `requirements.txt`***

**Para crear un `requirements.txt` para tu proyecto, sigue estos pasos:**

1. **Instala las Dependencias:** *Asegúrate de tener todas las bibliotecas necesarias instaladas en tu entorno virtual.*

2. **Genera el Fichero:** *Usa el comando `pip freeze` para generar un fichero `requirements.txt` con todas las dependencias instaladas y sus versiones. Ejecuta:*

   ```bash
   pip freeze > requirements.txt
   ```

3. **Revisa y Modifica:** *Abre `requirements.txt` y revisa las dependencias listadas. Puedes agregar, eliminar o actualizar versiones según sea necesario.*

4. **Uso:** *Para instalar las dependencias listadas en `requirements.txt`, utiliza el siguiente comando:*

   ```bash
   pip install -r requirements.txt
   ```

### ***1. `pip freeze`***

- *`pip freeze` es un comando de `pip`, el gestor de paquetes de Python, que se utiliza para generar una lista de todas las bibliotecas instaladas en el entorno virtual actual, junto con sus versiones exactas. Esta lista se presenta en un formato que puede ser fácilmente utilizado para recrear el entorno en otro sistema.*

#### ***¿Para qué sirve?***

- **Reproducción del Entorno:** *Permite capturar el estado exacto de las bibliotecas instaladas en el entorno de desarrollo actual. Esta lista puede ser guardada en un fichero `requirements.txt` y utilizada para instalar las mismas versiones de las bibliotecas en otros entornos.*

- **Mantenimiento de Dependencias:** *Facilita el seguimiento de las versiones de las bibliotecas y la gestión de las dependencias del proyecto. Esto es útil cuando se trabaja en equipo o se despliega una aplicación en producción.*

#### ***Ejemplo de Uso***

**Cuando ejecutas:**

```bash
pip freeze
```

**Obtendrás una salida como la siguiente:**

```txt
colored==2.2.4
mypy==1.10.0
pyinstaller==6.6.0
prettytable==3.10.2
toml==0.10.2
```

**Esto muestra todas las bibliotecas instaladas en el entorno actual junto con sus versiones.**

### ***2. La Flag `-r`***

- *La flag `-r` en el comando `pip install` se utiliza para especificar que `pip` debe instalar las dependencias a partir de un fichero de requisitos. El fichero debe contener una lista de paquetes y versiones, como un fichero `requirements.txt`.*

#### ***¿Qué Significa?***

- **`-r` o `--requirement`:** *Esta flag le indica a `pip` que lea el fichero proporcionado y procese las dependencias listadas en él. `pip` instalará todas las bibliotecas y versiones especificadas en ese fichero.*

#### ***Ejemplo de Uso:***

**Cuando ejecutas:**

```bash
pip install -r requirements.txt
```

- *Esto hace que `pip` lea el fichero `requirements.txt`, que contiene una lista de bibliotecas y versiones, e instale esas dependencias en el entorno actual. Este comando es muy útil para configurar un entorno de desarrollo de manera rápida y consistente a partir de un fichero de requisitos previamente creado.*

### ***Resumen***

- **`pip freeze`:** *Genera una lista de todas las bibliotecas instaladas en el entorno actual junto con sus versiones exactas, útil para capturar el estado del entorno.*

- **`-r`:** *Es una flag utilizada con `pip install` para instalar todas las dependencias listadas en un fichero de requisitos, facilitando la configuración de entornos reproducibles.*

### ***Conclusión***

- *El fichero `requirements.txt` es una herramienta esencial para la gestión de dependencias en proyectos Python. Proporciona una forma estandarizada de definir las bibliotecas necesarias, garantiza la reproducibilidad del entorno de desarrollo y facilita el despliegue y mantenimiento de aplicaciones. La sintaxis es sencilla pero efectiva, y su uso correcto es clave para un flujo de trabajo de desarrollo eficiente y consistente.*
