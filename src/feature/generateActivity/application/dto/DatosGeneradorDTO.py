from pydantic import BaseModel

class DatosGeneradorDTO(BaseModel):
    # Campos del usuario
    name: str
    interests: str
    topics: str
    description: str
    leisureType: str
    # Campos de la plantilla (Bored API)
    activity_template: str
    type_template: str
    participants_template: int
    duration_template: str
    kidFriendly_template: bool
