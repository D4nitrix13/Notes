<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Comandos A Ejecutar***

```bash
docker container rename stoic_hoover todo-sobre-la-web
```

```bash
docker image tag vsc-todosobrelawebphp-dbada673df8aa06f6ffbb968ef82c11c358b8be32cbe69bfca2b80516fd00f2d-uid:latest d4nitrix13/web-php:latest
```

```bash
docker container stop --signal SIGTERM $(docker container list --all --filter ancestor=vsc-todosobrelawebphp-dbada673df8aa06f6ffbb968ef82c11c358b8be32cbe69bfca2b80516fd00f2d-uid:latest --filter status=running --quiet)
```

```bash
docker rm todo-sobre-la-web
docker rmi vsc-todosobrelawebphp-dbada673df8aa06f6ffbb968ef82c11c358b8be32cbe69bfca2b80516fd00f2d-uid:latest --force
```
