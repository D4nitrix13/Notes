# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Foros
# https://stackoverflow.com/questions/47904974/what-are-shell-form-and-exec-form
# https://stackoverflow.com/questions/60530319/docker-cmd-when-should-shell-form-be-used
# docker image build --tag d4nitrix13/webphp:latest ./

ARG TAG=latest
ARG PLATAFORM=linux/amd64

FROM --platform=${PLATAFORM} ubuntu:${TAG} AS build

ARG PORT=80
ARG DIRECTORY=/App
RUN mkdir -p ${DIRECTORY}/ContactsApp
WORKDIR ${DIRECTORY}
COPY --chown=root:root ./ ${DIRECTORY}/ContactsApp

RUN apt update && apt-get install tini wget libx11-6 libxext6 iproute2 net-tools -y && \
    wget https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run && \
    chmod u+x ./xampp-linux-x64-8.2.12-0-installer.run && \
    yes | ./xampp-linux-x64-8.2.12-0-installer.run && \
    ln -sf ${DIRECTORY}/ContactsApp/ /opt/lampp/htdocs/ContactsApp && \
    /opt/lampp/lampp start && sleep 1 && /opt/lampp/bin/mysql -h localhost -P 3306 -u root --password='' -e "DROP USER IF EXISTS '$(whoami)'@'$(ip route | tail -n 1 | awk 'NF{print $NF}')'; CREATE USER '$(whoami)'@'$(ip route | tail -n 1 | awk 'NF{print $NF}')' IDENTIFIED BY ''; GRANT ALL PRIVILEGES ON *.* TO '$(whoami)'@'$(ip route | tail -n 1 | awk 'NF{print $NF}')' WITH GRANT OPTION; FLUSH PRIVILEGES" && \
    ln -sf ${DIRECTORY}/ContactsApp /opt/lampp/htdocs/ContactsApp && \
    /opt/lampp/lampp start && sleep 2 && /opt/lampp/bin/mysql -h localhost -P 3306 -u root --password='' -e "SOURCE ${DIRECTORY}/ContactsApp/sql/setup.sql";

LABEL org.opencontainers.image.authors="D4nitrix13"
LABEL org.opencontainers.image.email="danielperezdev@proton.me"
LABEL org.opencontainers.image.github="https://github.com/D4nitrix13"
MAINTAINER "D4nitrix13" "danielperezdev@proton.me"
ENV PATH="$PATH:/opt/lampp/bin"

SHELL [ "/usr/bin/bash", "-c" ]
STOPSIGNAL SIGTERM
VOLUME [ "/App" ]
EXPOSE ${PORT}
ENTRYPOINT [ "tini", "--" ]
CMD /opt/lampp/lampp start && sleep infinity

# docker container run --interactive --tty \
#     --detach \
#     --privileged \
#     --env "DISPLAY=$DISPLAY" --volume "/tmp/.X11-unix:/tmp/.X11-unix" \
#     --expose 80 \
#     --publish 80:80 \
#     --network bridge \
#     --stop-signal SIGTERM \
#     --restart unless-stopped \
#     --init \
#     --user root \
#     --dns 8.8.8.8 \
#     --device /dev/snd \
#     --name application-web \
#     d4nitrix13/webphp:latest
