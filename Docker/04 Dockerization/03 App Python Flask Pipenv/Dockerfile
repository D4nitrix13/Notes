# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Usamos la imagen base oficial de Python 3.10
# Esta imagen incluye Python y sus herramientas asociadas preinstaladas
FROM python:3.10

# Instalamos Pipenv, una herramienta de gestión de entornos virtuales y dependencias para Python
RUN pip install pipenv

# Definimos la variable de entorno FLASK_APP para apuntar al fichero principal de la aplicación Flask
# Esto indica a Flask dónde encontrar la aplicación cuando se ejecute
ENV FLASK_APP=./src.app

# Configuramos Pipenv para crear el entorno virtual dentro del directorio del proyecto
# Esto asegura que el entorno virtual se almacene en el directorio del proyecto en lugar de en el directorio de usuario
ENV PIPENV_VENV_IN_PROJECT=1


# Creamos el directorio de trabajo dentro del contenedor y lo establecemos como el directorio actual
# Todos los comandos subsiguientes se ejecutarán desde este directorio
WORKDIR /App

# Copiamos los ficheros Pipfile y Pipfile.lock al directorio de trabajo del contenedor
# Estos ficheros contienen las dependencias necesarias para la aplicación
COPY ./Pipfile* ./

# Instalamos las dependencias especificadas en Pipfile usando Pipenv
# Esto configura el entorno virtual con todas las bibliotecas necesarias
RUN pipenv install

# Copiamos todos los ficheros del proyecto desde el host al contenedor
# Esto incluye el código fuente de la aplicación y cualquier otro recurso necesario
COPY ./ ./

# Exponemos el puerto 5000 para permitir el acceso externo a la aplicación Flask
# Este es el puerto por defecto en el que Flask escucha
EXPOSE 5000

# Iniciamos el servidor Flask usando Pipenv para activar el entorno virtual
# La opción --host 0.0.0.0 permite que la aplicación sea accesible desde cualquier dirección IP
CMD pipenv run flask run --host 0.0.0.0
