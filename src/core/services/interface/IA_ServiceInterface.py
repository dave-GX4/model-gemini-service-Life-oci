from abc import ABC, abstractmethod
from src.feature.chat.domain.entity.Message import UsuarioContexto
from src.feature.generateActivity.domain.entity.Activity import ActividadSugerida, GeneradorParametros


class IA_ServiceInterface(ABC):
    @abstractmethod
    async def generar_chat(self, contexto: UsuarioContexto) -> str:
        pass

    @abstractmethod
    async def generar_actividad_dopamina(self, params: GeneradorParametros) -> ActividadSugerida:
        pass