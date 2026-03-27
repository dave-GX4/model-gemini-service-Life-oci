from pydantic import BaseModel

class SolicitudUsuarioDTO(BaseModel):
    mensaje: str
    contexto_extra: str | None = None