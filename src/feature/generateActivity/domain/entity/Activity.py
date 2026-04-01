from typing import List
from dataclasses import dataclass

@dataclass
class ActividadSugerida:
    titulo: str
    descripcion: str
    type: str
    categoria: str
    duracionEstimada: str
    socialType: str

@dataclass
class GeneradorParametros:
    userName: str
    userInterests: List[str]
    userTopics: List[str]
    userDescription: str
    userLeisureType: str
    templateActivity: str
    templateType: str
    templateParticipants: int
    templateDuration: str
    templateKidFriendly: bool