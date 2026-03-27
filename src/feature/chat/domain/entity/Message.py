from dataclasses import dataclass

@dataclass
class UsuarioContexto:
    mensaje: str
    contexto_extra: str | None