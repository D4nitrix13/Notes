<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Fichero De Configuracion `/opt/lampp/etc/my.cnf`***

```ini
# Example MySQL config file for medium systems.
#
# This is for a system with little memory (32M - 64M) where MySQL plays
# an important part, or systems up to 128M where MySQL is used together with
# other programs (such as a web server)
#
# You can copy this file to
# /etc/my.cnf to set global options,
# mysql-data-dir/my.cnf to set server-specific options (in this
# installation this directory is /opt/lampp/var/mysql) or
# ~/.my.cnf to set user-specific options.
#
# In this file, you can use all long options that a program supports.
# If you want to know which options a program supports, run the program
# with the "--help" option.

# The following options will be passed to all MySQL clients
[client]
#password = your_password
port  =3306
socket  =/opt/lampp/var/mysql/mysql.sock

# Here follows entries for some specific programs

# The MySQL server
default-character-set=utf8mb4
[mysqld]
user=mysql
port=3306
socket  =/opt/lampp/var/mysql/mysql.sock
key_buffer=16M
max_allowed_packet=1M
table_open_cache=64
sort_buffer_size=512K
net_buffer_length=8K
read_buffer_size=256K
read_rnd_buffer_size=512K
myisam_sort_buffer_size=8M

# Where do all the plugins live
plugin_dir=/opt/lampp/lib/mysql/plugin/

# Don't listen on a TCP/IP port at all. This can be a security enhancement,
# if all processes that need to connect to mysqld run on the same host.
# All interaction with mysqld must be made via Unix sockets or named pipes.
# Note that using this option without enabling named pipes on Windows
# (via the "enable-named-pipe" option) will render mysqld useless!
# 
#skip-networking

# Replication Master Server (default)
# binary logging is required for replication
# log-bin deactivated by default since XAMPP 1.4.11
#log-bin=mysql-bin

# required unique id between 1 and 2^32 - 1
# defaults to 1 if master-host is not set
# but will not function as a master if omitted
server-id =1

# Replication Slave (comment out master section to use this)
#
# To configure this host as a replication slave, you can choose between
# two methods :
#
# 1) Use the CHANGE MASTER TO command (fully described in our manual) -
#    the syntax is:
#
#    CHANGE MASTER TO MASTER_HOST=<host>, MASTER_PORT=<port>,
#    MASTER_USER=<user>, MASTER_PASSWORD=<password> ;
#
#    where you replace <host>, <user>, <password> by quoted strings and
#    <port> by the master's port number (3306 by default).
#
#    Example:
#
#    CHANGE MASTER TO MASTER_HOST='125.564.12.1', MASTER_PORT=3306,
#    MASTER_USER='joe', MASTER_PASSWORD='secret';
#
# OR
#
# 2) Set the variables below. However, in case you choose this method, then
#    start replication for the first time (even unsuccessfully, for example
#    if you mistyped the password in master-password and the slave fails to
#    connect), the slave will create a master.info file, and any later
#    change in this file to the variables' values below will be ignored and
#    overridden by the content of the master.info file, unless you shutdown
#    the slave server, delete master.info and restart the slaver server.
#    For that reason, you may want to leave the lines below untouched
#    (commented) and instead use CHANGE MASTER TO (see above)
#
# required unique id between 2 and 2^32 - 1
# (and different from the master)
# defaults to 2 if master-host is set
# but will not function as a slave if omitted
#server-id       = 2
#
# The replication master for this slave - required
#master-host     =   <hostname>
#
# The username the slave will use for authentication when connecting
# to the master - required
#master-user     =   <username>
#
# The password the slave will authenticate with when connecting to
# the master - required
#master-password =   <password>
#
# The port the master is listening on.
# optional - defaults to 3306
#master-port     =  <port>
#
# binary logging - not required for slaves, but recommended
#log-bin=mysql-bin


# Point the following paths to different dedicated disks
#tmpdir  = /tmp/  
#log-update  = /path-to-dedicated-directory/hostname

# Uncomment the following if you are using BDB tables
#bdb_cache_size = 4M
#bdb_max_lock = 10000

# Comment the following if you are using InnoDB tables
#skip-innodb
innodb_data_home_dir=/opt/lampp/var/mysql/
innodb_data_file_path=ibdata1:10M:autoextend
innodb_log_group_home_dir=/opt/lampp/var/mysql/
# You can set .._buffer_pool_size up to 50 - 80 %
# of RAM but beware of setting memory usage too high
innodb_buffer_pool_size=16M
# Deprecated in 5.6
#innodb_additional_mem_pool_size = 2M
# Set .._log_file_size to 25 % of buffer pool size
innodb_log_file_size=5M
innodb_log_buffer_size=8M
innodb_flush_log_at_trx_commit=1
innodb_lock_wait_timeout=50

character-set-server=utf8mb4
collation-server=utf8mb4_general_ci
[mysqldump]
max_allowed_packet=16M

[mysql]
# Remove the next comment character if you are not familiar with SQL
#safe-updates

[isamchk]
key_buffer=20M
sort_buffer_size=20M
read_buffer=2M
write_buffer=2M

[myisamchk]
key_buffer=20M
sort_buffer_size=20M
read_buffer=2M
write_buffer=2M

[mysqlhotcopy]
```

> [!TIP]
> *Para configurar MySQL para que escuche en una IP específica (como 172.17.0.2) y en un puerto diferente, debes modificar el fichero de configuración de MySQL. Como estás usando XAMPP (LAMPP) en Linux, puedes seguir estos pasos:*

- **Editar el fichero de configuración de MySQL (my.cnf):**
- *Abre el fichero de configuración de MySQL. Usualmente se encuentra en /opt/lampp/etc/my.cnf. Para editarlo, usa un editor de texto como nano:*

```ini
sudo nano /opt/lampp/etc/my.cnf
```

- **Configurar la IP y el puerto:**

- *Busca la sección [mysqld].*

- **Para que MySQL escuche en la IP 172.17.0.2, agrega o modifica la línea bind-address:**

```ini
bind-address = 172.17.0.2
```

- **Para cambiar el puerto, busca la línea port (si no está presente, agrégala) y establece el puerto deseado:**

```ini
port = 3306  # Otro Port
```

- **El fichero debería verse algo así:**

```ini
[mysqld]
bind-address = 172.17.0.2
port = 3306
```

**Reiniciar MySQL:**

- **Después de guardar los cambios, necesitas reiniciar el servidor MySQL para que los cambios surtan efecto. Puedes hacerlo ejecutando:**

```bash
sudo /opt/lampp/lampp restart
```

- **File Complete**

```ini
# Example MySQL config file for medium systems.
#
# This is for a system with little memory (32M - 64M) where MySQL plays
# an important part, or systems up to 128M where MySQL is used together with
# other programs (such as a web server)
#
# You can copy this file to
# /etc/my.cnf to set global options,
# mysql-data-dir/my.cnf to set server-specific options (in this
# installation this directory is /opt/lampp/var/mysql) or
# ~/.my.cnf to set user-specific options.
#
# In this file, you can use all long options that a program supports.
# If you want to know which options a program supports, run the program
# with the "--help" option.

# The following options will be passed to all MySQL clients
[client]
#password = your_password
port  =3306
socket  =/opt/lampp/var/mysql/mysql.sock

# Here follows entries for some specific programs

# The MySQL server
default-character-set=utf8mb4
[mysqld]
user=mysql
port=3306
# MySQL Listen IPv4 Example Value (localhost, 127.0.0.1, 192.168.1.17, 172.17.0.2)
bind-address = 172.17.0.2
socket  =/opt/lampp/var/mysql/mysql.sock
key_buffer=16M
max_allowed_packet=1M
table_open_cache=64
sort_buffer_size=512K
net_buffer_length=8K
read_buffer_size=256K
read_rnd_buffer_size=512K
myisam_sort_buffer_size=8M

# Where do all the plugins live
plugin_dir=/opt/lampp/lib/mysql/plugin/

# Don't listen on a TCP/IP port at all. This can be a security enhancement,
# if all processes that need to connect to mysqld run on the same host.
# All interaction with mysqld must be made via Unix sockets or named pipes.
# Note that using this option without enabling named pipes on Windows
# (via the "enable-named-pipe" option) will render mysqld useless!
# 
#skip-networking

# Replication Master Server (default)
# binary logging is required for replication
# log-bin deactivated by default since XAMPP 1.4.11
#log-bin=mysql-bin

# required unique id between 1 and 2^32 - 1
# defaults to 1 if master-host is not set
# but will not function as a master if omitted
server-id =1

# Replication Slave (comment out master section to use this)
#
# To configure this host as a replication slave, you can choose between
# two methods :
#
# 1) Use the CHANGE MASTER TO command (fully described in our manual) -
#    the syntax is:
#
#    CHANGE MASTER TO MASTER_HOST=<host>, MASTER_PORT=<port>,
#    MASTER_USER=<user>, MASTER_PASSWORD=<password> ;
#
#    where you replace <host>, <user>, <password> by quoted strings and
#    <port> by the master's port number (3306 by default).
#
#    Example:
#
#    CHANGE MASTER TO MASTER_HOST='125.564.12.1', MASTER_PORT=3306,
#    MASTER_USER='joe', MASTER_PASSWORD='secret';
#
# OR
#
# 2) Set the variables below. However, in case you choose this method, then
#    start replication for the first time (even unsuccessfully, for example
#    if you mistyped the password in master-password and the slave fails to
#    connect), the slave will create a master.info file, and any later
#    change in this file to the variables' values below will be ignored and
#    overridden by the content of the master.info file, unless you shutdown
#    the slave server, delete master.info and restart the slaver server.
#    For that reason, you may want to leave the lines below untouched
#    (commented) and instead use CHANGE MASTER TO (see above)
#
# required unique id between 2 and 2^32 - 1
# (and different from the master)
# defaults to 2 if master-host is set
# but will not function as a slave if omitted
#server-id       = 2
#
# The replication master for this slave - required
#master-host     =   <hostname>
#
# The username the slave will use for authentication when connecting
# to the master - required
#master-user     =   <username>
#
# The password the slave will authenticate with when connecting to
# the master - required
#master-password =   <password>
#
# The port the master is listening on.
# optional - defaults to 3306
#master-port     =  <port>
#
# binary logging - not required for slaves, but recommended
#log-bin=mysql-bin


# Point the following paths to different dedicated disks
#tmpdir  = /tmp/  
#log-update  = /path-to-dedicated-directory/hostname

# Uncomment the following if you are using BDB tables
#bdb_cache_size = 4M
#bdb_max_lock = 10000

# Comment the following if you are using InnoDB tables
#skip-innodb
innodb_data_home_dir=/opt/lampp/var/mysql/
innodb_data_file_path=ibdata1:10M:autoextend
innodb_log_group_home_dir=/opt/lampp/var/mysql/
# You can set .._buffer_pool_size up to 50 - 80 %
# of RAM but beware of setting memory usage too high
innodb_buffer_pool_size=16M
# Deprecated in 5.6
#innodb_additional_mem_pool_size = 2M
# Set .._log_file_size to 25 % of buffer pool size
innodb_log_file_size=5M
innodb_log_buffer_size=8M
innodb_flush_log_at_trx_commit=1
innodb_lock_wait_timeout=50

character-set-server=utf8mb4
collation-server=utf8mb4_general_ci
[mysqldump]
max_allowed_packet=16M

[mysql]
# Remove the next comment character if you are not familiar with SQL
#safe-updates

[isamchk]
key_buffer=20M
sort_buffer_size=20M
read_buffer=2M
write_buffer=2M

[myisamchk]
key_buffer=20M
sort_buffer_size=20M
read_buffer=2M
write_buffer=2M

[mysqlhotcopy]
```

- **Esto le dará al usuario root acceso desde cualquier dirección IP (el `%` representa cualquier IP).**

```sql
CREATE USER 'root'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

- **CREATE USER: Esta sentencia se utiliza para crear un nuevo usuario.**
  - *`'root'@'%'`: `'root'` es el nombre del usuario que se está creando, y `'%'` significa que el usuario puede conectarse desde cualquier host o dirección IP.*
  - *`IDENTIFIED BY ''`: El usuario `'root'` se crea sin una contraseña, lo que significa que no hay autenticación mediante contraseña configurada para este usuario. Esto se indica con una cadena vacía ''.*

- **`GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;`**
  - *GRANT ALL PRIVILEGES: Esta sentencia otorga todos los privilegios disponibles en la base de datos al usuario.*
  - *ON `*.*`: El usuario 'root' recibe estos privilegios sobre todas las bases de datos y todas las tablas, representado por *.*. El primer *representa todas las bases de datos y el segundo* representa todas las tablas dentro de esas bases de datos.*
  - *`TO 'root'@'%'`: Se especifica que estos privilegios se asignan al usuario 'root' que puede conectarse desde cualquier host (indicado por '%').*
  - *`WITH GRANT OPTION`: Esto permite que el usuario 'root' también pueda otorgar estos privilegios a otros usuarios. Es una opción adicional que le da al usuario 'root' la capacidad de gestionar los privilegios de otros usuarios.*

- **`FLUSH PRIVILEGES;`**
  - *Esta sentencia aplica y recarga las tablas de privilegios en el servidor de base de datos para que los cambios realizados (crear el usuario y otorgar privilegios) tengan efecto inmediato.*

- **IPv4 -> `172.17.0.2`**

```sql
CREATE USER 'root'@'172.17.0.2' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'172.17.0.2' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

- *Primera sentencia ('%'): El usuario 'root' tiene acceso desde cualquier dirección IP.*
- *Segunda sentencia ('172.17.0.2'): El usuario 'root' tiene acceso solo desde la IP específica 172.17.0.2.*

- **Ambos bloques crean un usuario sin contraseña (aunque es inseguro), otorgan privilegios completos sobre todas las bases de datos y permiten que el usuario otorgue esos privilegios a otros usuarios. Finalmente, ambos bloques usan FLUSH PRIVILEGES para hacer efectivos los cambios.**
