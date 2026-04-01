from typing import List, Union
from pydantic import BaseModel, field_validator

class DatosGeneradorDTO(BaseModel):
    name: str
    interests: Union[str, List[str]]
    topics: Union[str, List[str]]
    description: str
    leisureType: str
    activityTemplate: str
    typeTemplate: str
    participantsTemplate: int
    durationTemplate: str
    kidFriendlyTemplate: bool

    @field_validator('interests', 'topics', mode='before')
    @classmethod
    def split_if_string(cls, v):
        if isinstance(v, str):
            return [item.strip() for item in v.split(',') if item.strip()]
        return v