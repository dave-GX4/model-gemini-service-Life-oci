from dataclasses import dataclass

@dataclass
class ActividadSugerida:
    titulo: str
    descripcion: str
    categoria: str
    duracion_estimada: str
    socialType: str

@dataclass
class GeneradorParametros:
    # Datos del Usuario
    user_name: str
    user_interests: str
    user_topic: str
    user_description: str
    user_leisure_type: str
    # Datos de la Plantilla (Bored API)
    template_activity: str
    template_type: str
    template_participants: int
    template_duration: str
    template_kid_friendly: bool