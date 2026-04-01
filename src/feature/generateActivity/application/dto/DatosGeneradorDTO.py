from typing import List, Union
from pydantic import BaseModel, field_validator

class DatosGeneradorDTO(BaseModel):
    name: str
    interests: Union[str, List[str]] = []
    topics: Union[str, List[str]] = []
    description: str
    leisureType: str
    activityTemplate: str
    typeTemplate: str
    participantsTemplate: int
    durationTemplate: str
    kidFriendlyTemplate: bool

    @field_validator('interests', 'topics', mode='before')
    @classmethod
    def normalize_to_list(cls, v):
        # Si es null/undefined
        if v is None:
            return []
        
        # Si es string (viene separado por comas)
        if isinstance(v, str):
            if not v.strip():
                return []
            return [item.strip() for item in v.split(',') if item.strip()]
        
        # Si ya es lista (viene del cliente como array)
        if isinstance(v, list):
            # Asegurar que todos los elementos sean strings válidos
            return [str(item).strip() for item in v if item is not None and str(item).strip()]
        
        return v