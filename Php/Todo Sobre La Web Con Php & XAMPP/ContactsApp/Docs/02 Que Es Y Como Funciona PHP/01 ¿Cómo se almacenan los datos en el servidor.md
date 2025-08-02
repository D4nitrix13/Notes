<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# **¿Cómo se almacenan los datos en el servidor?**

- *El almacenamiento de datos en un servidor web es un proceso en el cual el servidor recibe datos del cliente (por ejemplo, a través de un formulario HTML) y luego almacena esos datos en un fichero, base de datos o cualquier otro sistema de almacenamiento. En este caso, se está tratando con un script PHP que intenta guardar datos en un fichero `contacts.json`. Sin embargo, el proceso está fallando debido a un problema de permisos en el sistema de ficheros del servidor.*

## **Logs del Servidor**

- *Cuando un servidor web (en este caso, un servidor PHP corriendo sobre Apache) encuentra un problema al intentar realizar una operación, como escribir en un fichero, este error se registra en los logs de error. El servidor tiene una serie de ficheros log en los que se almacenan los eventos, advertencias y errores ocurridos durante su ejecución.*

- **En los logs proporcionados, tenemos varias entradas en el fichero `php_error_log`:**

```bash
lsd -lA /opt/lampp/logs/
.rw-r--r-- daemon daemon  25 KB Sun Dec 15 22:45:18 2024  access_log
srwx------ daemon root     0 B  Sun Dec 15 22:40:53 2024 󰆨 cgisock.10828
srwx------ daemon root     0 B  Thu Dec 12 16:42:43 2024 󰆨 cgisock.11029
srwx------ daemon daemon   0 B  Wed Dec 11 18:55:18 2024 󰆨 cgisock.26991
srwx------ daemon root     0 B  Thu Dec 12 00:11:02 2024 󰆨 cgisock.5614
srwx------ daemon root     0 B  Fri Dec 13 15:53:14 2024 󰆨 cgisock.954
.rw-rw-r-- daemon daemon 6.9 KB Sun Dec 15 22:40:53 2024  error_log
.rw-r--r-- root   root     6 B  Sun Dec 15 22:40:53 2024  httpd.pid
.rw-r--r-- daemon daemon 851 B  Sun Dec 15 22:45:17 2024  php_error_log
.rw-r--r-- daemon daemon   0 B  Fri Apr 19 11:26:16 2013  ssl_request_log
```

```bash
tail -f /opt/lampp/logs/php_error_log
```

- *El fichero `php_error_log` muestra los errores generados por el script PHP, por ejemplo, si el script no tiene permisos para escribir en el fichero `contacts.json`.*
- *Si ves un error similar a `Failed to open stream: Permission denied`, eso indica que PHP no puede escribir en el fichero debido a que el usuario que ejecuta PHP no tiene permisos de escritura en ese fichero o directorio.*

### **Problema de Permisos**

- *El error principal que está causando que no se almacenen los datos en el fichero `contacts.json` está relacionado con los **permisos de escritura** en el sistema de ficheros. Según el comando `lsd -lA` que has mostrado, los permisos del fichero `contacts.json` son los siguientes:*

```bash
lsd -l contacts.json
.rw-r--r-- daemon daemon 95 B Sun Dec 15 23:34:43 2024  contacts.json
```

- **Esto significa lo siguiente:**
- *`rw-r--r--`: El fichero tiene permisos de **lectura** y **escritura** para el **propietario** (que es `daemon`), y solo **lectura** para el **grupo** y los **otros** usuarios.*
- *`daemon daemon`: El fichero es propiedad del usuario `daemon` y del grupo `daemon`.*

- *Dado que PHP generalmente se ejecuta bajo el usuario `daemon` (o un usuario similar), el fichero debería ser accesible para escribir, pero si PHP está corriendo bajo otro usuario o grupo, entonces el fichero puede no ser escribible por PHP debido a la configuración de permisos.*

### **Solución de Permisos**

- **Una forma de corregir el problema es asegurarte de que el directorio y el fichero sean **escribibles** para el usuario bajo el cual se ejecuta el servidor PHP. Esto se puede lograr utilizando el comando `chmod` para cambiar los permisos.**

#### ***Comando para cambiar los permisos:***

```bash
chmod -R o+wx /App/contacts-app/
```

- *Este comando cambia los permisos del directorio `/App/contacts-app/` y sus ficheros para que cualquier usuario (incluyendo el que ejecuta PHP) pueda escribir en ellos. Los permisos `o+wx` asignan permisos de escritura (`w`) y ejecución (`x`) a **otros usuarios** (usuarios que no son ni el propietario ni parte del grupo).*

- *También puedes cambiar los permisos específicamente para el fichero `contacts.json` con:*

```bash
chmod 666 /App/contacts-app/contacts.json
```

- *Esto permitirá a **todos los usuarios** leer y escribir en el fichero.*

### **Realizando una Solicitud POST con cURL**

- *El comando `curl` que has mostrado simula el envío de datos a través de una solicitud HTTP `POST` hacia el script `edit.php`:*

```bash
curl -X POST --location --header "Content-Type: application/x-www-form-urlencoded" --data "name=Daniel+Benjamin+Perez+Morales&phone_number=12345678" http://172.17.0.2/contacts-app/edit.php
```

```bash
curl -X POST -L -H "Content-Type: application/x-www-form-urlencoded" -d "name=Danna+Isabella+Perez+Morales&phone_number=87654321" http://172.17.0.2/contacts-app/edit.php
```

- *Este comando envía los datos del formulario (nombre y número de teléfono) al servidor. El script PHP `edit.php` recibe estos datos a través de `$_POST["name"]` y `$_POST["phone_number"]` y, en teoría, debería procesarlos y almacenarlos en el fichero `contacts.json`. Sin embargo, si no tiene permisos de escritura, el servidor PHP generará un error.*

### **Flujo Completo del Almacenamiento de Datos**

- *Cuando se envía la solicitud `POST`:*
- *El navegador (o cURL en este caso) envía los datos al servidor.*
- *El servidor recibe los datos en el script PHP.*
- *PHP intenta guardar los datos en un fichero JSON.*
- *Si PHP tiene permisos de escritura en el fichero, lo guarda correctamente.*
- *Si no tiene permisos, se genera un error, que puede verse en el fichero `php_error_log` o en el navegador (si la salida no está suprimida).*

### ***Resumen:***

- *El servidor PHP no tiene permisos suficientes para escribir en el fichero `contacts.json` debido a permisos de fichero o directorio insuficientes.*
- *El fichero `contacts.json` necesita permisos de escritura para el usuario que ejecuta el servidor PHP (usualmente `daemon`).*
- *Utilizando el comando `chmod` se pueden cambiar los permisos y permitir que PHP escriba en el fichero.*
- *Si todo está configurado correctamente, los datos enviados a través de una solicitud `POST` pueden ser almacenados en el fichero `contacts.json`.*

```bash
curl --help all
```

```bash
Usage: curl [options...] <url>
     --abstract-unix-socket <path> Connect via abstract Unix domain socket
     --alt-svc <file name> Enable alt-svc with this cache file
     --anyauth     Pick any authentication method
 -a, --append      Append to target file when uploading
     --aws-sigv4 <provider1[:provider2[:region[:service]]]> Use AWS V4 signature authentication
     --basic       Use HTTP Basic Authentication
     --ca-native   Use CA certificates from the native OS
     --cacert <file> CA certificate to verify peer against
     --capath <dir> CA directory to verify peer against
 -E, --cert <certificate[:password]> Client certificate file and password
     --cert-status Verify the status of the server cert via OCSP-staple
     --cert-type <type> Certificate type (DER/PEM/ENG/P12)
     --ciphers <list of ciphers> SSL ciphers to use
     --compressed  Request compressed response
     --compressed-ssh Enable SSH compression
 -K, --config <file> Read config from a file
     --connect-timeout <fractional seconds> Maximum time allowed for connection
     --connect-to <HOST1:PORT1:HOST2:PORT2> Connect to host
 -C, --continue-at <offset> Resumed transfer offset
 -b, --cookie <data|filename> Send cookies from string/file
 -c, --cookie-jar <filename> Write cookies to <filename> after operation
     --create-dirs Create necessary local directory hierarchy
     --create-file-mode <mode> File mode for created files
     --crlf        Convert LF to CRLF in upload
     --crlfile <file> Use this CRL list
     --curves <algorithm list> (EC) TLS key exchange algorithm(s) to request
 -d, --data <data> HTTP POST data
     --data-ascii <data> HTTP POST ASCII data
     --data-binary <data> HTTP POST binary data
     --data-raw <data> HTTP POST data, '@' allowed
     --data-urlencode <data> HTTP POST data URL encoded
     --delegation <LEVEL> GSS-API delegation permission
     --digest      Use HTTP Digest Authentication
 -q, --disable     Disable .curlrc
     --disable-eprt Inhibit using EPRT or LPRT
     --disable-epsv Inhibit using EPSV
     --disallow-username-in-url Disallow username in URL
     --dns-interface <interface> Interface to use for DNS requests
     --dns-ipv4-addr <address> IPv4 address to use for DNS requests
     --dns-ipv6-addr <address> IPv6 address to use for DNS requests
     --dns-servers <addresses> DNS server addrs to use
     --doh-cert-status Verify the status of the DoH server cert via OCSP-staple
     --doh-insecure Allow insecure DoH server connections
     --doh-url <URL> Resolve host names over DoH
 -D, --dump-header <filename> Write the received headers to <filename>
     --egd-file <file> EGD socket path for random data
     --engine <name> Crypto engine to use
     --etag-compare <file> Pass an ETag from a file as a custom header
     --etag-save <file> Parse ETag from a request and save it to a file
     --expect100-timeout <seconds> How long to wait for 100-continue
 -f, --fail        Fail fast with no output on HTTP errors
     --fail-early  Fail on first transfer error, do not continue
     --fail-with-body Fail on HTTP errors but save the body
     --false-start Enable TLS False Start
 -F, --form <name=content> Specify multipart MIME data
     --form-escape Escape multipart form field/file names using backslash
     --form-string <name=string> Specify multipart MIME data
     --ftp-account <data> Account data string
     --ftp-alternative-to-user <command> String to replace USER [name]
     --ftp-create-dirs Create the remote dirs if not present
     --ftp-method <method> Control CWD usage
     --ftp-pasv    Use PASV/EPSV instead of PORT
 -P, --ftp-port <address> Use PORT instead of PASV
     --ftp-pret    Send PRET before PASV
     --ftp-skip-pasv-ip Skip the IP address for PASV
     --ftp-ssl-ccc Send CCC after authenticating
     --ftp-ssl-ccc-mode <active/passive> Set CCC mode
     --ftp-ssl-control Require SSL/TLS for FTP login, clear for transfer
 -G, --get         Put the post data in the URL and use GET
 -g, --globoff     Disable URL sequences and ranges using {} and []
     --happy-eyeballs-timeout-ms <milliseconds> Time for IPv6 before trying IPv4
     --haproxy-clientip Sets client IP in HAProxy PROXY protocol v1 header
     --haproxy-protocol Send HAProxy PROXY protocol v1 header
 -I, --head        Show document info only
 -H, --header <header/@file> Pass custom header(s) to server
 -h, --help <category> Get help for commands
     --hostpubmd5 <md5> Acceptable MD5 hash of the host public key
     --hostpubsha256 <sha256> Acceptable SHA256 hash of the host public key
     --hsts <file name> Enable HSTS with this cache file
     --http0.9     Allow HTTP 0.9 responses
 -0, --http1.0     Use HTTP 1.0
     --http1.1     Use HTTP 1.1
     --http2       Use HTTP/2
     --http2-prior-knowledge Use HTTP 2 without HTTP/1.1 Upgrade
     --http3       Use HTTP v3
     --http3-only  Use HTTP v3 only
     --ignore-content-length Ignore the size of the remote resource
 -i, --include     Include protocol response headers in the output
 -k, --insecure    Allow insecure server connections
     --interface <name> Use network INTERFACE (or address)
     --ipfs-gateway <URL> Gateway for IPFS
 -4, --ipv4        Resolve names to IPv4 addresses
 -6, --ipv6        Resolve names to IPv6 addresses
     --json <data> HTTP POST JSON
 -j, --junk-session-cookies Ignore session cookies read from file
     --keepalive-time <seconds> Interval time for keepalive probes
     --key <key>   Private key file name
     --key-type <type> Private key file type (DER/PEM/ENG)
     --krb <level> Enable Kerberos with security <level>
     --libcurl <file> Dump libcurl equivalent code of this command line
     --limit-rate <speed> Limit transfer speed to RATE
 -l, --list-only   List only mode
     --local-port <num/range> Force use of RANGE for local port numbers
 -L, --location    Follow redirects
     --location-trusted Like --location, and send auth to other hosts
     --login-options <options> Server login options
     --mail-auth <address> Originator address of the original email
     --mail-from <address> Mail from this address
     --mail-rcpt <address> Mail to this address
     --mail-rcpt-allowfails Allow RCPT TO command to fail for some recipients
 -M, --manual      Display the full manual
     --max-filesize <bytes> Maximum file size to download
     --max-redirs <num> Maximum number of redirects allowed
 -m, --max-time <fractional seconds> Maximum time allowed for transfer
     --metalink    Process given URLs as metalink XML file
     --negotiate   Use HTTP Negotiate (SPNEGO) authentication
 -n, --netrc       Must read .netrc for user name and password
     --netrc-file <filename> Specify FILE for netrc
     --netrc-optional Use either .netrc or URL
 -:, --next        Make next URL use its separate set of options
     --no-alpn     Disable the ALPN TLS extension
 -N, --no-buffer   Disable buffering of the output stream
     --no-clobber  Do not overwrite files that already exist
     --no-keepalive Disable TCP keepalive on the connection
     --no-npn      Disable the NPN TLS extension
     --no-progress-meter Do not show the progress meter
     --no-sessionid Disable SSL session-ID reusing
     --noproxy <no-proxy-list> List of hosts which do not use proxy
     --ntlm        Use HTTP NTLM authentication
     --ntlm-wb     Use HTTP NTLM authentication with winbind
     --oauth2-bearer <token> OAuth 2 Bearer Token
 -o, --output <file> Write to file instead of stdout
     --output-dir <dir> Directory to save files in
 -Z, --parallel    Perform transfers in parallel
     --parallel-immediate Do not wait for multiplexing (with --parallel)
     --parallel-max <num> Maximum concurrency for parallel transfers
     --pass <phrase> Pass phrase for the private key
     --path-as-is  Do not squash .. sequences in URL path
     --pinnedpubkey <hashes> FILE/HASHES Public key to verify peer against
     --post301     Do not switch to GET after following a 301
     --post302     Do not switch to GET after following a 302
     --post303     Do not switch to GET after following a 303
     --preproxy [protocol://]host[:port] Use this proxy first
 -#, --progress-bar Display transfer progress as a bar
     --proto <protocols> Enable/disable PROTOCOLS
     --proto-default <protocol> Use PROTOCOL for any URL missing a scheme
     --proto-redir <protocols> Enable/disable PROTOCOLS on redirect
 -x, --proxy [protocol://]host[:port] Use this proxy
     --proxy-anyauth Pick any proxy authentication method
     --proxy-basic Use Basic authentication on the proxy
     --proxy-ca-native Use CA certificates from the native OS for proxy
     --proxy-cacert <file> CA certificate to verify peer against for proxy
     --proxy-capath <dir> CA directory to verify peer against for proxy
     --proxy-cert <cert[:passwd]> Set client certificate for proxy
     --proxy-cert-type <type> Client certificate type for HTTPS proxy
     --proxy-ciphers <list> SSL ciphers to use for proxy
     --proxy-crlfile <file> Set a CRL list for proxy
     --proxy-digest Use Digest authentication on the proxy
     --proxy-header <header/@file> Pass custom header(s) to proxy
     --proxy-http2 Use HTTP/2 with HTTPS proxy
     --proxy-insecure Do HTTPS proxy connections without verifying the proxy
     --proxy-key <key> Private key for HTTPS proxy
     --proxy-key-type <type> Private key file type for proxy
     --proxy-negotiate Use HTTP Negotiate (SPNEGO) authentication on the proxy
     --proxy-ntlm  Use NTLM authentication on the proxy
     --proxy-pass <phrase> Pass phrase for the private key for HTTPS proxy
     --proxy-pinnedpubkey <hashes> FILE/HASHES public key to verify proxy with
     --proxy-service-name <name> SPNEGO proxy service name
     --proxy-ssl-allow-beast Allow security flaw for interop for HTTPS proxy
     --proxy-ssl-auto-client-cert Use auto client certificate for proxy (Schannel)
     --proxy-tls13-ciphers <ciphersuite list> TLS 1.3 proxy cipher suites
     --proxy-tlsauthtype <type> TLS authentication type for HTTPS proxy
     --proxy-tlspassword <string> TLS password for HTTPS proxy
     --proxy-tlsuser <name> TLS username for HTTPS proxy
     --proxy-tlsv1 Use TLSv1 for HTTPS proxy
 -U, --proxy-user <user:password> Proxy user and password
     --proxy1.0 <host[:port]> Use HTTP/1.0 proxy on given port
 -p, --proxytunnel Operate through an HTTP proxy tunnel (using CONNECT)
     --pubkey <key> SSH Public key file name
 -Q, --quote <command> Send command(s) to server before transfer
     --random-file <file> File for reading random data from
 -r, --range <range> Retrieve only the bytes within RANGE
     --rate <max request rate> Request rate for serial transfers
     --raw         Do HTTP "raw"; no transfer decoding
 -e, --referer <URL> Referrer URL
 -J, --remote-header-name Use the header-provided filename
 -O, --remote-name Write output to a file named as the remote file
     --remote-name-all Use the remote file name for all URLs
 -R, --remote-time Set the remote file's time on the local output
     --remove-on-error Remove output file on errors
 -X, --request <method> Specify request method to use
     --request-target <path> Specify the target for this request
     --resolve <[+]host:port:addr[,addr]...> Resolve the host+port to this address
     --retry <num> Retry request if transient problems occur
     --retry-all-errors Retry all errors (use with --retry)
     --retry-connrefused Retry on connection refused (use with --retry)
     --retry-delay <seconds> Wait time between retries
     --retry-max-time <seconds> Retry only within this period
     --sasl-authzid <identity> Identity for SASL PLAIN authentication
     --sasl-ir     Enable initial response in SASL authentication
     --service-name <name> SPNEGO service name
 -S, --show-error  Show error even when -s is used
 -s, --silent      Silent mode
     --socks4 <host[:port]> SOCKS4 proxy on given host + port
     --socks4a <host[:port]> SOCKS4a proxy on given host + port
     --socks5 <host[:port]> SOCKS5 proxy on given host + port
     --socks5-basic Enable username/password auth for SOCKS5 proxies
     --socks5-gssapi Enable GSS-API auth for SOCKS5 proxies
     --socks5-gssapi-nec Compatibility with NEC SOCKS5 server
     --socks5-gssapi-service <name> SOCKS5 proxy service name for GSS-API
     --socks5-hostname <host[:port]> SOCKS5 proxy, pass host name to proxy
 -Y, --speed-limit <speed> Stop transfers slower than this
 -y, --speed-time <seconds> Trigger 'speed-limit' abort after this time
     --ssl         Try SSL/TLS
     --ssl-allow-beast Allow security flaw to improve interop
     --ssl-auto-client-cert Use auto client certificate (Schannel)
     --ssl-no-revoke Disable cert revocation checks (Schannel)
     --ssl-reqd    Require SSL/TLS
     --ssl-revoke-best-effort Ignore missing/offline cert CRL dist points (Schannel)
 -2, --sslv2       Use SSLv2
 -3, --sslv3       Use SSLv3
     --stderr <file> Where to redirect stderr
     --styled-output Enable styled output for HTTP headers
     --suppress-connect-headers Suppress proxy CONNECT response headers
     --tcp-fastopen Use TCP Fast Open
     --tcp-nodelay Use the TCP_NODELAY option
 -t, --telnet-option <opt=val> Set telnet option
     --tftp-blksize <value> Set TFTP BLKSIZE option
     --tftp-no-options Do not send any TFTP options
 -z, --time-cond <time> Transfer based on a time condition
     --tls-max <VERSION> Set maximum allowed TLS version
     --tls13-ciphers <ciphersuite list> TLS 1.3 cipher suites to use
     --tlsauthtype <type> TLS authentication type
     --tlspassword <string> TLS password
     --tlsuser <name> TLS user name
 -1, --tlsv1       Use TLSv1.0 or greater
     --tlsv1.0     Use TLSv1.0 or greater
     --tlsv1.1     Use TLSv1.1 or greater
     --tlsv1.2     Use TLSv1.2 or greater
     --tlsv1.3     Use TLSv1.3 or greater
     --tr-encoding Request compressed transfer encoding
     --trace <file> Write a debug trace to FILE
     --trace-ascii <file> Like --trace, but without hex output
     --trace-config <string> Details to log in trace/verbose output
     --trace-ids   Add transfer and connection identifiers to trace/verbose output
     --trace-time  Add time stamps to trace/verbose output
     --unix-socket <path> Connect through this Unix domain socket
 -T, --upload-file <file> Transfer local FILE to destination
     --url <url>   URL to work with
     --url-query <data> Add a URL query part
 -B, --use-ascii   Use ASCII/text transfer
 -u, --user <user:password> Server user and password
 -A, --user-agent <name> Send User-Agent <name> to server
     --variable <[%]name=text/@file> Set variable
 -v, --verbose     Make the operation more talkative
 -V, --version     Show version number and quit
 -w, --write-out <format> Use output FORMAT after completion
     --xattr       Store metadata in extended file attributes
```
