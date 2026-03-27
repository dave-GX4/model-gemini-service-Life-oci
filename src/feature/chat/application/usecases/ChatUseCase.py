from src.core.services.interface.IA_ServiceInterface import IA_ServiceInterface
from src.feature.chat.domain.entity.Message import UsuarioContexto

class ChatUseCase:
    def __init__(self, ia_service: IA_ServiceInterface):
        self.ia_service = ia_service

    async def execute(self, mensaje: str, contexto: str | None):
        entidad = UsuarioContexto(mensaje=mensaje, contexto_extra=contexto)
        return await self.ia_service.generar_chat(entidad)