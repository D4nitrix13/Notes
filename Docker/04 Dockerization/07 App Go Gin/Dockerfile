# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# ------------------------------------Inicio Stage 0----------------------------------

# Se utiliza la imagen base de golang, ideal para ejecutar aplicaciones con Go.
FROM golang AS builder

# Define el directorio de trabajo dentro del contenedor, que es donde se ejecutará la aplicación Go.
WORKDIR /App

# Añade la ruta de Go al PATH para permitir el acceso a los comandos de Go globalmente dentro del contenedor.
ENV PATH="$PATH:/usr/local/go/bin"

# Copia los ficheros go.mod y go.sum al directorio de trabajo. Estos ficheros contienen las dependencias del proyecto Go.
COPY go.* ./

# Ejecuta la descarga de todas las dependencias necesarias especificadas en go.mod.
RUN go mod download

# Copia todo el código fuente de la aplicación al directorio de trabajo del contenedor.
COPY ./ ./

# Compila el código fuente de Go, generando un binario de la aplicación con las librerías enlazadas de forma estática, 
# asegurando así que el ejecutable no dependa de bibliotecas externas en tiempo de ejecución.
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o App-Go

# ------------------------------------Final Stage 0-----------------------------------

# ------------------------------------Inicio Stage 1----------------------------------

# Usamos la imagen base de alpine:latest
FROM alpine:latest

# Establecemos el directorio de trabajo en /App
WORKDIR /App

# Copiamos los ficheros desde la primera fase (etapa 0) al directorio actual
# en el contenedor. Esto asume que en la primera etapa (multi-stage build),
# los ficheros de la aplicación Go se construyeron en /App/App-Go.
COPY --from=builder /App/App-Go ./

# Expone el puerto 8080, que es el puerto en el que la aplicación Go estará escuchando.
EXPOSE 8080

# Define el comando por defecto que ejecutará la aplicación Go cuando se inicie el contenedor.
CMD ./App-Go

# ------------------------------------Final Stage 1-----------------------------------