from pydantic import BaseModel

class DatosGeneradorDTO(BaseModel):
    hora_actual: str
    estado_animo: str
    intereses: str
    tiempo_disponible: str