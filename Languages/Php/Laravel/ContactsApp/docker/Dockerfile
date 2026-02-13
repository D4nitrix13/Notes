# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Construction
# docker image build --tag d4nitrix13/laravel-guide --no-cache -f "Dockerfile.dev" "$(pwd)"

# Recurso https://docs.docker.com/build/building/best-practices/

ARG VERSION=3.19
ARG USERNAME=zeus
ARG UID=1000
ARG GID=1000
ARG PORT=8000/tcp
ARG WORKDIR=/contacts-application/
ARG SIGNAL=15

FROM alpine:${VERSION}

ARG USERNAME
ARG UID
ARG GID
ARG PORT
ARG WORKDIR
ARG SIGNAL

RUN /sbin/apk update && /sbin/apk upgrade && \
    /sbin/apk add --no-cache libpq-dev php php-pdo_pgsql php-pgsql php-cli php-fpm php-opcache \
    php-pdo php-json php-phar php-mbstring php-xml php-xmlwriter php-dom php-session php-curl \
    php-ctype php-zip php-bcmath php-tokenizer php-iconv php-fileinfo composer tini npm curl && \
    adduser -DHu ${UID} "${USERNAME}"

# --chown=zeus:zeus -> --chown=1000:1000
WORKDIR ${WORKDIR}
COPY --chown=${UID}:${GID} composer.* package.json package-lock.json ${WORKDIR}
COPY --chown=${UID}:${GID} ./ ${WORKDIR}

# SIGTERM -> 15
STOPSIGNAL ${SIGNAL}

SHELL [ "/bin/sh", "-lic" ]
HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=30s \
    CMD /usr/bin/curl --silent --fail -X GET http://0.0.0.0:8000 || exit 1

# root -> 0
USER 0

RUN /bin/chown -R ${UID}:${GID} ${WORKDIR}
RUN composer install -o && npm install

# zeus -> 1000
USER ${UID}

EXPOSE ${PORT}
LABEL Stage="Production"
LABEL Maintainer="Daniel Benjamin Perez Morales"
LABEL Email="danielperezdev@proton.me"
LABEL Github="https://github.com/D4nitrix13"
LABEL Gitlab="https://gitlab.com/D4nitrix13"

ENTRYPOINT [ "tini", "--" ]
# /contacts-application/scripts/runApp.sh
CMD [ "/bin/sh", "scripts/runApp.sh" ]

