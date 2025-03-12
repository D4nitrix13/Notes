<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Modulo de antivirus***

*`Url de las paginas web que utilize en este modulo`*

1. [***av-test***](https://www.av-test.org/es/ "https://www.av-test.org/es/")

2. [***av-comparatives***](https://www.av-comparatives.org/consumer/ "https://www.av-comparatives.org/consumer/")

3. [***virustotal***](https://www.virustotal.com/gui/home/upload "https://www.virustotal.com/gui/home/upload")

4. [***hybrid-analysis***](https://www.hybrid-analysis.com/?lang=es "https://www.hybrid-analysis.com/?lang=es")

5. [***malwarebytes***](https://www.malwarebytes.com/ "https://www.malwarebytes.com/")

6. [***kaspersky***](https://www.kaspersky.es/resource-center/threats/what-is-a-security-breach "https://www.kaspersky.es/resource-center/threats/what-is-a-security-breach")

7. [***haveibeenpwned***](https://haveibeenpwned.com/ "https://haveibeenpwned.com/")

> [!IMPORTANT]
> *La pagina de Hybrid Analytics cuando hace un escaneo de los ficheros que subamos, luego de hacer el analisis el documento lo hace publico asi que no subamos ficheros confidenciales por que si no se puede filtrar informacion personal*

---

## ***Firewall***

*Un firewall, en español "cortafuegos", es un componente de seguridad informática que se utiliza para monitorear y controlar el tráfico de red, permitiendo o bloqueando la comunicación según un conjunto de reglas predefinidas. Su objetivo principal es proteger una red o un sistema informático de amenazas externas, como accesos no autorizados, malware y otros tipos de ataques.*

*Existen firewalls tanto a nivel de hardware como a nivel de software, y a menudo se utilizan en combinación para proporcionar una seguridad más completa. Los firewalls pueden operar en diferentes capas del modelo OSI (modelo de interconexión de sistemas abiertos) y pueden implementarse en dispositivos como routers, switches, servidores y computadoras personales.*

> **Las funciones principales de un firewall incluyen:**

1. **Filtrado de paquetes:** *Examina los datos que entran y salen de la red y bloquea o permite el paso según las reglas establecidas.*

2. **Control de acceso:** *Define quién tiene permiso para acceder a la red o a determinados recursos dentro de la red.*

3. **Registro de actividades:** *Lleva un registro de las actividades de red, lo que facilita la identificación de posibles amenazas o patrones de comportamiento sospechoso.*

4. **Proxy:** *Actúa como intermediario entre los usuarios y los recursos de la red, ocultando información sobre la red interna y proporcionando una capa adicional de seguridad.*

5. **Inspección de estado:** *Realiza un seguimiento del estado de las conexiones de red y permite o bloquea el tráfico basándose en el estado de la conexión.*

*La implementación de firewalls es una práctica común en la seguridad de redes para proteger la integridad y la confidencialidad de la información, así como para prevenir ataques cibernéticos.*

1. ***Permisos permisivos:***

   - *Los permisos permisivos se refieren a la configuración de un firewall que permite el tráfico por defecto, a menos que esté específicamente prohibido por las reglas establecidas.*

   - *En un enfoque permisivo, el firewall permite que todos los datos atraviesen a menos que se detecte una amenaza o una violación de las reglas establecidas.*

   - *Este enfoque puede ser más flexible, pero también puede ser menos seguro si no se configura adecuadamente, ya que cualquier tráfico no autorizado podría pasar desapercibido.*

2. ***Política de "drop":***

   - *La política de "drop" es un enfoque más restrictivo en el que el firewall bloquea todo el tráfico por defecto, a menos que esté específicamente permitido por las reglas.*
  
   - *En este caso, se deniega el acceso a menos que se haya establecido una regla explícita que permita el tráfico desde una fuente específica hacia un destino específico.*

   - *Este enfoque es más seguro por naturaleza, ya que adopta un enfoque más restrictivo y requiere una configuración explícita para permitir el tráfico.*

   - *La elección entre un enfoque permisivo y una política de "drop" depende de los requisitos de seguridad y las necesidades específicas de la red o del sistema. En entornos donde la seguridad es la máxima prioridad, la política de "drop" suele ser preferida, ya que sigue el principio de permitir solo lo que es necesario y bloquear todo lo demás.*

## ***Configurar el programador de tareas para hacer un escaneo del dispositivo en windows***

1. [***Programar tu propio examen windows defender***](https://support.microsoft.com/es-es/topic/programar-un-examen-en-el-antivirus-de-microsoft-defender-54b64e9c-880a-c6b6-2416-0eb330ed5d2d "https://support.microsoft.com/es-es/topic/programar-un-examen-en-el-antivirus-de-microsoft-defender-54b64e9c-880a-c6b6-2416-0eb330ed5d2d")

2. [***Configurar Firewall Windows***](#configurar-firewall-windows)

## ***Configurar-Firewall-Windows***

*Busca `<kbd>` **Firewall**`</kbd>`  en la barra de busqueda de Windows luego ve a configuraciones avanzadas luego selecciones reglas de salida, crear nueva regla, darle click ala opcion del programa luego dar la ruta absoluta del programa que queremos configurar con el firewall luego segun lo que queramos hacer con el programa podemos bloquear la conexion y permitir la conexion luego configuramos para que el firewall aplique sobre esto 3 aspectos que son: Dominio, Privado, Publico, luego de eso ponerle un nombre ala regla y una breve descripcion y listo. Podemos activar y desactivar la regla cuando queramos*

---

## ***Comando Powershell***

> **Comando PowerShell:** *Set-MpPreference -DisableRemovableDriveScanning 0*

```powershell
Set-MpPreference -DisableRemovableDriveScanning 0
```

*El comando PowerShell "Set-MpPreference -DisableRemovableDriveScanning 0" se utiliza para habilitar el escaneo de unidades extraíbles en Windows Defender. Al establecer el valor en "0", se permite que Windows Defender escanee dispositivos de almacenamiento extraíbles como unidades flash USB, discos duros externos y tarjetas de memoria SD en busca de posibles amenazas de seguridad. Si se establece en "1", se deshabilita el escaneo de unidades extraíbles.*
