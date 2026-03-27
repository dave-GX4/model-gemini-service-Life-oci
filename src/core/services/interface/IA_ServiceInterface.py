from abc import ABC, abstractmethod
from feature.chat.domain.entity.message import UsuarioContexto
from feature.generateActivity.domain.entity.activity import ActividadSugerida, GeneradorParametros

class IA_ServiceInterface(ABC):
    @abstractmethod
    async def generar_chat(self, contexto: UsuarioContexto) -> str:
        pass

    @abstractmethod
    async def generar_actividad_dopamina(self, params: GeneradorParametros) -> ActividadSugerida:
        pass