#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

""""
OCP": "Open Closed Principle" Significa en español Principio abierto cerrado. 

Este principio dice que una clase debe estar abierta para extenderse pero cerrada para modificarse.

Este principio evita que los desarrolladores modifiquen una clase y que afecte el funcionamiento de otras clases.
"""


# Nosotros debemos desarrollar un sistema para agregar nuevas funcionalidades sin modificar el codigo existente

# Ejemplo de un sistema de notificaciones" que notifique a los usuarios por email, sms, whatsapp, twitter, etc

from sys import stdout
from typing import Any, NoReturn, Union
class Notificador:
    def __init__(self: 'Notificador', usuario: Any, mensaje: str) -> None:
        self.usuario: Any = usuario
        self.mensaje: str = mensaje
        return None

    def notificar(self: 'Notificador') -> Union[NoReturn, str]:
        raise NotImplementedError("Este metodo debe ser implementado en la subclase")

class NotificadorEmail(Notificador):
    def __init__(self: 'NotificadorEmail', usuario: Any, mensaje: str) -> None:
        super().__init__(usuario = usuario, mensaje = mensaje)
        return None

    def notificar(self: 'NotificadorEmail') -> Union[NoReturn, str]:
        # Recordablemente que usuario sea un objeto y que tenga un atributo email
        return f"Enviando email a {self.usuario.email}"

class NotificadorSMS(Notificador):
    def __init__(self: 'NotificadorSMS', usuario: Any, mensaje: str) -> None:
        super().__init__(usuario = usuario, mensaje = mensaje)
        return None

    def notificar(self: 'NotificadorSMS') -> Union[NoReturn, str]:
        # Recordablemente que usuario sea un objeto y que tenga un atributo sms
        return f"Enviando email a {self.usuario.sms}"

class NotificadorWhatsApp(Notificador):
    def __init__(self: 'NotificadorWhatsApp', usuario: Any, mensaje: str) -> None:
        super().__init__(usuario = usuario, mensaje = mensaje)
        return None

    def notificar(self: 'NotificadorWhatsApp') -> Union[NoReturn, str]:
        # Recordablemente que usuario sea un objeto y que tenga un atributo whatsapp
        return f"Enviando email a {self.usuario.whatsapp}"

class NotificadorTwitter(Notificador):
    def __init__(self: 'NotificadorTwitter', usuario: Any, mensaje: str) -> None:
        super().__init__(usuario = usuario, mensaje = mensaje)
        return None

    def notificar(self: 'NotificadorTwitter') -> Union[NoReturn, str]:
        # Recordablemente que usuario sea un objeto y que tenga un atributo twitter
        return f"Enviando email a {self.usuario.twitter}"

notificacion: Notificador = Notificador(usuario = "Daniel", mensaje = "Hola, como estas?")
print(notificacion.notificar(),end="\n", file = stdout)
